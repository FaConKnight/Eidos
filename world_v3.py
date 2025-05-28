from physics_engine import PhysicsEngine
from time_controller import TimeController
from entities_v3 import AIEntity
from evolution_v3 import EvolutionEngine

class World:
    def __init__(self):
        self.physics = PhysicsEngine()
        self.time = TimeController()
        self.evolution = EvolutionEngine()
        self.entities = []
        self.offspring = []
        self.weather = self.generate_weather()

    def add_entity(self, entity):
        self.entities.append(entity)

    def step(self):
        self.time.tick()
        self.physics.update_weather()
        for entity in self.entities:
            entity.observe(self.physics.weather)
            self.physics.tick(entity)
            entity.act()
            entity.communicate(f"State at T={self.time.get_time()}")

        # ทุก 10 รอบให้ลองสืบพันธุ์
        if self.time.get_time() % 10 == 0:
            new_entities = self.evolution.evolve(self.entities)
            self.entities.extend(new_entities)
            self.offspring = new_entities

    def summary(self):
        return {
            "time": self.time.get_time(),
            "weather": self.physics.weather,
            "entities": [entity.summary() for entity in self.entities],
            "evolution": self.evolution.get_stats(),
            "new_offspring": [e.name for e in self.offspring]
        }
