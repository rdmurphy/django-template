# /bin/sh

echo "Wiping out all migrations..."
find {{ project_name }} -type f -path "*/migrations/00*.py" ! -path "*/contrib/*" -delete -print

echo "Making new migrations..."
python manage.py makemigrations

echo "Resetting database..."
dropdb {{ project_name }} --if-exists
createdb {{ project_name }}

echo "Migrating..."
python manage.py migrate

echo "Adding superuser..."
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell --plain
