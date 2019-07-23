

from pyspark import SparkContext
from pyspark.sql import *
import redis
import pandas as pd
import json
import redis_connector


sc = SparkContext('local','example')  # if using locally
sql_sc = SQLContext(sc)

sa = SparkContext.getOrCreate()
spark = SparkSession(sa)


brands_df = sql_sc.read.format('csv').options(header='true', inferSchema='true').load('testdate.csv')


df_json = brands_df.toJSON().map(lambda j: json.loads(j)).collect()
json_brands = json.dumps(df_json)
redis_connector.r.set('brands', json_brands)

unpacked_brands = json.loads(redis_connector.r.get('brands'))
pp = [x for x in unpacked_brands if x['colors'] == "blue"]
out_put=  json.dumps(pp)
print(out_put)




