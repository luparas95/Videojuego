class State:

    def __init__(self):
        self.done = False
        self.next_state = ""
        self.previous_state = ""
        self.score = 0

    def enter(self):
        pass

    def exit(self):
        pass

    def handle_input(self, event):
        pass

    def update(self, delta_time):
        pass

    def render(self, surface):
        pass
