find . -name "*.pyc" -exec rm {} \;
rm db.sqlite3

python manage.py makemigrations book
python manage.py makemigrations users
python manage.py makemigrations discourse
python manage.py migrate

# python manage.py create_test_data