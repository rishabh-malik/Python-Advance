import twitter

Consumer_Key="QWrnVQmW72MXfcgtAJpgQQFkJ"
Consumer_Secret="cHM48CBMBtqjBvdOeOuSoXGR1RuJsNYMG3pkYsNZPDGdeUI1Lq"
access_token="2205935751-jQSxLvlaaX6CnUnzO5gkhG5gZiDdDy9jgtwZ4Ho"
access_token_secret="bFgs1SVKDHRvaIdPRVt3ET4WACvmXUjvDSkBxMjBlnDEg"

#connecting to the api
api=twitter.Api(consumer_key=Consumer_Key,
                consumer_secret=Consumer_Secret,
                access_token_key=access_token,
                access_token_secret=access_token_secret)

#to see its working properly or not
print api.VerifyCredentials()

#to get users which twitter considers friends
friends=api.GetFriends()
print friends

#getting the followers
followers=api.GetFollowers()
print followers

#to post a tweet
post_update=api.PostUpdate(status="Python is amazing!")

# All other things that can be done

# api.PostUpdates(status)
# api.PostDirectMessage(user, text)
# api.GetUser(user)
# api.GetReplies()
# api.GetUserTimeline(user)
# api.GetHomeTimeline()
# api.GetStatus(status_id)
# api.DestroyStatus(status_id)
# api.GetFriends(user)
# api.GetFollowers()
# api.GetFeatured()
# api.GetDirectMessages()
# api.GetSentDirectMessages()
# api.PostDirectMessage(user, text)
# api.DestroyDirectMessage(message_id)
# api.DestroyFriendship(user)
# api.CreateFriendship(user)
# api.LookupFriendship(user)
# api.VerifyCredentials()