from flask import Flask, render_template, request
app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_world():  # put application's code here
    return render_template('home.html')

@app.route('/')
def home():  # put application's code here
    return render_template('dropdown.html')

if __name__ == "__main__":
    app.run()


@app.route('/about')
def about():  # put application's code here
    return render_template('about.html', title='about')

if __name__ == '__main__':
    app.run()
