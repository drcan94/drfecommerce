## generating a new secret key
#### > python manage.py shell
#### > from django.core.management.utils import get_random_secret_key
#### > print(get_random_secret_key())