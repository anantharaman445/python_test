

from flask import Flask
app = Flask(__name__)

import json
import redis_connector
from flask import Flask, request

@app.route('/test')
def index():
  return 'Server Works!'


unpacked_brands = json.loads(redis_connector.r.get('brands'))
pp = [x for x in unpacked_brands if x['colors'] == "blue"]
out_put=  json.dumps(pp)
#print(out_put)
@app.route('/getRecentItem', methods=['GET','POST'])
def get_recent_item_by_date():
	unpacked_brands = json.loads(redis_connector.r.get('brands'))
	date_added = request.form['date_added']
	# date_added = '23-07-2019'
	pp = [x for x in unpacked_brands if x['dateAdded'] == date_added]
	print(pp)
	return json.dumps(pp)


#unpacked_images = json.loads(r.get('brands').decode('utf-8'))
