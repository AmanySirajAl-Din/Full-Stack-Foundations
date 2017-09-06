# To get data from a form,
# I'll import request from flask package

# To redirect the user back to the main user page,
# I'll import redirect from flask package

from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
    return render_template('menu.html', restaurant=restaurant, items=items)

# Task 1: Create route for newMenuItem function here


@app.route('/restaurant/<int:restaurant_id>/new/', methods=['GET', 'POST'])
# methods=['GET', 'POST'] to responds to GET & POST requests
# Now, that I can respond to POST requests,
# I can make forms for creating & updating MenuItems
def newMenuItem(restaurant_id):
    if request.method == 'POST':
    # if statment that looks for POST request
        newItem = MenuItem(name=request.form['name'],
            restaurant_id=restaurant_id)
        # request.form['name'] ==> 
        # extract the name field from my form
        session.add(newItem)
        session.commit()
        # After creating my newItem,
        # Added to my session and 
        # commit the session to the DB
        
        # To redirect the user back to the main user page
        # use redirect fun.
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:  # to handle the GET request
    # if my server didn't receive a POST request,
        return render_template('newmenuitem.html', restaurant_id=restaurant_id)
        # it'll render the template, for newmenuitem.html

# Task 2: Create route for editMenuItem function here


@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/edit/')
def editMenuItem(restaurant_id, menu_id):
    return "page to edit a menu item. Task 2 complete!"

# Task 3: Create a route for deleteMenuItem function here


@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/delete/')
def deleteMenuItem(restaurant_id, menu_id):
    return "page to delete a menu item. Task 3 complete!"


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
