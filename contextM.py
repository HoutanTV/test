class Indenter:
    def __init__(self):
        self.sentence = ""
        self.called_times_enter = 0


    def print(self,our_str):
        if self.called_times_enter == 1:
            self.sentence = our_str
            print(self.sentence)
        if self.called_times_enter > 1:
            self.sentence = "   "*(self.called_times_enter-1) + our_str
            print(self.sentence)
        return self.sentence

    def __enter__(self):
        self.sentence = ""
        self.called_times_enter += 1
        return self.sentence

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.called_times_enter -= 1
        return True


indent = Indenter()

with indent:
    indent.print("Hi")
    with indent:
        indent.print("Talk is cheap")
        with indent:
            indent.print("Show me the code ...")
    indent.print("Trovalds")