from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, SubCategoryViewSet, QuestionViewSet
from . import views


router = DefaultRouter()
router.register(r'categories',CategoryViewSet)
router.register(r'subcategories',SubCategoryViewSet)
router.register(r'questions',QuestionViewSet)

urlpatterns = [
    path('',views.homepage, name='index'),
    path('category',views.category, name='category'),
    path('subcategory',views.subcategory, name= 'subcategory'),
    path('quiz',views.quiz, name='quiz'),
    path('result',views.result, name='result'),
    path('api/', include(router.urls))
    
    
    
    
    ]
