# restore trained data
import tensorflow as tf
import numpy as np

import sys
sys.path.append('imagenet')
import classify_image

# webapp
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/api/mnist', methods=['POST'])
def mnist():
    return jsonify({'task': {'aa':'aa'}}), 200

@app.route('/')
def main():
    return render_template('index.html')
