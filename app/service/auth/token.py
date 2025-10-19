from authx import AuthX,AuthXConfig
from core.config import settings
config = AuthXConfig(
    JWT_SECRET_KEY=settings.auth.secret_key,   
    JWT_ALGORITHM=settings.auth.algorithm,
)


auth = AuthX(config=config) 