from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity, get_jwt
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from dotenv import load_dotenv
from datetime import timedelta
from dto import ItemDto, UserDTO
import logging
import os

app = Flask(__name__)
#1: PENERAPAN CORS
CORS(app)

#2: PENERAPAN PENGAMANAN CONNECTION STRING KE DATABASE
load_dotenv() 
#print(os.getenv('DATABASE_URI'))
#Konfigurasi SQLAlchemy dengan menggunakan environtment variabel (agar aman)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#3: PENERAPAN LOGGING
logging.basicConfig(filename='app.log', level=logging.INFO)

#4: PENERAPAN RATE LIMITER
limiter = Limiter(
    app,
    key_func=get_remote_address,
    storage_uri="memory://"
)

#5: PENERAPAN JWT DENGAN REFRESH DAN REVOKE TOKEN
# Konfigurasi JWT untuk refresh dan revoke token:
app.config['JWT_SECRET_KEY'] = 'ihsanfati'
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
app.config['JWT_EXPRESS'] = timedelta(days=1)
jwt = JWTManager(app)
# Endpoint untuk mendapatkan token JWT
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    #6 PENERAPAN VALIDASI INPUT MENGGUNAKAN DATA TRANSFER OBJECT (DTO)
    user_dto = UserDTO(username=data.get('username'), password=data.get('password'))
    if not user_dto.username or not user_dto.password:
        return jsonify({'error': 'Missing username or password'}), 400

    # Gantilah dengan logika otentikasi yang sesuai dengan proyek Anda
    if user_dto.username == 'fati' and user_dto.password == 'jogja-istimewa':
        access_token = create_access_token(user_dto.username)
        # Menambahkan refresh token dalam respons
        refresh_token = create_refresh_token(user_dto.username)
        return jsonify(access_token=access_token, refresh_token=refresh_token), 200
    else:
        return jsonify({'error': 'Invalid username or password'}), 401
# Endpoint untuk mendapatkan refresh token
@app.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    new_access_token = create_access_token(identity=current_user)
    return jsonify(access_token=new_access_token), 200
# Endpoint yang memerlukan token JWT
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    # Tambahkan pengecekan apakah token telah direvoke
    jti = get_jwt()['jti']
    if jti in revoked_tokens:
        return jsonify({'error': 'Token has been revoked'}), 401
    return jsonify(logged_in_as=current_user), 200

# REVOKE TOKEN:
revoked_tokens = set()
@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    jti = jwt_payload['jti']
    return jti in revoked_tokens

@app.route('/revoke_token', methods=['DELETE'])
@jwt_required()
def revoke_token():
    jti = get_jwt_identity()
    revoked_tokens.add(jti)
    clear_revoked_tokens()  # Tambahkan ini
    return jsonify({'message': 'Token revoked successfully'}), 200

# Model untuk data API (ganti sesuai kebutuhan)
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

# Fungsi untuk menambahkan data dummy
def add_dummy_data():
    dummy_items = [
        {'name': 'Martabak Telor'},
        {'name': 'Beng-beng drink'},
        # Tambahkan item dummy lainnya sesuai kebutuhan
    ]

    for dummy_item in dummy_items:
        new_item = Item(name=dummy_item['name'])
        db.session.add(new_item)

    db.session.commit()

# Endpoint untuk mendapatkan daftar item
@app.route('/items', methods=['GET'])
@limiter.limit("5 per minute")  # 4: PENERAPAN RATE LIMITING
def get_items():
    items = Item.query.all()
    items_list = [{'id': item.id, 'name': item.name} for item in items]
    return jsonify(items_list)

# Endpoint untuk menambahkan item baru
@app.route('/items', methods=['POST'])
@limiter.limit("10 per day")  #4: PENERAPAN RATE LIMITING
@jwt_required()  # Memerlukan token JWT
def add_item():
    data = request.get_json()
    
    #6: PENERAPAN VALIDASI INPUT
    if 'name' not in data:
        return jsonify({'error': 'Missing name parameter'}), 400

    #7: PENERAPAN DATA TRANSFER OBJECT (DTO)
    item_dto = ItemDto(**data)
    new_item = Item(name=item_dto.name)
    db.session.add(new_item)
    db.session.commit()

    return jsonify({'message': 'Item added successfully'}), 201

@app.route('/reset_items', methods=['POST'])
def reset_items():
    # Hapus semua data pada tabel Item
    Item.query.delete()
    db.session.commit()

    # Tambahkan data dummy kembali
    add_dummy_data()

    return jsonify({'message': 'Items reset successfully'}), 200

# Tambahkan fungsi untuk membersihkan data token yang direvoke sebelumnya
def clear_revoked_tokens():
    global revoked_tokens
    revoked_tokens = set()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        add_dummy_data()
        clear_revoked_tokens()
    app.run(debug=True)