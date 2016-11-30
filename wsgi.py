# -*- coding: utf-8 -*-

from flask import Flask
application = Flask(__name__)

import redis
rdb = redis.Redis('redis')
#rdb.set("counter", 0)

@application.route('/', methods=['GET'])
def index():
    rdb.incr("counter")
    counter = rdb.get("counter")
    
    return 'Counter: {}\n'.format(counter)


if __name__ == '__main__':
    application.run(debug=True)
