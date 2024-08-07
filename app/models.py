from sqlalchemy import Boolean, Column, Integer, String, VARCHAR, TIMESTAMP, ForeignKey, JSON
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id= Column(String(36), primary_key=True,index=True)
    sso_id = Column(String(36))
    userName = Column(String(50))
    email=Column(String(50))
    picture = Column(VARCHAR(512) )
    sso_type = Column(String(30))
    created_at = Column(TIMESTAMP) 

    # Relationship with Theme
    themes = relationship("Theme", back_populates="user")


class Theme(Base):
    __tablename__ = "themes"
    
    id= Column(String(36), primary_key=True,index=True)
    user_id = String(36)
    portfolio_name = VARCHAR(30)
    created_at = TIMESTAMP 
    user_id = Column(String(36), ForeignKey("users.id"))
    data = JSON

    # Relationship with User
    user = relationship("User", back_populates="themes")