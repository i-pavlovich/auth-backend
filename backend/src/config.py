from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    database_url: str

    model_config = SettingsConfigDict(env_file=(".env", ".env.prod"))


settings = Config()
