from fastapi import FastAPI
from Portfolio.api.portfolio import portfolio_router


app = FastAPI()


# routers

app.include_router(portfolio_router)