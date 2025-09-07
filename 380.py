from random import randint


class RandomizedSet:

    def __init__(self):
        self.seen = {}
        self.vals = []
        self.top = -1

    def insert(self, val: int) -> bool:
        if val in self.seen:
            return False

        self.top += 1
        self.seen[val] = self.top
        self.vals.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.seen:
            return False

        idx = self.seen[val]
        last = self.vals[self.top]
        self.seen[last] = idx
        self.vals[idx] = last
        self.top -= 1
        del self.seen[val]

        return True

    def getRandom(self) -> int:
        idx = randint(0, self.top)

        return self.vals[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
