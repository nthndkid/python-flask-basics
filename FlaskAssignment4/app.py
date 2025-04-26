# I will teach you guys how to perform a phishing attack

# I added request in import to know the method requested by
# the client.
from flask import Flask, render_template, request

app = Flask(__name__)

# Here we need both GET and POST.
# We need GET so when the client open the endpoint
# The server will return a page.
# The POST request would be used for processing
# data coming from the client.
@app.route('/', methods=['GET', 'POST'])
def kunwariLogin():
    # Process info if POST
    if request.method == "POST":
        # This would be the user credentials when
        # the victim submits the info to the form.
        cred = request.form

        print(cred)

        # pass the cred to the template so we can render
        return render_template('victim.html', cred=cred)


    # We don't need else statement since we always
    # do a return statement inside POST. So this
    # statement catches request when not POST, like
    # when user's request is GET
    return render_template('phishing.html')
    
# Now it's your turn
# Challenge 1
# make an empty list data type called tasks
# make an endpoint named todo and use GET and POST
# name the function todo as well
# if request is POST, append the value (in the html,
# the key is `task`) in tasks
# render the html
# visit todo.html to see the html code
# tasks = []
# @app.route('/todo', methods=['GET', 'POST'])
# def todo():
#     if request.method == "POST":
#         ...

#     return render_template("todo.html", tasks=tasks)

   


if __name__ == "__main__":
    app.run(debug=True, port=5000)