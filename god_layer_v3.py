class GodLayer:
    def __init__(self, world):
        self.world = world
        self.saved_states = {}
        self.speed_multiplier = 1

    def set_speed(self, multiplier):
        self.speed_multiplier = multiplier
        print(f"[⏩] Simulation speed set to x{multiplier}")

    def step(self, steps=1):
        for _ in range(steps * self.speed_multiplier):
            self.world.step()

    def pause(self):
        self.speed_multiplier = 0
        print("[⏸️] Simulation paused.")

    def resume(self):
        if self.speed_multiplier == 0:
            self.speed_multiplier = 1
        print("[▶️] Simulation resumed at x1.")

    def save_state(self, label):
        self.saved_states[label] = self._clone_world()
        print(f"[📌] Saved world state as '{label}'.")

    def load_state(self, label):
        if label in self.saved_states:
            self.world = self.saved_states[label]._clone_world()
            print(f"[↩️] Loaded saved world state '{label}'.")

    def _clone_world(self):
        import copy
        return copy.deepcopy(self.world)