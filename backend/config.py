import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/agno_db")
SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")
DEBUG = os.getenv("DEBUG", "True").lower() == "true"
