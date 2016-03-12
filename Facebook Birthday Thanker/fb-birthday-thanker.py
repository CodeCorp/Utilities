import json
import fb                     #To install this package run: sudo pip install fb
from facepy import GraphAPI   #To install this package run: sudo pip install facepy
import datetime

'''
TODO:
  - Search the post for string 'happy' and then only post bday wishes
  - Tag friends instead of just putting the names.

'''

#facebook user access token here with extented permissions to post | https://developers.facebook.com/tools/explorer
token='----' # enter your token here ^^^ 
facebook=fb.graph.api(token)
graph = GraphAPI(token)
since_date = "1391212800" #unix time stamp for the time since when you want the posts to be commented
readable_since_date = datetime.datetime.fromtimestamp(int(since_date)).strftime('%Y-%m-%d %H:%M:%S')

def getComment(id):

    query = id+'?fields=message,from'
    result = graph.get(query)
    commentor_name = result['from']['name']
    commentor_id = result['from']['id']
    comment = 'Thank You ' + commentor_name +' :)'

    print "\nPost    : " + result['message'].split('\n')[0] #prints only the first line of post
    print "Comment : " + comment 
    return comment


def ThankAndLike():

    query="me/posts?fields=id&limit=500&since="+since_date
    result=graph.get(query)
    
    idlist=[x['id'] for x in result['data']] #post id's of all the posts in the time-frame
    idlist.reverse() #order it from recent to old
    print("There are "+ str(len(idlist)) +" posts since "+readable_since_date)
    
    char1=raw_input("Are you sure you want to comment and like the posts? (y/n) ")
    count=0
    if char1=='y':
        nos=input("Enter number of latest posts to be commented and liked : ")
        
        if nos<=len(idlist):
           for p_id in (idlist[(len(idlist)-nos):]):
              mess = getComment (p_id)
              facebook.publish(cat="comments",id=p_id,message=mess) #Comments on each post
              facebook.publish(cat="likes",id=p_id)                 #Likes each post
              count=count+1
              print("Notification "+str(count)+" : www.facebook.com/"+str(p_id).split('_')[0]+"/posts/"+str(p_id).split('_')[1])
        else: 
              print("Not that many posts available")
    else :
      print("No commenting then.")

ThankAndLike()
