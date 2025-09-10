from django.apps import AppConfig


class FootballappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
    
    ## Fixing dissalowed host bug
    a = 12 
