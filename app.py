from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy 

from controllers.designer_controller import designer_blueprint
from controllers.product_controller import product_blueprint

import repositories.product_repository as product_repository
import repositories.designer_repository as designer_repository

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Nazar123@localhost:5432/jewellery_shop'
app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle+cx_oracle://postgres:Nazar123@localhost:1521/?service_name=jewellery_shop'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app) 

app.register_blueprint(designer_blueprint)
app.register_blueprint(product_blueprint)


@app.route('/', methods=['GET', 'POST'])
def home():
    return redirect('/products') 

if __name__ == '__main__':
    app.run(debug=True)