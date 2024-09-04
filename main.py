from loader import greenAPI, app_log
from utils import send_message
from config import ADMIN_ID


def main():
    app_log.info("Starting...")
    app_log.info("Sending a greeting message...")
    send_message(greenAPI, ADMIN_ID, 'Starting the bot...\nBot successfully started!')
    app_log.info("Greeting message sent successfully!")


if __name__ == '__main__':
    main()

