# Improts from Django
from django.db.models import Q
from django.contrib.auth import get_user_model

#  Importing form rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Importing Models
from colleges.models import College
from universities.models import University
from posts.models import Post

# Importing Serailizers
from accounts.serializers import UserSearchBoxProfileCardSerializer
from colleges.serializers import CollegeMiniDataSerializer
from universities.serializers import UniversityMiniDataSerializer
from posts.serializers import PostSerializer

# Additional Imports
from utilities.response.response_utilities import ResponseUtilities

# Import for advanced query splitting, stop word removal
from nltk.corpus import stopwords
import re

# Getting the User Model with the django provided function
User = get_user_model()

class SearchView(APIView, ResponseUtilities):
    authentication_classes = []

    def get(self, request, format=None):
        query = request.query_params.get('search-for', '')
        self.response_data = {
            'users': [],
            'colleges': [],
            'universities': [],
            'posts': []  # Add posts to the response
        }
        self.success_status = True

        if not query:
            return Response(self.get_generated_response())

        # Process the query into terms for advanced boolean search
        processed_query = self.process_query(query)
        if not processed_query:
            return Response(self.get_generated_response())

        try:
            # Get results from different models
            self.response_data['users'] = self.search_users(processed_query)
            self.response_data['colleges'] = self.search_colleges(processed_query)
            self.response_data['universities'] = self.search_universities(processed_query)
            self.response_data['posts'] = self.search_posts(processed_query)

        except Exception as e:
            self.success_status = False
            self.messege_to_client = str(e)
            return Response(self.get_generated_response())

        return Response(self.get_generated_response())

    def process_query(self, query):
        """
        Split the query, remove stop words, and prepare terms for advanced searching.
        """
        query = re.sub(r'[^\w\s]', '', query.lower())
        terms = query.split()

        stop_words = set(stopwords.words('english'))
        processed_terms = [term for term in terms if term not in stop_words]

        return processed_terms

    def search_users(self, terms):
        """
        Search for users using the processed query terms.
        """
        try:
            user_qs = Q()
            for term in terms:
                user_qs &= Q(full_name__icontains=term) | Q(username__icontains=term)
            
            users = User.objects.filter(user_qs).prefetch_related(
                'collegeconnection_set__college',
                'universityconnection_set__university'
            )[:3]

            return UserSearchBoxProfileCardSerializer(users, many=True).data
        except Exception as e:
            self.success_status = False
            self.messege_to_client = f"User search error: {str(e)}"
            return []

    def search_colleges(self, terms):
        """
        Search for colleges using the processed query terms.
        """
        try:
            # Build a query for colleges
            college_qs = Q()
            for term in terms:
                college_qs &= Q(name__icontains=term)
            
            colleges = College.objects.filter(college_qs)[:3]  # Limit to 3 results
            return CollegeMiniDataSerializer(colleges, many=True).data

        except Exception as e:
            self.success_status = False
            self.messege_to_client = f"College search error: {str(e)}"
            return []

    def search_universities(self, terms):
        """
        Search for universities using the processed query terms.
        """
        try:
            # Build a query for universities
            university_qs = Q()
            for term in terms:
                university_qs &= Q(name__icontains=term)
            
            universities = University.objects.filter(university_qs)[:3]  # Limit to 3 results\
            return UniversityMiniDataSerializer(universities, many=True).data

        except Exception as e:
            self.success_status = False
            self.messege_to_client = f"University search error: {str(e)}"
            return []

    def search_posts(self, terms):
        """
        Search for posts using the processed query terms.
        """
        try:
            # Build a query for posts
            post_qs = Q()
            for term in terms:
                post_qs &= Q(caption__icontains=term)
            
            posts = Post.objects.filter(post_qs).select_related('user', 'college')[:5]  # Limit to 5 results
            return PostSerializer(posts, many=True).data

        except Exception as e:
            self.success_status = False
            self.messege_to_client = f"Post search error: {str(e)}"
            return []