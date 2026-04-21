from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.user import User
from schemas.user import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["users"])

#response_model -> diz ao FastAPI qual schema usar para formatar a resposta
@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    #user: UserCreate -> o FastAPI lê o corpo da requisição
    #  e valida com o schema UserCreate automaticamente

    #db: Session = Depends(get_db) -> injeção de dependência.
    #O FastAPI chama o get_db, abre a sessão, excuta ações e fecha
    # no final da função

    user_exist = db.query(User).filter(User.email == user.email).first()
    if user_exist:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_user = User(
        username=user.username,
        email=user.email,
        password=user.password,
        is_author=user.is_author
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)#Atualiza o objeto em memória. Sem ele, o id ainda seria None
    return new_user

@router.get("/", response_model=list[UserResponse])
def list_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.get("/{user_id}", response_model=UserResponse)
def fetch_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{user_id}")
def del_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}