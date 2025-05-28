
import tkinter as tk
from tkinter import ttk
import threading
import time
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class EidosController:
    def __init__(self, update_callback):
        self.running = False
        self.speed = 1  # 1x = ปกติ
        self.update_callback = update_callback

    def start(self):
        if not self.running:
            self.running = True
            threading.Thread(target=self.run).start()

    def stop(self):
        self.running = False

    def set_speed(self, multiplier):
        self.speed = multiplier

    def run(self):
        while self.running:
            self.update_callback()
            time.sleep(1.0 / self.speed)

class EidosGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Eidos Observer Dashboard")

        self.controller = EidosController(self.update_display)

        control_frame = ttk.Frame(root)
        control_frame.pack(pady=10)

        ttk.Button(control_frame, text="▶ Start", command=self.controller.start).grid(row=0, column=0, padx=5)
        ttk.Button(control_frame, text="⏸ Pause", command=self.controller.stop).grid(row=0, column=1, padx=5)
        ttk.Button(control_frame, text="⏩ x10", command=lambda: self.controller.set_speed(10)).grid(row=0, column=2, padx=5)
        ttk.Button(control_frame, text="⏩ x100", command=lambda: self.controller.set_speed(100)).grid(row=0, column=3, padx=5)

        self.status_label = ttk.Label(root, text="System Idle")
        self.status_label.pack()

        self.figure = plt.Figure(figsize=(9, 5), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.chart = FigureCanvasTkAgg(self.figure, root)
        self.chart.get_tk_widget().pack()

        self.last_count = -1

    def update_display(self):
        try:
            df = pd.read_csv("eidos_individuals.csv")
            if df.empty:
                self.status_label.config(text="No data available.")
                return

            year_counts = df.groupby("year").size()
            current_year = year_counts.index.max()
            current_count = year_counts.loc[current_year]

            if self.last_count != current_count:
                self.status_label.config(text=f"Year: {current_year} | Population: {current_count}")
                self.last_count = current_count

            self.ax.clear()
            year_counts.plot(ax=self.ax, title="AI Population Over Time")
            self.ax.set_xlabel("Year")
            self.ax.set_ylabel("Population")
            self.chart.draw()

        except Exception as e:
            self.status_label.config(text=f"Error: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    gui = EidosGUI(root)
    root.mainloop()
