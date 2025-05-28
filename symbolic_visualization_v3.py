import matplotlib.pyplot as plt

class SymbolicVisualizer:
    def __init__(self, world, belief_system):
        self.world = world
        self.belief_system = belief_system

    def summarize_beliefs(self):
        counts = {}
        for entity in self.world.entities:
            b = self.belief_system.get_belief(entity)
            if b:
                key = b.split("_belief_")[0]
                counts[key] = counts.get(key, 0) + 1
        return counts

    def plot_belief_map(self):
        data = self.summarize_beliefs()
        if not data:
            print("❗ No belief data yet.")
            return
        labels = list(data.keys())
        values = list(data.values())
        plt.figure(figsize=(8, 4))
        plt.bar(labels, values)
        plt.title("Symbolic Belief Overview")
        plt.xlabel("Belief Context")
        plt.ylabel("Number of Entities")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()