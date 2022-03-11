import os

from flask import Flask, redirect, render_template, request, url_for
from flask_migrate import Migrate

from models import db, AuthType, Datasources
import service


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql+psycopg2://postgres:{os.getenv('PSQL_PW')}@localhost/test_task2"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    auth_type = AuthType.query.all()
    datasources = Datasources.query.all()
    return render_template('index.html', auth_type=auth_type, datasources=datasources)

@app.route('/insert', methods=('GET', 'POST'))
def insert():
    if request.method == "POST":
        try:
            service.insert(request)
            return redirect(url_for('insert'))
        except:
            return "Error, check fields!"
    else:
        return render_template('insert.html')

@app.route('/update/<uuid:guid>', methods=('GET', 'POST'))
def update(guid):
    if request.method == 'POST':
        try:
            service.update(request, guid)
            return redirect(url_for('update', guid=guid))
        except:
            return 'Error'
    else:
        datasources = Datasources.query.get(guid)
        auth_type = AuthType.query.get(datasources.ref_auth_type).enumname
        return render_template('update.html', datasources=datasources, auth_type=auth_type)

@app.route('/delete/<uuid:guid>', methods=('GET', 'POST'))
def delete(guid):
    try:
        service.delete(guid)
        return 'Deleted!'
    except:
        return 'Error'