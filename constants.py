import os

from dotenv import load_dotenv

load_dotenv()

# váriaveis de ambiente
BASE_URL = os.getenv("BASE_URL")
KEY_API_GOOGLE = os.getenv("KEY_API_GOOGLE")
KEY_CX_ID_GOOGLE = os.getenv("KEY_CX_ID_GOOGLE")
PORT = os.getenv("PORT")
