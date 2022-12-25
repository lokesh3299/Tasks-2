class Fibonacci:

    def __init__(self, max=int(input('Enter maximum value: '))):
        self.max = max

    def __iter__(self):
        self.first = 0
        self.second = 1
        return self

    def __next__(self):
        self.return_value = self.first
        if self.first > self.max:
            raise StopIteration

        self.third = self.first + self.second
        self.first = self.second
        self.second = self.third
        return self.return_value


for f in Fibonacci():
    print(f)
