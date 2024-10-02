from pydantic import BaseModel
from typing import Optional, List
from datetime import date


class SubscriptionBase(BaseModel):
    subscription_type: str
    start_date: date
    end_date: date


class SubscriptionCreate(SubscriptionBase):
    pass


class Subscription(SubscriptionBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True  # Cambiado de orm_mode a from_attributes


class UserBase(BaseModel):
    name: str
    email: str


class UserCreate(UserBase):
    password: str


class User(BaseModel):
    id: int
    name: str
    email: str
    subscription: Optional[Subscription] = None

    class Config:
        from_attributes = True  # Cambiado de orm_mode a from_attributes


class ReviewBase(BaseModel):
    rating: int
    created_at: date
    ride_id: int


class ReviewCreate(ReviewBase):
    pass


class Review(ReviewBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True  # Cambiado de orm_mode a from_attributes
