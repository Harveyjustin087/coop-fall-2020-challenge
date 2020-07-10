class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.history = 0
        self.change = []

    def add(self, num: int):
        final = 0
        final = num + self.value
        self.history += 1
        self.change.append(final)
        return final

    def subtract(self, num: int):
        final = 0
        final = self.value - num
        self.history += 1
        self.change.append(final)
        return final

    def undo(self):
        final = 0
        if(self.history > 0):
            self.history -= 1
            final = int(self.change[self.history])
        else:
            print("Nothing to Undo")
        return final

    def redo(self):
        final = 0
        if(self.history + 1 < len(self.change)):
            self.history += 1
            final = int(self.change[self.history])
        else:
            print("Nothing to Redo")
        return final

    def bulk_undo(self, steps: int):
        final = 0
        if(steps > self.change[steps] ):
            print("index out of range")
        else:
            final = int(self.change[steps])
            self.history -= steps
        return final

    def bulk_redo(self, steps: int):
        final = 0
        if(steps > self.change[steps] ):
            print("index out of range")
        else:
            final = int(self.change[steps])
            self.history += steps
        return final
