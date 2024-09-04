from logging.handlers import RotatingFileHandler

from whatsapp_api_client_python import API
from config import ID_INSTANCE, API_TOKEN_INSTANCE
import logging

log_formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(funcName)s - %(message)s')
my_handler = RotatingFileHandler("bot.log", mode='a', maxBytes=5 * 1024 * 1024,
                                 backupCount=1, encoding="utf8", delay=0)
my_handler.setFormatter(log_formatter)
my_handler.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(log_formatter)
stream_handler.setLevel(logging.INFO)


app_log = logging.getLogger('bot_logger')
app_log.setLevel(logging.DEBUG)
app_log.addHandler(my_handler)
app_log.addHandler(stream_handler)

# Initialize the API client
greenAPI = API.GreenApi(ID_INSTANCE, API_TOKEN_INSTANCE)
