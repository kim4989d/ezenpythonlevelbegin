class it_2:

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
          raise  StopIteration
        self.index = self.index - 1
        return self.data[self.index]


it2 = it_2('abcde')
iter(it2)
# print(itervalue.__next__())

for i in it2:
    print(i)
