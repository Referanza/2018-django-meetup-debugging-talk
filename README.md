# 2018-django-meetup-debugging-talk
Code for the presentation on debugging at the Django meetup in Stockholm
2018-02-07.

# Install
createuser --interactive --superuser --pwprompt django_project
createdb -Odjango_project django_project
python manage.py migrate
python manage.py createsuperuser
