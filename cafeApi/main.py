from flask import Flask, jsonify, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import random as rd

app = Flask(__name__)

## Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


## Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.Float, nullable=True)

    def to_dict(self):
        # Loop through each column in the data record
        # Create a new dictionary entry;
        # where the key is the name of the column
        # and the value is the value of the column
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record
@app.route("/user/<int:cafe_id>")
def cafe_detail(cafe_id):
    cafe = db.get_or_404(Cafe, cafe_id)
    return jsonify(cafe=cafe.to_dict())


@app.route("/random")
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = rd.choice(cafes)
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/cafes", methods=["GET"])
def get_all_cafes():
    cafes = db.session.query(Cafe).all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])


@app.route("/search")
def get_cafe_by_loc():
    query_location = request.args.get("loc")
    cafes = db.session.query(Cafe).filter_by(location=query_location).all()
    if cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in cafes])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})


## HTTP POST - Create Record
@app.route("/cafes/create", methods=["POST"])
def add_cafe():
    if request.method == "POST":
        cafe = Cafe(
            name=request.form.get("name"),
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("loc"),
            has_sockets=bool(request.form.get("sockets")),
            has_toilet=bool(request.form.get("toilet")),
            has_wifi=bool(request.form.get("wifi")),
            can_take_calls=bool(request.form.get("calls")),
            seats=request.form.get("seats"),
            coffee_price=request.form.get("coffee_price"),
        )
        db.session.add(cafe)
        db.session.commit()
        return redirect(url_for("cafe_detail", id=cafe.id))
    return render_template("cafe/create.html")


## HTTP PUT/PATCH - Update Record
@app.route("/update/<int:cafe_id>")
def update_cafe(cafe_id):
    cafe = db.get_or_404(Cafe, cafe_id)
    key = request.args.get('key')
    value = request.args.get('value')
    setattr(cafe, key, value)
    db.session.commit()
    return jsonify(cafe=cafe.to_dict())


## HTTP DELETE - Delete Record
@app.route("/cafe/<int:cafe_id>/delete", methods=["GET", "POST"])
def user_delete(cafe_id):
    cafe = db.get_or_404(Cafe, cafe_id)

    if request.method == "POST":
        db.session.delete(cafe)
        db.session.commit()
        return redirect(url_for("get_all_cafes"))

    return render_template("cafe/delete.html", cafe=cafe)


if __name__ == '__main__':
    app.run(debug=True)
