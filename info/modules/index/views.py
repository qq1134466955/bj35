from info.modules.index import index_blu
from info import redis_store
@index_blu.route('/')
def index():
    # redis_store['name'] = '小王'
    # session['name'] = '小花'
    # session['age'] = 15
    return 'hello world'