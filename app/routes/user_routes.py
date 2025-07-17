# Rotas de usuário (exemplo para FastAPI)

from fastapi import APIRouter

router = APIRouter()

@router.post('/users')
def create_user():
    # Lógica para criar usuário
    pass
