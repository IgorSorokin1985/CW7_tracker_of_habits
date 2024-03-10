# CW7_tracker_of_habits

## Description
This project is an API server for a service for tracking useful habits. The project provides endpoints for creating, 
changing, viewing and deleting useful habits, nice habits, and users. The project provides for sending 
messages via a telegram bot.

## Installation
Firstly install the project from GitHub and place it somewhere easily accessible from your driver, 
for example if your drive is named C:, then the location should be something like:
```
C:\TrackerHabits\
```
This should clone this project from Github:
```
git clone https://github.com/IgorSorokin1985/CW6_mailing_of_letters.git
```
Remember to go into the folder that the service is in. Then to install required libraries and frameworks 
run the commands:
```
pip install -r requirements.txt
```
When that is said and done, that should be it on the computer side, you should connect this service with Database.

## Environment variables
For working Tracker of Habits it is need create file ".env" with information about your email service and other. 
Example this file you can see as ".env.example".
For working message sending in Telegram you need Token of Telegram Bot.
```
DATABASE_NAME=
DATABASE_USER=
DATABASE_PASSWORD=
TELEGRAM_BOT_API_KEY=
REDIS_URL=
```

## Database connection
You should install PosgreSQL. 
```
https://www.postgresql.org/download/
```

Then create Database.
```
CREATE DATABASE name_database
```

Then you should make migrations with these commands
```
python manage.py makemigrations
```
If all is ok then
```
python manage.py migrate
```

## Celery
For right working Celery you need Redis. After downloadind Redis you can start worker. For this you should use command
```
celery -A config worker -l INFO
```

## Creating a superuser
For creating superuser you should use command
```
python manage.py csu
```

## Add test habits
For adding test habits you can use command
```
python manage.py add_test_habits
```

## Add telegram sending
For starting automatic sending messages in telegram you should use command.
```
python manage.py add_telegram_task_in_celery
```

## Documentation
All documentation about endpoints you can see by the link
```
http://localhost:8000/docs/
http://localhost:8000/redoc/
```
