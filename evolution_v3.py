import random
from entities_v3 import AIEntity

class EvolutionEngine:
    def __init__(self):
        self.births = 0
        self.deaths = 0

    def evolve(self, entities):
        new_entities = []
        survivors = [e for e in entities if e.is_alive()]

        for parent in survivors:
            if parent.energy > 50:
                if random.random() < 0.3:  # อัตราสืบพันธุ์ 30%
                    child = AIEntity(
                        name=None,
                        core_trait=parent.core_trait,
                        generation=parent.generation + 1
                    )
                    if random.random() < 0.3:  # 30% กลายพันธุ์
                        child.adjust_trait()

                    parent.children.append(child.name)
                    new_entities.append(child)
                    self.births += 1

        self.deaths += len(entities) - len(survivors)
        return new_entities

    def get_stats(self):
        return {
            "births": self.births,
            "deaths": self.deaths
        }