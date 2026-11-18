
import os
from dotenv import load_dotenv

# Load environment variables from project root
BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../")
)

ENV_FILE = os.path.join(BASE_DIR, ".env")

load_dotenv(ENV_FILE)


class Settings:
    PROJECT_NAME: str = "NexusOne AI"
    PROJECT_VERSION: str = "1.0.0"
    API_V1_PREFIX: str = "/api/v1"

    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: int = int(os.getenv("DB_PORT", "5432"))
    DB_NAME: str = os.getenv("DB_NAME", "nexusone_db")
    DB_USER: str = os.getenv("DB_USER", "postgres")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "")


settings = Settings()
