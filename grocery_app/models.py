from sqlalchemy_utils import URLType

from grocery_app.extensions import db
from grocery_app.utils import FormEnum

from flask_login import UserMixin

class ItemCategory(FormEnum):
    """Categories of grocery items."""
    PRODUCE = 'Produce'
    DELI = 'Deli'
    BAKERY = 'Bakery'
    PANTRY = 'Pantry'
    FROZEN = 'Frozen'
    OTHER = 'Other'

class GroceryStore(db.Model):
    """Grocery Store model."""
    __tablename__ = 'GroceryStore'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    items = db.relationship('GroceryItem', back_populates='store')
    
    created_by_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    created_by = db.relationship('User')
    
class GroceryItem(db.Model):
    """Grocery Item model."""
    __tablename__ = 'GroceryItem'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    category = db.Column(db.Enum(ItemCategory), default=ItemCategory.OTHER)
    photo_url = db.Column(URLType)
    store_id = db.Column(
        db.Integer, db.ForeignKey('GroceryStore.id'), nullable=False)
    store = db.relationship('GroceryStore', back_populates='items')
    
    created_by_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    created_by = db.relationship('User')    
    
    carts = db.relationship('User', secondary='shopping_list_items', back_populates='shopping_list_items')
    
class User(db.Model, UserMixin):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())
    
    shopping_list_items = db.relationship('GroceryItem', secondary='shopping_list_items', back_populates='carts')
    
shopping_list_table = db.Table('shopping_list_items', 
    db.Column('user', db.Integer, db.ForeignKey('User.id')), 
    db.Column('item', db.Integer, db.ForeignKey('GroceryItem.id')),
)
