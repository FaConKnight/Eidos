
import csv
import os

LOG_FILE = "eidos_individuals.csv"

def export_population(year, entities):
    write_header = not os.path.exists(LOG_FILE)
    with open(LOG_FILE, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(["year", "name", "age", "trait", "location", "belief", "economic_status"])
        for e in entities:
            writer.writerow([
                year,
                e.name,
                e.age,
                e.traits,
                getattr(e, 'location', 'Unknown'),
                getattr(e, 'belief', 'None'),
                getattr(e, 'economic_status', 'Neutral')
            ])
