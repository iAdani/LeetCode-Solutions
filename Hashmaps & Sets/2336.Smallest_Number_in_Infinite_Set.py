class SmallestInfiniteSet:
    # O(1)
    def __init__(self):
        self.smallest = 1
        self.added = set()

    # O(N)
    def popSmallest(self) -> int:
        ret = 0
        if not self.added:
            ret = self.smallest
            self.smallest += 1
        else:
            ret = min(self.added)
            self.added.remove(ret)
        return ret

    # O(1)
    def addBack(self, num: int) -> None:
        if num < self.smallest:
            self.added.add(num)

        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)