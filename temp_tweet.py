import tweepy, json, time
import conf
from boltiot import Bolt
config = {
"consumer_key" : conf.consumer_key,
"consumer_secret" : conf.consumer_secret,
"access_token" : conf.access_token,
"access_token_secret" : conf.access_token_secret
}
def get_api_object(cfg):
	auth = tweepy.OAuthHandler(cfg['consumer_key'],cfg['consumer_secret'])
	auth.set_access_token(cfg['access_token'],cfg['access_token_secret'])
	return tweepy.API(auth)
api_object = get_api_object(config)
mybolt = Bolt(conf.bolt_cloud_api_key, conf.device_id)
temp_threshold = 59
while True:
	response = mybolt.analogRead('A0')
	data = json.loads(response)
	print(data['value'])
	try:
		sensor_value = int(data['value'])
		if sensor_value > temp_threshold:
			tweet = "Temperature has crossed the thershold"
			api_object.update_status(tweet)
	except Exception as e:
		print("Error",e)
	time.sleep(10)
