from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('q', '')
    category = request.args.get('category', 'laptops')
    
    # This will integrate with Cuelinks API once approved
    sample_products = [
        {
            'name': 'HP Pavilion Gaming Laptop',
            'price': '₹48,990',
            'rating': '4.2',
            'image': 'https://via.placeholder.com/300x200',
            'url': '#'
        },
        {
            'name': 'ASUS TUF Gaming F15',
            'price': '₹45,990',
            'rating': '4.3',
            'image': 'https://via.placeholder.com/300x200',
            'url': '#'
        }
    ]
    
    return render_template('search.html', products=sample_products, query=query)

@app.route('/api/products')
def api_products():
    # API endpoint for future Cuelinks integration
    return jsonify({
        'status': 'success',
        'message': 'API ready for Cuelinks integration',
        'products': []
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
