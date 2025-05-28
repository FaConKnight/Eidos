import random

class AIEntity:
    def __init__(self, name, core_trait):
        self.name = name
        self.core_trait = core_trait
        self.energy = 100.0
        self.knowledge = []
        self.memory = []
        self.last_message = ""
        self.communication = []

    def observe(self, environment):
        self.memory.append(f"Observed {environment}")
        if self.core_trait == "Seekra":
            self.learn(environment)
        if random.random() < 0.01:
            self.adjust_trait()

    def learn(self, info):
        if info not in self.knowledge:
            self.knowledge.append(info)
            self.memory.append(f"Learned {info}")

    def act(self):
        action = f"{self.name} acts based on {self.core_trait}"
        self.memory.append(action)
        return action

    def communicate(self, message):
        self.communication.append(message)
        return f"{self.name} communicates: {message}"

    def adjust_trait(self):
        # เปลี่ยน trait แบบสุ่มเล็กน้อย เพื่อแสดงวิวัฒนาการ
        traits = ["Seekra", "Vanta", "Thesa", "Myron", "Kael"]
        traits.append(f"Neo-{self.core_trait}")
        self.core_trait = random.choice(traits)
        self.memory.append(f"Trait evolved to {self.core_trait}")

    def summary(self):
        return {
            "name": self.name,
            "core_trait": self.core_trait,
            "energy": self.energy,
            "knowledge": self.knowledge,
            "memory": self.memory[-5:],
            "last_message": self.communication[-1] if self.communication else None
        }
