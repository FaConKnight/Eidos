import random

class PhysicsEngine:
    def __init__(self):
        self.weather = self.generate_weather()
        self.gravity = 9.8  # m/s^2
        self.resistance = 0.1  # air resistance coefficient
        self.decay_rate = 0.01  # entropy-like decay per tick

    def generate_weather(self):
        return {
            "type": random.choice(["sunny", "cloudy", "rainy", "stormy", "windy"]),
            "temperature": round(random.uniform(-10, 40), 1),
            "humidity": round(random.uniform(0.2, 1.0), 2)
        }

    def update_weather(self):
        # Change weather with slight variation over time
        self.weather = self.generate_weather()

    def apply_physics(self, entity):
        # Apply decay over time
        entity.energy -= self.decay_rate
        if entity.energy < 0:
            entity.energy = 0
        # Apply temperature effect (sample logic)
        if self.weather["temperature"] < 0:
            entity.energy -= 0.01

    def tick(self, entity):
        self.apply_physics(entity)
