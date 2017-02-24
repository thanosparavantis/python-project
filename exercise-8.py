import sys
import tweepy

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

def askUsername(forUser):
    while True:
        user = raw_input("%s: " % forUser)
        if user:
            return user

def getFollowers(username):
    followers = []

    try:
        for users in tweepy.Cursor(api.followers, screen_name = username, count = 200).pages():
            for user in users:
                followers.append(user.screen_name)
    except tweepy.TweepError as e:
        print "Could not get %s's followers: %s" % (username, e.message[0]['message'])
        sys.exit()

    return followers

user1 = askUsername("User 1")
user2 = askUsername("User 2")

followers1 = getFollowers(user1)
followers2 = getFollowers(user2)

common = list(set(followers1) & set(followers2))

if (common):
    print "Common followers:"
    print ", ".join(map(str, common))
else:
    print "No common followers."
