from sqlalchemy.orm import Session
from . import db_models as models
from . import schemas
from datetime import date

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_subscription(db: Session, subscription: schemas.SubscriptionCreate, user_id: int):
    db_subscription = models.Subscription(**subscription.dict(), user_id=user_id)
    db_subscription.set_end_date()  # Establece la fecha de fin automáticamente según el tipo
    db.add(db_subscription)
    db.commit()
    db.refresh(db_subscription)
    return db_subscription

def delete_expired_subscription(db: Session, user_id: int):
    today = date.today()
    db_subscription = db.query(models.Subscription).filter(models.Subscription.user_id == user_id).first()

    # Verificar si la suscripción está caducada
    if db_subscription and db_subscription.end_date <= today:
        db.delete(db_subscription)
        db.commit()
        return None  # Si la suscripción ha caducado, retornamos None
    return db_subscription

def get_user_subscription(db: Session, user_id: int):
    return delete_expired_subscription(db, user_id)  # Verificamos si está caducada y la eliminamos


def create_review(db: Session, review: schemas.ReviewCreate, user_id: int):
    db_review = models.Review(**review.dict(), user_id=user_id)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

def get_review(db: Session, review_id: int):
    return db.query(models.Review).filter(models.Review.id == review_id).first()


