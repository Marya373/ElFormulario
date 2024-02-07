from django.core.management.base import BaseCommand, CommandParser
from recipies.models import Recipies, Categories
from datetime import time

class Command(BaseCommand):
    help = "Create new recipe"
    
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('name', type=str, help='Recipe name')
        parser.add_argument('description', type=str, help='Recipe description')
        parser.add_argument('steps', type=str, help='Steps of cooking')
        parser.add_argument('time', type=time, help='Cooking time')
        parser.add_argument('author', type=int, help='Author of recipe')
        parser.add_argument('category', type=str, help='Recipe category')
        
    def handle(self, *args, **kwargs):
        caregory = Categories.objects.filter(name=kwargs.get('name'))
        recipe = Recipies(name=kwargs.get('name'),
                          description=kwargs.get('description'),
                          steps=kwargs.get('steps'),
                          time=kwargs.get('time'),
                          author=kwargs.get('author'),
                          category=caregory)
        recipe.save()
        self.stdout.write(f"{recipe}")