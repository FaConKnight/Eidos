class TimeController:
    def __init__(self):
        self.time = 0
        self.paused = False
        self.speed_multiplier = 1

    def tick(self):
        if not self.paused:
            self.time += 1 * self.speed_multiplier

    def set_speed(self, multiplier):
        self.speed_multiplier = multiplier

    def pause(self):
        self.paused = True

    def resume(self):
        self.paused = False

    def get_time(self):
        return self.time