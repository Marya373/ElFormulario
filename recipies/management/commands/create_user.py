from django.core.management.base import BaseCommand, CommandParser
from recipies.models import User
from werkzeug.security import generate_password_hash



class Command(BaseCommand):
    help = "Create new user"
    
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('name', type=str, help='Имя пользователя')
        
        parser.add_argument('pswd', type=str, help='Пароль пользователя')
        
        
        
    def handle(self, *args, **kwargs):
        user = User(username=kwargs.get('name'), 
                    
                    password=kwargs.get('pswd'))
        user.save()
        self.stdout.write(f'{user}')