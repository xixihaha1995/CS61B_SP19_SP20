class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.v_ = collections.defaultdict(list)
        self.t_ = collections.defaultdict(list)
        self.max_ = collections.defaultdict(int)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.v_[key].append(value)
        self.t_[key].append(timestamp)
        self.max_[key] = max(self.max_[key], timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.t_: return ""
        if timestamp >= self.max_[key]:
            return self.v_[key][-1]
        time = bisect.bisect_right(self.t_[key], timestamp)
        if time:
            return self.v_[key][time-1]
        return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)