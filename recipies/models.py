from django.db import models
from django.contrib.auth.models import User # https://docs.djangoproject.com/en/4.2/ref/contrib/auth/
# Create your models here.

# class User(User):
    
    
#     def __str__(self) -> str:
#         return self.username
    
    

class Categories(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name


class Recipies(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    steps = models.TextField()
    cooking_time = models.TimeField()
    image = models.ImageField(upload_to='recipies/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Categories, through='CategoryRecipe')
    
    def __str__(self) -> str:
        return  "\n".join([self.name,
                          self.description,
                        str(self.cooking_time)],
                          )
    


class CategoryRecipe(models.Model):
    recipe = models.ForeignKey(Recipies, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
