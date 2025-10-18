from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker
from core.config import settings
class DataBaseHelper:
    def __init__(self, db_url:str,echo:bool,max_overflow:int):
        self.engine = create_async_engine(db_url,echo=echo,max_overflow=max_overflow)
        
        self.session_factory = async_sessionmaker(
            bind=self.engine, 
            autocommit=False,
            autoflush=False, 
            expire_on_commit=False
            )
        
    async def dispose(self):
        await self.engine.dispose()
        
    async def session_dependency(self):
        async with self.session_factory() as session:
            yield session
            
            

db_helper = DataBaseHelper(db_url=settings.db.url,echo=settings.db.echo,max_overflow=settings.db.max_overflow)