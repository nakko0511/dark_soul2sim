from fastapi import FastAPI
from routers import sim_routers


app = FastAPI(debug=True)
# app = FastAPI()


app.include_router(sim_routers.router)
