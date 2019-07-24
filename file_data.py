

from flask import Flask
app = Flask(__name__)

import json
import redis_connector
from flask import Flask, request
from collections import defaultdict
from collections import Counter

@app.route('/test')
def index():
  return 'Server Works!'




@app.route('/getBrandsCount', methods=['GET','POST'])
def get_items_brans_count():
	unpacked_brands = json.loads(redis_connector.r.get('brands'))
	date_added = request.form['date_added']
	pp = [x for x in unpacked_brands if x['dateAdded'] == date_added]
	values = [d['brand'] for d in pp]
	counter = Counter(values)
	return json.dumps(counter)


@app.route('/getItemsbyColor', methods=['GET','POST'])
def get_items_by_color():
	unpacked_brands = json.loads(redis_connector.r.get('brands'))
	color = request.form['color']
	pp = [x for x in unpacked_brands if x['colors'] == color]
	rest_list = pp[:10]
	return json.dumps(rest_list)

	



@app.route('/getRecentItem', methods=['GET','POST'])
def get_recent_item_by_date():
	unpacked_brands = json.loads(redis_connector.r.get('brands'))
	date_added = request.form['date_added']
	pp = [x for x in unpacked_brands if x['dateAdded'] == date_added]
	reverse_list = pp.reverse()
	rest_list = pp[:1]
	return json.dumps(rest_list)







