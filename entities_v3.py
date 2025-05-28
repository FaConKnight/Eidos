import random
import uuid

class AIEntity:
    def __init__(self, name=None, core_trait=None, generation=0):
        self.id = str(uuid.uuid4())
        self.name = name or f"AI_{self.id[:5]}"
        self.core_trait = core_trait or random.choice(["Seekra", "Vanta", "Thesa", "Myron", "Kael"])
        self.energy = 1.0
        self.age = 0
        self.generation = generation
        self.knowledge = []
        self.memory = []
        self.communication = []
        self.children = []

    def observe(self, environment):
        self.memory.append(f"Observed: {environment}")
        if self.core_trait == "Seekra":
            self.learn(str(environment))
        if random.random() < 0.01:
            self.adjust_trait()

    def learn(self, info):
        if info not in self.knowledge:
            self.knowledge.append(info)
            self.memory.append(f"Learned: {info}")

    def act(self):
        action = f"{self.name} acts based on {self.core_trait}"
        self.memory.append(action)
        self.energy -= 0.01
        self.age += 1
        return action

    def communicate(self, message):
        self.communication.append(message)
        self.memory.append(f"Communicated: {message}")
        return f"{self.name} says: {message}"

    def adjust_trait(self):
        traits = ["Seekra", "Vanta", "Thesa", "Myron", "Kael"]
        traits.append(f"Neo-{self.core_trait}")
        self.core_trait = random.choice(traits)
        self.memory.append(f"Trait evolved to {self.core_trait}")

    def is_alive(self):
        return self.energy > 0 and self.age < 100

    def summary(self):
        return {
            "name": self.name,
            "core_trait": self.core_trait,
            "generation": self.generation,
            "age": self.age,
            "energy": round(self.energy, 2),
            "knowledge_count": len(self.knowledge),
            "last_memory": self.memory[-3:],
            "last_message": self.communication[-1] if self.communication else None
        }
