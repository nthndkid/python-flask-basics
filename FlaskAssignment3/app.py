# Import flask dependencies
from flask import Flask, render_template

# Initialize the Flask app
app = Flask(__name__)

# The route method accepts a string as a parameter. 
# This is the endpoint for the function below the @
# The @ is a special symbol called a decorator that wraps the function.
@app.route('/')
def home():
    # The render_template method is when you want to use HTML 
    # with jinja syntax.
    # Before using this, make sure that the html you want to render is
    # in the /templates/ folder.
    # Open /templates for this directory to learn more.
    return render_template('index.html')

# By default, the method is GET.
# You can pass in a list data type for the methods parameter to 
# specify the method
@app.route('/demonMode', methods=['GET'])
def demon():
    # Since the endpoint used for this function is `/demonMode`,
    # The location where we can access this page is in 
    # `http://localhost:5000/demonMode`
    return "Demon Mode on 😈"

# !!! Challenge 1: render html angelMode
# 1. specify endpoint in app.route
# 2. name the function angel()
# 3. render the html
@app.route('/angelMode', methods=['GET'])
def angel():
    return render_template('angel.html')

# !!! Challenge 2: render html frog
# 1. specify endpoint in app.route
# 2. name the function frog()
# 3. render the html passing a parameter
# 4. look for frog.html in /templates
# 5. try changing the count value
@app.route('/frogMode', methods=['GET'])
def frog():
    count = 15
    return render_template('frog.html', frogCount=count)

# !!! Challenge 3: render html elon
# 1. specify endpoint in app.route
# 2. name the function elon()
# 3. render the html passing a parameter
# 4. look for elon.html in /templates
# 5. try changing really to 2
# 6. try changing really to 3
@app.route('/elonMode', methods=['GET'])
def ____():
    # really = 1
    # really = 2
    really = 3
    return render_template('elon.html', romanSalute=really)

# !!! Challenge 4: render html wishlist
# 1. specify endpoint in app.route
# 2. name the function wishlist()
# 3. render the html passing a parameter
# 4. look for wishlist.html in /templates
# 5. try adding other string in the wishlist list data type
@app.route('/wishlist', methods=['GET'])
def wishlist():
    wishlist = ['iphone', 'mac', 'macbook', 'legion', 'predator', 'ps5']
    return render_template('wishlist.html', hilingKo=wishlist)

# This ensures that the script is being run directly (not imported as a module).
# When a Python file is executed, __name__ is set to "__main__".
# If the script is imported elsewhere, this block will not execute.
if __name__ == "__main__":
    # app.run() starts the Flask development server.
    # debug=True enables debug mode:
        # Automatically restarts the server on code changes.
        # Provides an interactive debugger for errors.
    # port=5000 specifies that the server should run on port 5000 (default for Flask).
    app.run(debug=True, port=5000)