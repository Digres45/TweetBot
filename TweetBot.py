added

# TweetBot
import tweepy

def letstweet():
    print("Enter your tweet " + user.name)
    tweet = getStatus()
    try:
        api.update_status(tweet)
        print("Successfuly post tweet...!!!")
    except Exception as e:
        print(e)
        return
        
def getStatus():
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    status = '\n'.join(lines)
    return status

def main():
    global api, user, auth
    ck = "write consumer key" 
    # consumer key
    cks = "write consumer key SECRET" 
    # consumer key SECRET
    at = "write access token" 
    # access token
    ats = "write access token secret" 
    # access token SECRET

    auth = tweepy.OAuthHandler(ck,cks)
    auth.set_access_token(at,ats)

    api = tweepy.API(auth)
    user = api.me()

    letstweet()

main()
