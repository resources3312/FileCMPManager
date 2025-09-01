from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    REDIS_HOST: str = getenv("REDIS_HOST")
    REDIS_PORT: str = getenv("REDIS_PORT")
    REQUEST_COUNT: int = int(getenv("REQUEST_COUNT"))



