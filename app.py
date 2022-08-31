from flask import Flask, render_template
from forms import CostForm
app = Flask(__name__)
app.debug = True

@app.route('/')
def home():  # put application's code here
    return render_template('home.html')

@app.route('/')
def home_cost():
    form = CostForm()
    return render_template('cost.html', title='Input information', form=form)


@app.route('/about')
def about():  # put application's code here
    return render_template('about.html', title='about')

if __name__ == '__main__':
    app.run()
