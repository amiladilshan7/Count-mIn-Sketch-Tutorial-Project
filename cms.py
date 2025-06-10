import math
import mmh3




class CountMinSketch:
    def __init__(self, epsilon=0.01, delta =0.01):
        self.epsilon = epsilon
        self.delta = delta
        self.w = math.ceil(math.e/epsilon)
        self.d = math.ceil(math.log(1/delta))
        self.table = [[0]* self.w for _ in range(self.d)]


    def _hash(self, item, seed):

        return mmh3.hash(str(item), seed) % self.w


    def add(self, item, count=1):
        for i in range(self.d):
            index = self._hash(item,i)
            self.table[i][index]+=count


    def estimate(self, item):
        return min(
            self.table[i][self._hash(item,i)]
            for i in range(self.d)

        )
    def __str__(self):
        return "\n".join(str(row) for row in self.table)

