from fastapi import FastAPI
from public.users import users_router

app = FastAPI()
app.include_router(users_router)

@app.get("/")
async def f_index():
    return "Hello! I'm Oplachko Vadim Romanovich, nice too meet you"
