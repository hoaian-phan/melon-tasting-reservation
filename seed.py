""" Script to seed database """

import os
import json
from random import choice, sample, choices
from datetime import datetime, date, timedelta

import crud
import model
import server

os.system("dropdb melon_reservations")
os.system("createdb melon_reservations")

model.connect_to_db(server.app)
model.db.create_all()

# Create seed users
with open("data/users.json") as f:
    user_data = json.loads(f.read())

for user in user_data:
    name = user["name"]
    email = user["email"]

    user_in_db = crud.create_user(name, email)
    model.db.session.add(user_in_db)

model.db.session.commit()
    