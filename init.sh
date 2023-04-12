# Create the super user 'root'
python3 manage.py createsuperuser --noinput

# Database initialization - authentication
wget 127.0.0.1:8000/authentication/init

# Database initialization - quiz
wget 127.0.0.1:8000/quiz/question/init

# Database initialization - role
wget 127.0.0.1:8000/role/init
