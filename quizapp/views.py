from django.shortcuts import render
from rest_framework import viewsets
from .models import Category, Subcategory, Question
from .serializers import CategorySerializer, SubCategorySerializer, QuestionSerializer
# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset= Category.objects.all()
    serializer_class = CategorySerializer

class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    seriallizer_class = SubCategorySerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


def homepage(request):
    return render(request,'quizapp/index.html')

def category(request):
    return render(request,'quizapp/category.html')

def subcategory(request):
    return render(request,'quizapp/subcategory.html')

def quiz(request):
    return render(request,'quizapp/quiz.html')

def result(request):
    return render(request,'quizapp/result.html')