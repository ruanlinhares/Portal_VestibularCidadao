from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "mysql://root:root@localhost:3306/baseVC"
    google_api_key: str

    class Config:
        env_file = ".env"

settings = Settings()