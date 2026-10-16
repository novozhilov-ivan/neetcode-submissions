class Twitter:
    def __init__(self):
        self.count = 0
        self.tweet_map = defaultdict(set) # list of [count, tweetId]
        self.follow_map = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res, min_h = [], []

        self.follow_map[userId].add(userId)
        for followeeId in self.follow_map[userId]:
            if followeeId in self.tweet_map:
                index = len(self.tweet_map[followeeId]) - 1
                count, tweetId = self.tweet_map[followeeId][index]
                min_h.append([count, tweetId, followeeId, index - 1])
            heapq.heapify(min_h)
        
        while min_h and len(res) < 10:
            _, tweetId, followeeId, index = heapq.heappop(min_h)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweet_map[tweet]



    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[folloewId].add(followerId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follow_map: 
            self.follow_map[followerId].add(followerId)
        
