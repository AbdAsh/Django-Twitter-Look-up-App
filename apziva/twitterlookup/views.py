from django.shortcuts import render
import tweepy as tw
import pandas as pd



# Create your views here.
def index(request):
    return render(request,'index.html')


def twitterlookup(sortType, order, count):
    consumer_key= 'SUh9Knu3bmN48jJXZfMZZjoA8'
    consumer_secret= 'rIq3n5Ax94wXE3DMgRSRL0Eh5Wa8kr6vvs6RWLjIt9PJ5YrWZE'
    access_token= '2231420115-0ECh6fpuAbsWd0hrn94QEOUaXiBOX85vTqX248E'
    access_token_secret= 'KdD837lm2bIGYmVsXsHXiJqspoSzMGxPMAdO5D0wM4nQg'

    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)

    search_words = "request for startup"

    tweets = tw.Cursor(api.search,q=search_words).items(count)

    extractedTweets = [[tweet.user.screen_name, tweet.created_at, tweet.text, tweet.favorite_count, tweet.retweet_count, "Only available with the Premium and Enterprise tier products."] for tweet in tweets]

    tweetTable = pd.DataFrame(data=extractedTweets, columns=["User", "Created At", "Tweet Content", "Like Count", "Retweet Count", "Discussion Count"])

    sortedtweetTable = tweetTable.sort_values(by=[sortType], ascending=order)