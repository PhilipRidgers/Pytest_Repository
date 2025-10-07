class StringBuilder:
    def __init__(self):
        self.str = ""

    def add(self, str):
        self.str += str

    def size(self):
        return len(self.str)

    def output(self):
        return self.str

"""
one_string = StringBuilder()
one_string.add("The world went missing yesterday,\n")
one_string.add("while I was in the bath.\n")
one_string.add("Not much has changed since it returned,\n")
one_string.add("except we're all giraffes.")
result = one_string.output()
print(result)
"""