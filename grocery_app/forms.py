from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, FloatField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL

from grocery_app.utils import FormEnum
from grocery_app.models import GroceryStore


class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""

    # TODO: Add the following fields to the form class:
    # - title - StringField
    # - address - StringField
    # - submit button
    title = StringField('Title')
    address = StringField('Address')
    sumbit = SubmitField()
    

class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""

    # TODO: Add the following fields to the form class:
    # - name - StringField
    # - price - FloatField
    # - category - SelectField (specify the 'choices' param)
    # - photo_url - StringField
    # - store - QuerySelectField (specify the `query_factory` param)
    # - submit button
    name = StringField('Name')
    price = FloatField('Price')
    category = SelectField('category', choices=['Produce', 'Deli', 'Bakery', 'Pantry', 'Frozen', 'Other'])
    photo_url = StringField('Image')
    store = QuerySelectField('Store', query_factory=lambda: GroceryStore.query)
    submit = SubmitField()