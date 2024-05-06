from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name
    
class Subcategory(models.Model):
    category = models.ForeignKey(Category, related_name='subcategory',on_delete=models.CASCADE)
    name  = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name
    
class Question(models.Model):
    subcategory = models.ForeignKey(Subcategory,related_name='questions',on_delete=models.CASCADE)
    difficulty = models.CharField(max_length=100)
    text = models.CharField(max_length=500)
    correct_answer = models.CharField(max_length=200)
    option_one = models.CharField(max_length=200)
    option_two = models.CharField(max_length=200)
    option_three = models.CharField(max_length=200)
    option_four = models.CharField(max_length=200)


    def __str__(self) -> str:
        return self.text



    