import random
from django.core.management.base import BaseCommand, CommandParser
from recipies.models import User
from werkzeug.security import generate_password_hash



class Command(BaseCommand):
    help = "Create new user"
    
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('number', type=int, help='Количество тетсовых пользователей')
        
        
        
        
    def handle(self, *args, **kwargs):
        for i in range(kwargs.get('number')):
            user = User(username=f'name{i}n', 
                        
                        password=generate_password_hash(f'{random.choices(['e','w','W','1','@','&','6','m', 'd'], k=15)}'))
            user.save()
        