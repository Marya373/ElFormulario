import random
from django.core.management.base import BaseCommand, CommandParser
from recipies.models import Recipies, User, Categories
from werkzeug.security import generate_password_hash
import time
import random

class Command(BaseCommand):
    help = "Create new recipe"
    
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('number', type=int, help='Количество тетсовых рецептов')
        
        
        
        
    def handle(self, *args, **kwargs):
        author_array = [i for i in User.objects.all()]
        category_array = [i for i in Categories.objects.all()]
        for i in range(kwargs.get('number')):
            recipe = Recipies(name=f'recipe{i}n', 
                        description=f'desc{i}',
                        steps=f'step1\nstep2\nstep3\n',
                        cooking_time=time.strftime('%H:%M', time.localtime(i * 100)),
                        author=random.choice(author_array),)
                        
            
            recipe.save()
        