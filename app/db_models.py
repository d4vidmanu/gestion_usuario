from sqlalchemy import Column, Integer, String, ForeignKey, Date, Enum
from sqlalchemy.orm import relationship
from .database import Base
from datetime import date, timedelta


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    subscription = relationship("Subscription", uselist=False, back_populates="user")
    reviews = relationship("Review", back_populates="user")


class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    subscription_type = Column(String, nullable=False)
    start_date = Column(Date, default=date.today)
    end_date = Column(Date)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="subscription")

    def set_end_date(self):
        if self.subscription_type == "1":
            self.end_date = self.start_date + timedelta(days=30)
        elif self.subscription_type == "2":
            self.end_date = self.start_date + timedelta(days=60)
        elif self.subscription_type == "3":
            self.end_date = self.start_date + timedelta(days=90)


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    rating = Column(Integer)
    created_at = Column(Date, default=date.today)
    ride_id = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'))

    # Aquí simplificamos el enum
    description = Column(Enum('Excelente', 'Bien', 'Problemas', name="review_description_enum"), nullable=False)

    user = relationship("User", back_populates="reviews")
