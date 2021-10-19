# In this code, I will set up my flask app, defined by application.py (which would be my server). I will define
# functions in this script that determines what happens
# if I access certain API end points (using my web browser/client)


from flask import request, Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__) # set up flask app

# set up database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' # find all these in flask documentation
db = SQLAlchemy(app)


@app.route('/') # define endpoint
def index(): # define a method that is executed whenever someone visit this endpoint (home page)
    return 'Hello!'

# Next create a few environment variables in your terminal

# export FLASK_APP = application.py
# export FLASK_ENV=development
# flask run
# open the website from the output link
# I get "Hello!" on the webpage  (This indicates I have my app ready to go)

# create a relational database to be used with sql alchemy
class Drink (db.Model):
    # attributes
    id = db.Column(db.Integer,primary_key=True) # create column callled id that contains integer. It is the primary key
    name = db.Column(db.String(80), unique=True, nullable=False) # can't have nulls, unique values only, string with 80 chars
    description = db.Column(db.String(120)) # strings with 120 chars

    # methods
    def __repr__(self): # whenever I call object, these strings will be return
        return f"{self.name} - {self.description}"





@app.route('/drinks') # endpoint: home page/drinks
def get_drinks():
    drinks = Drink.query.all()
    output = []
    for drink in drinks: # drink is not "JSON serializable, so below is a workaround"-- I create a list of dicts, each dict is a drink
        drink_data = {'name': drink.name, 'description': drink.description}
        output.append(drink_data)
    return{"drinks":output} # wrap the list of dicts with a dict, where the key to the list of dict is "drinks"
    #return {"drinks":"drink data"}

# Save it and then the app will get updated automatically
# Enter http://127.0.0.1:5000/drinks on the web browser
# I get:
#{
#  "drinks": "drink data"
#}

@app.route('/drinks/<id>') # individual drink
def get_drink(id):
    drink= Drink.query.get_or_404(id) # get drink object
    return {"name": drink.name,"description":drink.description} # dicts are jsonifiable, otherwise use the jsonify() function

# Adding a new drink (I will use POSTMAN to do that), we define in the body of our request what our drink is (json format data)
@app.route('/drinks', methods=['POST']) # the deault for the methods argument is GET, I now use POST because I am defining a POST request
def add_drink():
    drink = Drink(name=request.json['name'], description=request.json['description']) # create a new drink, request.json allow us to access the data that was sent
    db.session.add(drink)
    db.session.commit()
    return {'id':drink.id}