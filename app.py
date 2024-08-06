from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Transaction, Category

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_transaction', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':
        # Handle form submission
        pass
    return render_template('add_transaction.html')

@app.route('/view_transactions')
def view_transactions():
    transactions = Transaction.query.all()
    return render_template('view_transactions.html', transactions=transactions)

@app.route('/budget')
def budget():
    # Handle budget logic
    return render_template('budget.html')

if __name__ == '__main__':
    app.run(debug=True)
