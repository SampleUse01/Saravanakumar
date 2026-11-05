from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str = "PTMS"

    DATABASE_URL: str

    JWT_SECRET_KEY: str

    JWT_REFRESH_SECRET: str

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15

    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    class Config:
        env_file = ".env"


settings = Settings()