tweet = input("Type out your tweet for me: ")
tweet_length = len(tweet.strip().replace(' ', ''))

if tweet_length < 1:
    print(f'Whoa man... that \"{tweet}\" is not even possible.')
elif tweet_length < 10:
    print(f"Sorry, your tweet \"{tweet}\" is too short")
elif tweet_length < 35:
    print(f"Sorry, your tweet \"{tweet}\" is not long enough")
else:
    print(f"Your tweet \"{tweet}\" long enough")

