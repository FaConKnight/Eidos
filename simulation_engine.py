
from world_v3 import World
import export_log

class SimulationEngine:
    def __init__(self):
        self.world = World()
        self.running = False

    def step(self):
        self.world.step()
        export_log.export_population(self.world.time.get_time(), self.world.entities)
        return self.world.summary()

    def get_time(self):
        return self.world.time.get_time()
