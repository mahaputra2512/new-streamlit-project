from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from dotenv import load_dotenv
import logging
import os

app = Flask(__name__)
#1: PENERAPAN CORS
CORS(app)

#2: PENERAPAN PENGAMANAN CONNECTION STRING KE DATABASE
load_dotenv() 
#Konfigurasi SQLAlchemy dengan menggunakan environtment variabel
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Konfigurasi JWT
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
jwt = JWTManager(app)

#2: PENERAPAN LOGGING
logging.basicConfig(filename='app.log', level=logging.INFO)

# Konfigurasi Rate Limiting
limiter = Limiter(
    app,
    key_func=get_remote_address,
    storage_uri="memory://"
)

# Model untuk data API (ganti sesuai kebutuhan)
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

# Fungsi untuk menambahkan data dummy
def add_dummy_data():
    dummy_items = [
        {'name': 'Martabak Pelor'},
        {'name': 'Beng-beng drink'},
        # Tambahkan item dummy lainnya sesuai kebutuhan
    ]

    for dummy_item in dummy_items:
        new_item = Item(name=dummy_item['name'])
        db.session.add(new_item)

    db.session.commit()

# Endpoint untuk mendapatkan daftar item
@app.route('/items', methods=['GET'])
@limiter.limit("5 per minute")  # 3: PENERAPAN RATE LIMITING
def get_items():
    items = Item.query.all()
    items_list = [{'id': item.id, 'name': item.name} for item in items]
    return jsonify(items_list)

# Endpoint untuk menambahkan item baru
@app.route('/items', methods=['POST'])
@limiter.limit("1 per day")  #3: PENERAPAN RATE LIMITING
@jwt_required()  # Memerlukan token JWT
def add_item():
    data = request.get_json()
    
    #4: VALIDASI INPUT
    if 'name' not in data:
        return jsonify({'error': 'Missing name parameter'}), 400

    new_item = Item(name=data['name'])
    db.session.add(new_item)
    db.session.commit()

    return jsonify({'message': 'Item added successfully'}), 201

# Endpoint untuk mendapatkan token JWT
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    #4 VALIDASI INPUT
    if 'username' not in data or 'password' not in data:
        return jsonify({'error': 'Missing username or password'}), 400

    # Gantilah dengan logika otentikasi yang sesuai dengan proyek Anda
    if data['username'] == 'example' and data['password'] == 'password':
        access_token = create_access_token(identity=data['username'])
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({'error': 'Invalid username or password'}), 401

# Endpoint yang memerlukan token JWT
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        add_dummy_data()
    app.run(debug=True)