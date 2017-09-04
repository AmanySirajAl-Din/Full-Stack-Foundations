# this the minimum flask app
# first, import Flask class
from flask import Flask
# next, create an instance of Flask class
# with the name of the running app __name__
app = Flask(__name__)


@app.route('/')  # the decorator
@app.route('/hello')
def HelloWorld():
    return "Hello World"

if __name__ == '__main__':  
# makes sure the server only runs if the script is
# excuted directly from the Python interpreter
# and not used as imported moudule
    app.debug = True
    # Flask take care of,
    # restarting our server each time
    # we made a modification to our code
    # with app.debug = True,
    # the server will reload itself each time
    # the code changes
    # and provide a helpful debug in the browser
    app.run(host='0.0.0.0', port=5000)
    # to run the local server with our app
    # '0.0.0.0' this tells the web server to
    # listen to all public IP addresses