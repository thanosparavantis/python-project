import re
import sys
import tweepy

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def askUsername(forUser):
    while True:
        user = raw_input("%s: " % forUser)
        if user:
            return user

def getTimeline(username):
    try:
        return api.user_timeline(screen_name = username, count = 10, include_rts = False)
    except tweepy.TweepError as e:
        print "Could not get %s's tweets: %s" % (username, e.message)
        sys.exit()

def getWordCount(timeline):
    length = 0
    for tweet in timeline:
        text = re.sub(r'http\S+', '', str(unicode(tweet.text.encode('UTF-8'), errors = 'ignore')).strip(' \t\n\r').replace('\n', ''))
        length += len(re.findall("[a-zA-Z_]+", text))
    return length

user1 = askUsername("User 1")
user2 = askUsername("User 2")

timeline1 = getTimeline(user1)
length1 = getWordCount(timeline1)

timeline2 = getTimeline(user2)
length2 = getWordCount(timeline2)

if (length1 > length2):
    print "%s has the longest word count of %s words." % (user1, length1)
    print "%s has %s words." % (user2, length2)
elif (length1 < length2):
    print "%s has the longest word count of %s words." % (user2, length2)
    print "%s has %s words." % (user1, length1)
else:
    print "Both %s and %s have the same word count of %s." % (user1, user2, length1)
