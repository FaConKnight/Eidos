import random

class EvolutionEngine:
    def __init__(self):
        self.generations = []
        self.generation_count = 0

    def evolve(self, population):
        new_generation = []
        for parent in population:
            if parent.energy > 50:  # เงื่อนไขสืบพันธุ์เบื้องต้น
                child = self.mutate(parent)
                new_generation.append(child)
        if new_generation:
            self.generations.append(new_generation)
            self.generation_count += 1
        return new_generation

    def mutate(self, parent):
        trait = parent.core_trait
        name = f"{trait}_Child_{random.randint(1000, 9999)}"
        child = parent.__class__(name, trait)
        child.knowledge = parent.knowledge[:random.randint(1, len(parent.knowledge))] if parent.knowledge else []
        return child

    def get_stats(self):
        return {
            "generation_count": self.generation_count,
            "population_history": [len(gen) for gen in self.generations]
        }