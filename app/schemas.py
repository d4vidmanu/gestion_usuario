from pydantic import BaseModel
from typing import Optional, Literal
from datetime import date

# Esquema de Subscripción
class SubscriptionCreate(BaseModel):  # This is new
    subscription_type: str
    start_date: date
    end_date: date

class Subscription(BaseModel):
    id: int
    subscription_type: str
    start_date: date
    end_date: date
    user_id: int

    class Config:
        from_attributes = True  # Para la compatibilidad con SQLAlchemy

# Esquema de Usuario
class UserCreate(BaseModel):
    name: str
    email: str
    password: str  # Se incluye la contraseña directamente en el esquema de creación de usuario

class User(BaseModel):
    id: int
    name: str
    email: str
    subscription: Optional[Subscription] = None  # Relación opcional con subscripción

    class Config:
        from_attributes = True  # Para la compatibilidad con SQLAlchemy

# Esquema de creación de Reseña (ReviewCreate)
class ReviewCreate(BaseModel):
    rating: int
    created_at: date
    ride_id: int
    description: Literal['Excelente', 'Bien', 'Problemas']

# Esquema de Reseña (Review)
class Review(BaseModel):
    id: int
    rating: int
    created_at: date
    ride_id: int
    description: Literal['Excelente', 'Bien', 'Problemas']
    user_id: int  # Relación con usuario

    class Config:
        from_attributes = True  # Para la compatibilidad con SQLAlchemy

# Esquema de respuesta de Usuario (por ejemplo, en registros)
class UserIDResponse(BaseModel):
    id: int

    class Config:
        from_attributes = True  # Para la compatibilidad con SQLAlchemy
