from django.shortcuts import render
from rest_framework import generics
from .models import Author, Book, Student, BorrowingTransaction
from .serializers import AuthorSerializer, BookSerializer, StudentSerializer, BorrowingTransactionSerializer

# Author Views
class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

# Book Views
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Student Views
class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Borrowing Transaction Views
class BorrowingTransactionListCreateView(generics.ListCreateAPIView):
    queryset = BorrowingTransaction.objects.all()
    serializer_class = BorrowingTransactionSerializer

class BorrowingTransactionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BorrowingTransaction.objects.all()
    serializer_class = BorrowingTransactionSerializer
