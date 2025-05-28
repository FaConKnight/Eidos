from world_v3 import World
from entities_v3 import AIEntity
from god_layer_v3 import GodLayer
from visualization_v3 import Visualization

def run_simulation(rounds=100):
    world = World()
    god = GodLayer(world)
    visual = Visualization(world)

    # เพิ่ม AI 5 ตัวพร้อม Core Traits
    world.add_entity(AIEntity("Seekra", "Seekra"))
    world.add_entity(AIEntity("Vanta", "Vanta"))
    world.add_entity(AIEntity("Thesa", "Thesa"))
    world.add_entity(AIEntity("Myron", "Myron"))
    world.add_entity(AIEntity("Kael", "Kael"))

    god.set_speed(1)  # เริ่มที่ x1

    for i in range(rounds):
        god.step(1)
        summary = god.world.summary()
        print(f"🕒 Time: {summary['time']}")
        print(f"🌦️ Weather: {summary['weather']}")
        for e in summary['entities']:
            print(f"🧠 {e['name']} | Trait: {e['core_trait']}")
            print(f"  Energy: {e['energy']:.2f}")
            print(f"  Knowledge: {e['knowledge']}")
            print(f"  Memory: {e['memory']}")
            print(f"  Last Message: {e['last_message']}")
        if summary['new_offspring']:
            print(f"🍼 New Offspring: {summary['new_offspring']}")
        evo = summary['evolution']
        print(f"🧬 Generations: {evo['generation_count']}, Population per Gen: {evo['population_history']}")
        print("=" * 50)

        # ตัวอย่างการบันทึก timeline
        if summary['time'] == 25:
            god.save_state("milestone_25")

        if summary['time'] == 50:
            god.save_state("milestone_50")

        # แสดงแผนที่ทุก 10 รอบ
        if summary['time'] % 10 == 0:
            visual.plot_map()

if __name__ == "__main__":
    run_simulation()