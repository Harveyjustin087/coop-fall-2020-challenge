class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.history = 0
        self.change = []

    def add(self, num: int):
        final = sum(num, self.value)
        self.history += 1
        self.change.append(final)
        return final

    def subtract(self, num: int):
        final = self.value - num
        self.history += 1
        self.change.append(final)
        return final

    def undo(self):
        if(self.history > 0):
            self.history -= 1
            final = self.change[self.history]
        else:
            print("Nothing to Undo")
        return final

    def redo(self):
        if(self.history + 1 < len(self.history)):
            self.history += 1
            final = self.change[self.history]
        else:
            print("Nothing to Redo")
        return final

    def bulk_undo(self, steps: int):
        final = self.change[steps]
        self.history -= steps
        return final

    def bulk_redo(self, steps: int):
        final = self.change[steps]
        self.history += steps
        return final
