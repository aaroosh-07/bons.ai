from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    api_token: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()