""" Database for Melon Tasting Reservation Scheduler app """

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# User class
class User (db.Model):
    """ User information """

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, nullable=False, unique=True)
    name = db.Column(db.String)

    reservations = db.relationship("Reservation", back_populates="user")

    def __repr__(self):
        """ Display user on the screen """

        return f"<User user_id={self.user_id} name={self.name}>"

# Reservation class
class Reservation(db.Model):
    """ Reservation information """

    __tablename__ = "reservations"

    reservation_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date, nullable=False)
    start = db.Column(db.Time, nullable=False)
    end = db.Column(db.Time, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    
    user = db.relationship("User", back_populates="reservations")
    

    def __repr__(self):
        """ Display a reservation on the screen """

        return f"<Reservation reservation_id={self.reservation_id} user_id={self.user_id} date={self.date} start={self.start}>"


# Connect to database
def connect_to_db(flask_app, db_uri="postgresql:///melon_reservations", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    connect_to_db(app)