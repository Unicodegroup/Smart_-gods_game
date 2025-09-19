from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Database
    sqlalchemy_database_url: str
    
    
    
    # Redis
    redis_url: str
    
    # Telegram Bot
    api_token: str   # <-- add this field so Alembic stops complaining

    class Config:
        env_file = ".env"   # make sure .env is in project root
        extra = "ignore"    # ignore any unrelated env vars
        case_sensitive = False 


settings = Settings()
