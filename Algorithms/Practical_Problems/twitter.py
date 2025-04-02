"""
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.
Implement the Twitter class:

Twitter() Initializes your twitter object.

void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.

List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.

void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.

void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.

Input
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]

Output
[null, null, [5], null, null, [6, 5], null, [5]]

Explanation
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2);    // User 1 follows user 2.
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
"""

import heapq, collections


class Twitter:

    def __init__(self):
        self.tweets = collections.defaultdict(list)
        self.follows = collections.defaultdict(set)
        self.tweet_count = 0

    def post_tweet(self, user: int, tweet: int) -> None:
        self.tweets[user].append((self.tweet_count, tweet))
        self.tweet_count -= 1

    def get_news_feed(self, user: int) -> list[int]:
        res, minHeap = [], []

        # Get all of the user's followee's tweets and put them in minHeap
        for followee in self.follows[user]:
            for tweet in self.tweets[followee]:
                minHeap.append(tweet)

        # Add all of the user's tweets to minHeap
        for tweet in self.tweets[user]:
            minHeap.append(tweet)

        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            _, newest_tweet = heapq.heappop(minHeap)
            res.append(newest_tweet)

        print(res)
        return res

    def follow(self, follower: int, followee: int) -> None:
        self.follows[follower].add(followee)

    def unfollow(self, follower: int, followee: int) -> None:
        if followee in self.follows[follower]:
            self.follows[follower].remove(followee)


twitter = Twitter()
twitter.post_tweet(1, 5)  # User 1 posts a new tweet (id = 5).
twitter.get_news_feed(
    1
)  # User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2)  # User 1 follows user 2.
twitter.post_tweet(2, 6)  # User 2 posts a new tweet (id = 6).
twitter.get_news_feed(
    1
)  # User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2)  # User 1 unfollows user 2.
twitter.get_news_feed(
    1
)  # User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
