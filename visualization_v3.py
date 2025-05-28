import matplotlib.pyplot as plt
import random

class Visualization:
    def __init__(self, world):
        self.world = world
        self.map_size = (20, 20)
        self.positions = {}

    def update_positions(self):
        for i, entity in enumerate(self.world.entities):
            if entity.name not in self.positions:
                # สุ่มตำแหน่งเริ่มต้น
                self.positions[entity.name] = [
                    random.randint(0, self.map_size[0] - 1),
                    random.randint(0, self.map_size[1] - 1)
                ]
            else:
                # ขยับเล็กน้อยแบบสุ่ม
                dx, dy = random.choice([(-1,0),(1,0),(0,-1),(0,1),(0,0)])
                self.positions[entity.name][0] = max(0, min(self.map_size[0] - 1, self.positions[entity.name][0] + dx))
                self.positions[entity.name][1] = max(0, min(self.map_size[1] - 1, self.positions[entity.name][1] + dy))

    def plot_map(self):
        self.update_positions()
        plt.figure(figsize=(6, 6))
        plt.xlim(0, self.map_size[0])
        plt.ylim(0, self.map_size[1])
        plt.grid(True)
        for name, pos in self.positions.items():
            plt.text(pos[0] + 0.1, pos[1] + 0.1, name[:2], fontsize=9)
        plt.title(f"Map at Time {self.world.time.get_time()}")
        plt.show()