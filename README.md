# Boolean Retrieval System for Social Media Search

## Overview

This project implements a **Boolean Retrieval System** designed to enhance search functionalities within a social media platform. By efficiently querying user profiles, college and university information, and posts, the system delivers fast and accurate results tailored to user queries.

## Features

- **Multi-Entity Search**: Retrieve results for users, colleges, universities, and posts.
- **Natural Language Processing (NLP)**: Processes search queries using techniques like stop word removal to enhance result relevance.
- **Django & REST Framework**: Built on the Django framework for robust performance and scalability.

## Technologies Used

- **Django**: A high-level Python web framework for rapid development.
- **Django REST Framework**: A toolkit for building Web APIs.
- **NLTK**: A leading platform for building Python programs to work with human language data.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

To search, send a GET request to the search endpoint with a query parameter. For example:
```
GET /search?search-for=your_query
```

## Reason for Using Boolean Retrieval System

The Boolean Retrieval System is implemented for its **speed** and **accuracy**, making it ideal for social media searches where users expect quick and relevant results.

## References

1. Django Documentation. (n.d.). Retrieved from [Django Documentation](https://docs.djangoproject.com)
2. Django REST Framework. (n.d.). Retrieved from [Django REST Framework](https://www.django-rest-framework.org)
3. NLTK Documentation. (n.d.). Retrieved from [NLTK Documentation](https://www.nltk.org)
4. Cooper, W. S. (2019). *Information Retrieval: Data Structures and Algorithms*. Retrieved from [Amazon](https://www.amazon.com)
