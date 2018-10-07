import conf
import tweepy
config = {
"consumer_key" : conf.consumer_key,
"consumer_secret" : conf.consumer_secret,
"access_token" : conf.access_token,
"access_token_secret" : conf.access_token_secret
}
def get_api_object(cfg):
	auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
	auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
	return tweepy.API(auth)
api_object = get_api_object(config)
tweet = "Hello beautiful people, I hope you all are enjoying your day!!"
status = api_object.update_status(tweet)


