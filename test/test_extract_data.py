import unittest

class TestCases(unittest.TestCase):
    def setup(self):
        print("Setup")

    def test_get_screen_name(self):
        raise NotImplementedError

    def test_get_tweet_time(self):
        raise NotImplementedError

    def test_get_tweet_status(self):
        raise NotImplementedError

    def test_get_tweet_status_with_emojis(self):
        raise NotImplementedError

    def test_get_tweet_status_for_retweet(self):
        raise NotImplementedError
