echo "Setting up database..."
dropdb {{ project_name }} --if-exists
createdb {{ project_name }}

echo "Running initial migrations..."
python manage.py migrate

echo "Adding development superuser..."
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell --plain
