from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "FastAPI Server"
    MONGODB_URI: str = ""  # Mandatory in order to make .env work
    DATABASE_NAME: str = "fastapi-app"
    MAX_CONNECTIONS_COUNT: int = 10
    MIN_CONNECTIONS_COUNT: int = 10

    model_config = SettingsConfigDict(env_file=".env")


config = Settings()
