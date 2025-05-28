import random
import math

class PhysicsEngine:
    def __init__(self, gravity=9.81, energy_loss_rate=0.01, friction=0.05):
        self.gravity = gravity
        self.energy_loss_rate = energy_loss_rate
        self.friction = friction
        self.weather = {
            "temperature": 25.0,
            "type": "clear"
        }

    def apply_gravity(self, entity):
        # แรงโน้มถ่วงดึงพลังงานลงในแต่ละรอบ
        entity.energy -= self.gravity * 0.01

    def apply_friction(self, entity):
        entity.energy -= self.friction * 0.01

    def apply_energy_decay(self, entity):
        entity.energy -= entity.energy * self.energy_loss_rate

    def update_weather(self):
        temp_change = random.uniform(-0.5, 0.5)
        self.weather["temperature"] += temp_change

        # เปลี่ยนประเภทของสภาพอากาศแบบสุ่ม
        weather_types = ["clear", "rain", "storm", "cloudy"]
        self.weather["type"] = random.choices(
            weather_types, weights=[0.6, 0.2, 0.1, 0.1])[0]

    def tick(self, entity):
        self.apply_gravity(entity)
        self.apply_friction(entity)
        self.apply_energy_decay(entity)