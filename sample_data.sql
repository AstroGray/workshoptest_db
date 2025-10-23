-- INSERT INTO Vehicle (VIN, WaymoID, Model, Year, Mileage, Status)
-- VALUES ('7ABC1234XYZ999', 'WAYMO001', 'Electric SUV', 2025, 1200, 'Active');

-- SELECT * FROM Vehicle;

-- Sample Vehicle Data
INSERT INTO Vehicle (VIN, WaymoID, Model, Year, Mileage, Status)
VALUES
  ('1ABC234DMN965421', 'WAYMO002', 'Electric Sedan', 2024, 5050, 'Active'),
  ('2DEF456OPQ874321', 'WAYMO003', 'Electric SUV', 2025, 1200, 'Active'),
  ('3GHI789TUV132547', 'WAYMO004', 'Electric Van', 2023, 30000, 'Needs Maintenance');

-- Sample Workshop Data
INSERT INTO Workshop (Name, Location, Capacity)
VALUES
  ('East Valley Service', 'Phoenix, AZ', 15),
  ('Downtown Service Hub', 'Tempe, AZ', 12);

-- Sample Technician Data
INSERT INTO Technician (Name, Role, CertificationLevel)
VALUES
  ('Alex Kim', 'Lead Tech', 'Master'),
  ('Jordan Casey', 'Diagnostic Specialist', 'Advanced'),
  ('Bailey Smith', 'Battery Tech', 'Basic');

-- Sample MaintenanceRecord Data
INSERT INTO MaintenanceRecord (
    VehicleID, WorkshopID, TechnicianID, DateIn, DateOut, Odometer,
    Issue, Resolution, Cost
)
VALUES
  (1, 1, 1, '2025-10-21', '2025-10-21', 5050,
   'Routine Checkup', 'No issues found', 150.00),
  (2, 2, 2, '2025-10-19', '2025-10-19', 1200,
   'Battery Health Inspection', 'Replaced battery module', 1100.00),
  (3, 1, 3, '2025-10-15', '2025-10-16', 30000,
   'Autonomous System Fault', 'Repaired Lidar sensor', 2200.00);