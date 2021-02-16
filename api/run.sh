# convenience script to make migrations, apply migrations to DB and run server
python3 manage.py makemigrations assessments resources
python3 manage.py migrate
python3 manage.py runserver 