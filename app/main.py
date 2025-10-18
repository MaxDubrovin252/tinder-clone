from fastapi import FastAPI
from core.models import db_helper
from contextlib import asynccontextmanager
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.session_dependency() as session:
        yield
        await db_helper.dispose()
        
        
app = FastAPI(lifespan=lifespan)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)