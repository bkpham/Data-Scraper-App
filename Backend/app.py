import subprocess
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///ammos.db'

db = SQLAlchemy(app)


class ProductResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    url = db.Column(db.String(255))
    price = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    quantity = db.Column(db.Integer)
    type = db.Column(db.Integer)

    def __init__(self, name, url, price, quantity, type):
        self.name = name
        self.url = url
        self.price = price
        self.quantity = quantity
        self.type = type


@app.route('/results', methods=['POST'])
def submit_results():
    results = request.json.get('data')
    id = request.json.get("id")
    update_time = datetime.now(timezone.utc)
    product = db.session.get(ProductResult, id)
    product.price = results['price']
    product.quantity = results['quantity']
    product.created_at = update_time
    product.type = results['type']
    db.session.commit()
    response = {'message': 'Received data successfully'}
    return jsonify(response), 200

@app.route('/add', methods=['POST'])
def add_it():
    results = request.json.get('data')
    product_result = ProductResult(
        name=results['name'],
        url=results['url'],
        price=results['price'],
        quantity=results['quantity'],
        type=results['type']
    )
    db.session.add(product_result)
    db.session.commit()
    response = {'message': 'Received data successfully'}
    return jsonify(response), 200


@app.route('/results')
def get_product_results():
    search_type = request.args.get('type')
    results = ProductResult.query.filter_by(type=search_type).order_by(
        ProductResult.created_at.desc()).all()
    product_results = []
    for result in results:
        url = result.url
        product_results.append( {
            'id': result.id,
            'name': result.name,
            'url': result.url,
            'price': result.price,
            "created_at": result.created_at,
            "quantity": result.quantity,
            "type": result.type
        })
    return jsonify(product_results)


@app.route('/all-results', methods=['GET'])
def get_results():
    results = ProductResult.query.all()
    product_results = []
    for result in results:
        product_results.append({
            'id': result.id,
            'name': result.name,
            'url': result.url,
            'price': result.price,
            "created_at": result.created_at,
            "quantity":result.quantity,
            "type":result.type
        })
    return jsonify(product_results)

@app.route('/start-scraper', methods=['POST'])
def start_scraper():
    url = request.json.get('url')
    id = request.json.get('id')
    # Run scraper asynchronously in a separate Python process
    command = f"python ./scraper/__init__.py {url} {id} /results"
    subprocess.Popen(command, shell=True)

    response = {'message': 'Scraper started successfully'}
    return jsonify(response), 200

@app.route('/add-scraper', methods=['POST'])
def add_scraper():
    url = request.json.get('url')
    # Run scraper asynchronously in a separate Python process
    command = f"python ./scraper/add.py {url} /add"
    subprocess.Popen(command, shell=True)

    response = {'message': 'Scraper started successfully'}
    return jsonify(response), 200

@app.route('/start-scrape-all', methods=['POST'])
def start_scrape_all():
    # Run scraper asynchronously in a separate Python process
    command = f"python ./scraper/scrape_all.py /scrape-all"
    subprocess.Popen(command, shell=True)
    response = {'message': 'Scraper started successfully'}
    return jsonify(response), 200

@app.route('/scrape-all', methods=['POST'])
def add_all_data():
    results = request.json.get('data')
    for product in results:
        product_result = ProductResult(
            name=product['name'],
            url=product['url'],
            price=product['price'],
            quantity=product['quantity'],
            type=product['type']
        )
        db.session.add(product_result)
        db.session.commit()
    response = {'message': 'Received data successfully'}
    return jsonify(response), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()