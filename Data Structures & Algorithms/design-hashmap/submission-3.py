class MyHashMap:

    def __init__(self):
        self.x = []

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.x)):
            if self.x[i][0] == key:
                self.x[i] = [key, value]
                return
        self.x.append([key, value])

    def get(self, key: int) -> int:
        for i in range(len(self.x)):
            if self.x[i][0] == key:
                return self.x[i][1]
        return -1

    def remove(self, key: int) -> None:
        for i in range(len(self.x)):
            if self.x[i][0] == key:
                self.x.remove(self.x[i])
                return



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)