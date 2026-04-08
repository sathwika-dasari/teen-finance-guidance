import os
from dotenv import load_dotenv

# Load variables from .env file (no-op if the file doesn't exist in production)
load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    if not SECRET_KEY:
        import warnings
        warnings.warn(
            "SECRET_KEY is not set. Using an insecure default — set it in your .env file.",
            stacklevel=2
        )
        SECRET_KEY = 'dev-key-please-change-in-production'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///../database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
