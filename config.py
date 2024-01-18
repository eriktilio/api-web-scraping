import os

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.


class Config(object):
    # API_ variables
    API_NAME = os.environ.get("API_NAME")
    API_VERSION = os.environ.get("API_VERSION")
    API_DESC = os.environ.get("API_DESC")
    PORT = os.environ.get("PORT")
