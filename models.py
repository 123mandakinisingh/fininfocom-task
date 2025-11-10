from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date, Enum
from sqlalchemy.orm import relationship
from database import Base

class MenuName(Base):
    __tablename__ = "menu_names"
    menu_id = Column(Integer, primary_key=True)
    menu_name = Column(String(50))

class Category(Base):
    __tablename__ = "categories"
    cat_id = Column(Integer, primary_key=True)
    category_name = Column(String(50))
    menu_id = Column(Integer, ForeignKey("menu_names.menu_id"))
    menu = relationship("MenuName")

class Menu(Base):
    __tablename__ = "menu"
    item_id = Column(Integer, primary_key=True)
    item_name = Column(String(50))
    cat_id = Column(Integer, ForeignKey("categories.cat_id"))
    menu_id = Column(Integer, ForeignKey("menu_names.menu_id"))
    size = Column(String(100), nullable=True)
    price = Column(String(100), nullable=True)
    category = relationship("Category")
    menu = relationship("MenuName")

class OrderHistory(Base):
    __tablename__ = "order_history"
    id = Column(Integer, primary_key=True)
    order_date = Column(String(50))
    order_id = Column(Integer)
    item_id = Column(Integer, ForeignKey("menu.item_id"))
    size = Column(String(50), nullable=True)
    price = Column(Float)
    qty = Column(Integer)
    order_status = Column(String(50))
    total = Column(Float)
    item = relationship("Menu")

class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True)
    payment_date = Column(String(50))
    payment_id = Column(Integer)
    order_id = Column(Integer)
    amount_due = Column(Float)
    tips = Column(Float)
    discount = Column(Float)
    total_paid = Column(Float)
    payment_type = Column(String(50))
    payment_status = Column(String(50))
