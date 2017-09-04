from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# To add var to URL,
# specify a rule with <type:var_name>
# type ==> can be (int, string or path)
@app.route('/restaurants/<int:restaurant_id>/')
# make a new route for my menue app
# by using the restaurant_id to specify 
# which menu I want to see
# in /<int:restaurant_id>/')
# the slash in the end (the trailing slash)
# Flask will render the page even 
# when it's not there in the URL
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    # filter_by to filter results to restaurant_id
    # .one() requires that there is only one result in the result set;
    # it is an error if the database returns 0 or 2 or more results and an exception will be raised.
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
    output = ''
    for i in items:
        output += i.name
        output += '</br>'
        output += i.price
        output += '</br>'
        output += i.description
        output += '</br>'
        output += '</br>'
    return output

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
