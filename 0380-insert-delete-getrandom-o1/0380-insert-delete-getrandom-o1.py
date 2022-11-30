class RandomizedSet:

    def __init__(self):
        self.dic = set()

    def insert(self, val: int) -> bool:
        len1 = len(self.dic)
        self.dic.add(val)
        len2 = len(self.dic)
        return not (len1 == len2)
        # if val in self.dic:
        #     return False
        # else:
        #     self.dic.add(val)
        #     return True

    def remove(self, val: int) -> bool:
        # len1 = len(self.dic)
        # self.dic.remove(val)
        # len2 = len(self.dic)
        # return not (len1 == len2)
        if val in self.dic:
            self.dic.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        if len(self.dic)>0:
            return random.sample(self.dic, 1)[0]
        else:
            return False


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()