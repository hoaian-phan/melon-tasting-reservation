""" CRUD operations """

from model import (db, connect_to_db, User, Appointment, Reservation) 
from datetime import date

# Log in
def get_user_by_email(email):
    """ Return the user object by email """

    user = User.query.filter_by(email=email).first()

    return user

# Create users for seed.py
def create_user(name, email):
    """ Create and return a user """

    user = User(name=name, email=email)

    return user