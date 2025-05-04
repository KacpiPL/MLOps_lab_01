# settings.py
from pydantic_settings import BaseSettings
from pydantic import field_validator
from pydantic import ConfigDict


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str
    FAKE_API_KEY: str

    model_config = ConfigDict(env_file=".env")

    @field_validator("ENVIRONMENT")
    @classmethod
    def validate_environment(cls, value: str) -> str:
        allowed = {"dev", "test", "prod"}
        if value.lower() not in allowed:
            raise ValueError(f"ENVIRONMENT must be one of: {', '.join(allowed)}")
        return value.lower()

    # class Config:
    #     env_file = ".env"
