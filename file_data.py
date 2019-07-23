

from flask import Flask
app = Flask(__name__)

import json
import redis_connector

@app.route('/test')
def index():
  return 'Server Works!'


unpacked_brands = json.loads(redis_connector.r.get('brands'))
pp = [x for x in unpacked_brands if x['colors'] == "blue"]
out_put=  json.dumps(pp)
#print(out_put)



#unpacked_images = json.loads(r.get('brands').decode('utf-8'))
