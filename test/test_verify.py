import unittest

class TestCases(unittest.TestCase):
    def setup(self):
        print("Setup")

    def test_target_tweet_is_real(self):
        raise NotImplementedError

    def test_target_tweet_is_fake(self):
        raise NotImplementedError

    def test_target_tweet_is_not_found(self):
        raise NotImplementedError
