from .base import *  
import dj_database_url

DEBUG=False

ALLOWED_HOSTS =['djangoproject11.herokuapp.com']   

DATABASES = {
    'default':dj_database_url.parse(os.environ.get('DATABASE_URL'))

}