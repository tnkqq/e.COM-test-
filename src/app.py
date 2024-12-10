from contextlib import asynccontextmanager

from fastapi import FastAPI

from routers.forms_router import router as forms_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # bf start
    yield
    # af stop


app = FastAPI(lifespan=lifespan)

app.include_router(forms_router)
