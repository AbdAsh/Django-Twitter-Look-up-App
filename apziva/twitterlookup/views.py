from django.shortcuts import HttpResponse, render
from django.http import HttpResponse
import tweepy as tw
import pandas as pd
from twitterlookup.forms import SortForm



# Create your views here.
def home(request):
    return render(request,'home.html')

def retweetSort(request):
    data = makeTable("Retweet_Count")
    context = {'data':data}
    return render(request,'index.html',context)

def likeSort(request):
    data = makeTable("Like_Count")
    context = {'data':data}
    return render(request,'index.html',context)

def disSort(request):
    data = makeTable("Discussion_Count")
    context = {'data':data}
    return render(request,'index.html',context)

def dataSort(request):
    sortform = SortForm()
    data = makeTable("Created_At")
    context = {'data':data}
    form = {'form':sortform}
    return render(request,'index.html',context)

def allSort(request):
    data = makeTable("All")
    context = {'data':data}
    return render(request,'index.html',context)
    
def makeTable(sortType):
    if sortType == "Retweet_Count":
        df = twitterlookup(["Retweet_Count"],False,100)
    elif sortType == "Like_Count":
        df = twitterlookup(["Like_Count"],False,100)
    elif sortType == "Discussion_Count":
        df = twitterlookup(["Discussion_Count"],False,100)
    elif sortType == "Created_At":
        df = twitterlookup(["Created_At"],False,100)
    elif sortType == "All":
        df = twitterlookup(["Retweet_Count","Like_Count","Discussion_Count","Created_At"],False,100)

    #This is variable holding a csv if needed
    csv = df.to_csv()
    ##########################################
    data=[]
    for i in range(df.shape[0]):
        temp=df.loc[i]
        data.append(dict(temp))
    return data

def twitterlookup(sortType, isAscending, count):
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

    tweetTable = pd.DataFrame(data=extractedTweets, columns=["User", "Created_At", "Tweet_Content", "Like_Count", "Retweet_Count", "Discussion_Count"])
    tweetTable['Created_At'] =pd.to_datetime(tweetTable.Created_At,format='%b %d, %Y, %H:%M *')
    #April 10, 2021, 9:51 p.m.

    sortedtweetTable = tweetTable.sort_values(by=sortType, ascending=isAscending, ignore_index=True)
    
    return sortedtweetTable

