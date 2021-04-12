from django.db import models

# Create your models here.
class options(models.Model):
    user = "User"
    created = "Created_At"
    content = "Tweet_Content"
    likes = "Like_Count"
    retweets = "Retweet_Count"
    discussions = "Discussion_Count"
    ascending = True
    descending = False
    count10 = 10
    count50 = 50
    count100 = 100
    ORDER = [
        (user, "User"),
        (created, "Created_At"),
        (content, "Tweet_Content"),
        (likes,"Like_Count"),
        (retweets,"Retweet_Count"),
        (discussions,"Discussion_Count")
        ]
    SORT = [
        (ascending,"Ascending"),
        (descending,"Descending")
        ]
    COUNT = [
        (count10,"10"),
        (count50,"50"),
        (count100,"100")
        ]
    order = models.CharField(choices = ORDER, max_length=40)
    sort = models.CharField(choices = ORDER, max_length=40)
    count = models.CharField(choices = COUNT, max_length=40)
    
    def __str__(self):
        return self.order

    