
import tkinter as tk
from tkinter import ttk, scrolledtext
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading
import time
from simulation_engine import SimulationEngine

class SimulationGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("EIDOS Civilization Monitor")

        self.sim = SimulationEngine()
        self.running = False
        self.speed = 1

        self.population_data = []

        # Controls
        control_frame = ttk.Frame(root)
        control_frame.grid(row=0, column=0, sticky="w")

        self.start_button = ttk.Button(control_frame, text="▶️ Start", command=self.toggle_simulation)
        self.start_button.grid(row=0, column=0, padx=5, pady=5)

        self.speed_var = tk.StringVar(value="x1")
        self.speed_menu = ttk.Combobox(control_frame, textvariable=self.speed_var, values=["x1", "x10", "x100"], state="readonly")
        self.speed_menu.grid(row=0, column=1, padx=5, pady=5)
        self.speed_menu.bind("<<ComboboxSelected>>", self.change_speed)

        self.year_label = ttk.Label(control_frame, text="Year: 0")
        self.year_label.grid(row=0, column=2, padx=5, pady=5)

        # Graph
        self.fig, self.ax = plt.subplots(figsize=(6, 4))
        self.ax.set_title("AI Population Over Time")
        self.ax.set_xlabel("Year")
        self.ax.set_ylabel("Population")
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().grid(row=1, column=0, padx=10, pady=5)

        # Info Panel
        info_frame = ttk.LabelFrame(root, text="Summary Info")
        info_frame.grid(row=2, column=0, sticky="ew", padx=10, pady=5)

        self.textbox = scrolledtext.ScrolledText(info_frame, wrap=tk.WORD, width=80, height=10)
        self.textbox.grid(row=0, column=0, padx=5, pady=5)

        self.update_graph()

    def toggle_simulation(self):
        self.running = not self.running
        if self.running:
            self.start_button.config(text="⏸️ Pause")
            threading.Thread(target=self.run_simulation, daemon=True).start()
        else:
            self.start_button.config(text="▶️ Start")

    def change_speed(self, event=None):
        speed_map = {"x1": 1, "x10": 0.1, "x100": 0.01}
        self.speed = speed_map.get(self.speed_var.get(), 1)

    def run_simulation(self):
        while self.running:
            summary = self.sim.step()
            year = summary["time"]
            pop = len(summary["entities"])
            self.population_data.append((year, pop))
            self.year_label.config(text=f"Year: {year}")
            self.update_graph()
            self.update_summary(summary)
            time.sleep(self.speed)

    def update_graph(self):
        years = [d[0] for d in self.population_data]
        pops = [d[1] for d in self.population_data]
        self.ax.clear()
        self.ax.plot(years, pops, marker='o')
        self.ax.set_title("AI Population Over Time")
        self.ax.set_xlabel("Year")
        self.ax.set_ylabel("Population")
        self.canvas.draw()

    def update_summary(self, summary):
        text = f"Year: {summary['time']}"
        text += f"Weather: {summary['weather']}"
        text += f"New Offspring: {', '.join(summary['new_offspring']) if summary['new_offspring'] else 'None'}"
        text += f"Total Entities: {len(summary['entities'])}"

        traits_count = {}
        for e in summary["entities"]:
            trait = e['core_trait']
            traits_count[trait] = traits_count.get(trait, 0) + 1

        text += "Core Traits:"
        for trait, count in traits_count.items():
            text += f"  - {trait}: {count}"

        self.textbox.delete("1.0", tk.END)
        self.textbox.insert(tk.END, text)

if __name__ == "__main__":
    root = tk.Tk()
    app = SimulationGUI(root)
    root.mainloop()
