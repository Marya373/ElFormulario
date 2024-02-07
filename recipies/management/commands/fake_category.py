import random
from django.core.management.base import BaseCommand, CommandParser
from recipies.models import Categories
from werkzeug.security import generate_password_hash



class Command(BaseCommand):
    help = "Create new category"
    
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('number', type=int, help='Количество тетсовых категорий')
        
        
        
        
    def handle(self, *args, **kwargs):
        for i in range(kwargs.get('number')):
            category = Categories(name=f'category{i}', 
                        
                        )
            category.save()
        