import redis

r = redis.Redis(
    host='localhost',
    # host='redisden.21uqea.ng.0001.aps1.cache.amazonaws.com', this is for elastic cache aws
    port=6379, 
    db = 0,
    decode_responses=True,
    password='')
