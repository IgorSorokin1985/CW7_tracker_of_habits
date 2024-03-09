from config.settings import TELEGRAM_BOT_API_KEY
import requests


telegram_token = TELEGRAM_BOT_API_KEY
send_message_url = f'https://api.telegram.org/bot{telegram_token}/sendMessage'


def send_telegram_message(habit):
    """Function for sending message in Telegram"""
    user = habit.user
    message = create_message(habit, user)
    requests.post(
        url=send_message_url,
        data={
            'chat_id': user.telegram,
            'text': message
        })


def create_message(habit, user):
    """Function for creating message"""
    if habit.reward:
        reward_text = f"After this you can get {habit.reward}!"
    else:
        reward_text = f"After this you can {habit.associated_nice_habit.action}!"
    result = f"Hello, {user.name}! Today at {habit.time} in {habit.place} you should {habit.action} " \
             f"during {habit.duration_time}! {reward_text} Good luck!!!"
    return result
