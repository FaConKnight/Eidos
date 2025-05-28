from world_v3 import World
from entities_v3 import AIEntity
import export_log

class SimulationEngine:
    def __init__(self):
        self.world = World()
        self.running = False
        self.initialize_entities()

    def initialize_entities(self):
        initial_traits = ["Seekra", "Vanta", "Thesa", "Myron", "Kael"]
        for trait in initial_traits:
            entity = AIEntity(name=trait, core_trait=trait)
            self.world.add_entity(entity)

    def step(self):
        self.world.step()
        return self.world.summary()
