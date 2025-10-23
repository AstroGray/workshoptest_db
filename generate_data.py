import sqlite3
import random
from datetime import datetime, timedelta

# Connect to your database
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# Define ranges and options based on your schema (adjust IDs to match your data)
workshop_ids = [1, 2]  # e.g., from Workshop table
technician_ids = [1, 2, 3]  # e.g., from Technician table
vehicle_ids = [1, 2, 3]  # e.g., from Vehicle table

issues = ['Routine Checkup', 'Battery Health Inspection', 'Autonomous System Fault', 'Tire Replacement', 'Software Update']
resolutions = ['No issues found', 'Replaced battery module', 'Repaired Lidar sensor', 'Replaced tires', 'Updated firmware']

# Generate 10 random records
num_records = 20
for _ in range(num_records):
    vehicle_id = random.choice(vehicle_ids)
    workshop_id = random.choice(workshop_ids)
    technician_id = random.choice(technician_ids)
    
    # Random date in 2025 (adjust range as needed)
    start_date = datetime(2025, 1, 1)
    random_days = random.randint(0, 300)  # Up to ~10 months
    date_in = (start_date + timedelta(days=random_days)).strftime('%Y-%m-%d')
    date_out = (datetime.strptime(date_in, '%Y-%m-%d') + timedelta(days=random.randint(1, 3))).strftime('%Y-%m-%d')
    
    odometer = random.randint(1000, 50000)  # Random mileage
    issue = random.choice(issues)
    resolution = random.choice(resolutions)
    cost = round(random.uniform(50.0, 2500.0), 2)  # Random cost between $50 and $2500
    
    # Insert the record
    sql = """
    INSERT INTO MaintenanceRecord 
    (VehicleID, WorkshopID, TechnicianID, DateIn, DateOut, Odometer, Issue, Resolution, Cost) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
    """
    cursor.execute(sql, (vehicle_id, workshop_id, technician_id, date_in, date_out, odometer, issue, resolution, cost))

# Commit changes and close
conn.commit()
conn.close()

print(f"Inserted {num_records} random records into MaintenanceRecord.")
