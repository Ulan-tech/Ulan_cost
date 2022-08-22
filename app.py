from flask import Flask, render_template, url_for
from forms import CostForm

app = Flask(__name__)

posts = [
    {
        'material': 'maraging steel',
        'number_layers': '450',
        'product': 'bracket'
    },
    {
        'material': 'ti64',
        'number_layers': '400',
        'product': 'plate'
    }
]

@app.route('/')
def hello_world():  # put application's code here
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():  # put application's code here
    return render_template('about.html', title='about')

if __name__ == '__main__':
    app.run()

@app.route('/cost')
def cost():  # put application's code here
    form = CostForm()
    return render_template('cost.html', title='cost', form=form)


if __name__ == '__main__':
    app.run(debug=True)
