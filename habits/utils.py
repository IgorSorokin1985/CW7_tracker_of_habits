from config.settings import TELEGRAM_BOT_API_KEY
import requests


telegram_token = TELEGRAM_BOT_API_KEY
send_message_url = f'https://api.telegram.org/bot{telegram_token}/sendMessage'


def send_telegram_message(habit):
    user = habit.user
    requests.post(
        url=send_message_url,
        data={
            'chat_id': user.telegram,
            'text': f'''Hello, {user.name}! Today at {habit.time} in {habit.place} you should
{habit.action} during {habit.duration_time}! Good luck'''
        })
