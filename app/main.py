from fastapi import FastAPI
from routes.user_routes import router as user_router
from routes.device_routes import router as device_router

app = FastAPI()

# Inclui as rotas
app.include_router(user_router)
app.include_router(device_router)

# Você pode adicionar eventos de startup/shutdown aqui se necessário
