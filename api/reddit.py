import praw

number_of_searches = 10
search = ['NVDA', 'TESLA', 'TSLA', 'AMD','sPY','DKn','comparison']
ignore = ['48']

PERSONAL_USE_SCRIPT = ''
SECRET = ''
APP_NAME = ''
USERNAME = ''
PASSWORD = ''

reddit = praw.Reddit(
                        client_id=PERSONAL_USE_SCRIPT,
                        client_secret=SECRET,
                        user_agent=APP_NAME,
                        username=USERNAME,
                        password=PASSWORD
                    )

stocks = reddit.subreddit('wallstreetbets').search('flair:"stocks"',sort='new',limit=number_of_searches)
options = subred = reddit.subreddit('wallstreetbets').search('flair:"options"',sort='new',limit=number_of_searches)
for post in stocks:
    for search_word in search:
        if search_word.upper() in (post.title + post.selftext).upper():
            to_ignore = False
            for ignore_word in ignore:
                if ignore_word.upper() in (post.title + post.selftext).upper():
                    to_ignore = True
                    break
            if not to_ignore:
                print("\n#######################\n")
                print(post.title+'\n')
                # print(post.selftext+'\n')
                print(post.url)
                break
