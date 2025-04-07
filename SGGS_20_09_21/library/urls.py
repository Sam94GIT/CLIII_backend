"""
URL configuration for SGGS_20_09_21 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import (
    AuthorListCreateView, AuthorDetailView,
    BookListCreateView, BookDetailView,
    StudentListCreateView, StudentDetailView,
    BorrowingTransactionListCreateView, BorrowingTransactionDetailView
)

urlpatterns = [
    # Author Endpoints
    path('authors/', AuthorListCreateView.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),

    # Book Endpoints
    path('books/', BookListCreateView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # Student Endpoints
    path('students/', StudentListCreateView.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),

    # Borrowing Transaction Endpoints
    path('transactions/', BorrowingTransactionListCreateView.as_view(), name='transaction-list'),
    path('transactions/<int:pk>/', BorrowingTransactionDetailView.as_view(), name='transaction-detail'),
]