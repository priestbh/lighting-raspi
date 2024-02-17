#!/usr/bin/env python
# encoding: utf-8
import time
import board
import neopixel
import json
from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/')
def index():
    return jsonify({'name': 'lighting',
                    'strip': 'LEDs'})

app.run()