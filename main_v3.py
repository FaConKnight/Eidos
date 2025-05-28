from world_v3 import World
from entities_v3 import AIEntity
from god_layer_v3 import GodLayer
from visualization_v3 import Visualization
from belief_and_economy_v3 import BeliefSystem, EconomySystem
from symbolic_visualization_v3 import SymbolicVisualizer

def run_simulation(rounds=100):
    world = World()
    god = GodLayer(world)
    viz = Visualization(world)
    beliefs = BeliefSystem()
    economy = EconomySystem()
    symbolic = SymbolicVisualizer(world, beliefs)

    # เพิ่ม AI 5 ตัวพร้อม Core Traits
    entities = [
        AIEntity("Seekra", "Seekra"),
        AIEntity("Vanta", "Vanta"),
        AIEntity("Thesa", "Thesa"),
        AIEntity("Myron", "Myron"),
        AIEntity("Kael", "Kael")
    ]

    for ent in entities:
        world.add_entity(ent)
        economy.assign_resources(ent)

    god.set_speed(1)

    for i in range(rounds):
        god.step(1)
        summary = god.world.summary()
        print(f"🕒 Time: {summary['time']}")
        print(f"🌦️ Weather: {summary['weather']}")

        for e in world.entities:
            print(f"🧠 {e.name} | Trait: {e.core_trait}")
            print(f"  Energy: {e.energy:.2f}")
            print(f"  Knowledge: {e.knowledge}")
            print(f"  Memory: {e.memory}")
            print(f"  Last Message: {e.last_message}")
            belief = beliefs.form_belief(e, world.weather)
            print(f"  Belief: {belief}")
            resources = economy.get_resources(e)
            print(f"  Resources: {resources}")

        if summary['new_offspring']:
            print(f"🍼 New Offspring: {summary['new_offspring']}")
        evo = summary['evolution']
        print(f"🧬 Generations: {evo['generation_count']}, Population per Gen: {evo['population_history']}")
        print("=" * 50)

        if summary['time'] in [25, 50]:
            god.save_state(f"milestone_{summary['time']}")

        if summary['time'] % 10 == 0:
            viz.plot_map()

        if summary['time'] % 20 == 0:
            symbolic.plot_belief_map()

if __name__ == "__main__":
    run_simulation()