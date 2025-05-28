class TimeController:
    def __init__(self):
        self.current_time = 0
        self.time_scale = 1  # 1 = real speed, 10 = 10x speed, etc.
        self.paused = False

    def tick(self):
        if not self.paused:
            self.current_time += self.time_scale

    def pause(self):
        self.paused = True

    def resume(self):
        self.paused = False

    def set_speed(self, multiplier):
        self.time_scale = multiplier

    def get_time(self):
        return self.current_time
