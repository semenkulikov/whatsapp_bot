from dotenv import find_dotenv, load_dotenv
import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

if not find_dotenv():
    exit("Не загружены необходимые переменные окружения!")
else:
    load_dotenv()


API_URL = os.getenv("API_URL")
MEDIA_URL = os.getenv("MEDIA_URL")
API_TOKEN_INSTANCE = os.getenv("API_TOKEN_INSTANCE")
ID_INSTANCE = os.getenv("ID_INSTANCE")

