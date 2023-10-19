# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Apply database migrations
python3.9 manage.py migrate

# Collect static files
python3.9 manage.py collectstatic --noinput

# Create a superuser
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='flm').exists() or User.objects.create_superuser('flm', 'admin@example.com', 'fiangonana')" | python3.9 manage.py shell
