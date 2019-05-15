# Real Time Database

# Pre-requisite
- Python 3.6 or above
- RabbitMQ (message broker)

# Configure Celery
- Run the message broker
```bash
rabbitmq-server
```

- Using separate terminal window / tab, run the celery `worker` and `beat`
```bash
celery -A realtimedb worker -l info -B
```

# How to run the app
1. Configure and activate your virtual environment (e.g. using `virtualenvwrapper`)

2. Install all dependencies
```bash
pip install -r requirements.txt
```

3. Run migrations
```bash
python manage.py migrate
```

3. Run development server
```bash
python manage.py runserver
```

4. Seed `Temperature` data
```bash
python manage.py seed [number]
```
> The number argument is optional, by default it has a value of 5.

5. Visit http://localhost:8000/temperatures/list

6. The table will be updated every 10 seconds and recorded in the Last Modified column.

