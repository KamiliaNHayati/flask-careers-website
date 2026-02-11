from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') # if / be accessed will return 'Hello World!'
def index():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True) # when i change the code it will automatically reload
