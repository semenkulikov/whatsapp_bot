from dotenv import find_dotenv, load_dotenv
import os

if not find_dotenv():
    exit("Не загружены необходимые переменные окружения!")
else:
    load_dotenv()

