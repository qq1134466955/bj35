from flask import current_app
from flask import render_template

from info.modules.index import index_blu

@index_blu.route('/')
def index():
    # redis_store['name'] = '小王'
    # session['name'] = '小花'
    # session['age'] = 15
    return  render_template('news/index.html')
