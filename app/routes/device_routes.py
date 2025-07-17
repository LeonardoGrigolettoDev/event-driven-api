# Rotas de dispositivo (exemplo para FastAPI)

from fastapi import APIRouter

router = APIRouter()

@router.post('/devices')
def register_device():
    # Lógica para registrar dispositivo
    pass
