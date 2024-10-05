import os
from dotenv import load_dotenv

environment = os.getenv('FLASK_ENV')

if environment == 'local':
    load_dotenv(dotenv_path='.env.local')
elif environment == 'test':
    load_dotenv(dotenv_path='.env.test')
else:
    load_dotenv(dotenv_path='.env')

class Config:
    ENVIRONMENT = environment
    APP_NAME=os.getenv('APP_NAME')
    CONTAINER_STORAGE=os.getenv('CONTAINER_STORAGE')
    CONNECTION_STRING_STORAGE=os.getenv('CONNECTION_STRING_STORAGE')