from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "mysql://root:root@localhost:3306/baseVC"

    class Config:
        env_file = ".env"

Settings = Settings()