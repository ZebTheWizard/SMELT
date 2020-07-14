import datetime
import difflib
# import datefinder

from dateparser.search import search_dates
from dateutil.parser import parse
from SMELT.validators.twitter.tweets import get_tweets
from SMELT.Validation import Validator
# from twitterscraper import
import twint


def fetch_closest_matching_tweet(username, message, time):
    tweets = []
    tweet = None
    conf = 0
    for tweet in get_tweets(username, pages=1):
        print(tweet['time'].date(), time.date())
        if tweet['time'].date() == time.date():
            tweets.append(tweet)
    # print(tweets)
    messages = list(map(lambda x: x['text'], tweets))
    matches = difflib.get_close_matches(message, messages, cutoff=0.7)
    if matches:
        text = matches[0]
        tweet = list(filter(lambda x: x['text'] == text, tweets))[0]
        conf = difflib.SequenceMatcher(None, text, message).ratio()
    else:
        conf = 1
    return tweet, conf


class SimpleTwitterValidator(Validator):
    display_name = ""
    username = ""
    body = ""
    time = ""
    conf = 0
    failed = False
    tweet = {}
    tc = None

    def __init__(self, image, **kwargs):
        super().__init__(image, confidence=0.9, **kwargs)
        if SimpleTwitterValidator.tc is None:
            SimpleTwitterValidator.setup()


    @staticmethod
    def setup(config=None, user_list=()):
        if config:
            SimpleTwitterValidator.tc = config
        else:
            SimpleTwitterValidator.tc = twint.Config()
            SimpleTwitterValidator.tc.Members_list = user_list
            SimpleTwitterValidator.tc.Database

    def get_tweet_date(self):
        matches = list(datefinder.find_dates(self.ocr.string))
        for line in self.ocr.lines:
            matches2 = parse()
            print(matches2)
        # d = matches[0]
        # try:
        #     date = '-'.join(dateline.split('-')[:2]).strip()
        #     try:
        #         time = datetime.datetime.strptime(date, '%I:%M %p - %m/%d/%y')
        #     except ValueError:
        #         time = datetime.datetime.strptime(date, '%I:%M %p - %b %d, %Y')
        return matches[0]

    def handle(self):
        print(self.ocr.lines)
        username = self.ocr.lines[1].split('@')[-1]
        message = ' '.join(self.ocr.chunks[1])
        time = self.get_tweet_date()
        print(time, username)
        self.tweet, self.conf = fetch_closest_matching_tweet(username, message, time)
        if self.tweet is None:
            self.failed = True

    def confidence(self):
        return max(min(self.conf + 0.01, 1), 0)

    def __str__(self):
        return """
        \rTWEET: %s
        \rCONFIDENCE: %f
        \rPASSING: %r
        """ % (self.tweet, self.confidence(), self.passing())