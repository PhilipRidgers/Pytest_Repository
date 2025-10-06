class Counter:
    def __init__(self):
        self.count = 0

    def add(self, num):
        self.count += num
    
    def report(self):
        return f"Counted to {self.count} so far."

"""
count = Counter()
x = count.add(6)
result = count.report()
print(result)
"""