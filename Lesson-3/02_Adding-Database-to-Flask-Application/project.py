from flask import Flask
# bring our CRUD functionality into my app
# 1- import the code for SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
app = Flask(__name__)

# 2- And the DB engine in sissionmaker like lesson 1&2
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/hello')
def HelloWorld():
    # 3- change my HelloWorld fun
    restaurant = session.query(Restaurant).first()
    # query to grap the 1st restaurant
    # out of my DB
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
    # list out all of the menu items
    output = ''
    for i in items:
        output += i.name
        output += '</br>'  
        # add it to make my output easier to read
    return output  # return it so that my user sees it from the browser
    # and stored in a string called output

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
