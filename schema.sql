
CREATE TABLE Vehicle (
    VehicleID INTEGER PRIMARY KEY AUTOINCREMENT,
    VIN TEXT UNIQUE NOT NULL,
    WaymoID TEXT UNIQUE,
    Model TEXT,
    Year INTEGER,
    Mileage INTEGER,
    Status TEXT
);

CREATE TABLE Workshop (
    WorkshopID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT,
    Location TEXT,
    Capacity INTEGER
);

CREATE TABLE Technician (
    TechnicianID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT,
    Role TEXT,
    CertificationLevel TEXT
);

CREATE TABLE MaintenanceRecord (
    MaintenanceID INTEGER PRIMARY KEY AUTOINCREMENT,
    VehicleID INTEGER,
    WorkshopID INTEGER,
    TechnicianID INTEGER,
    DateIn DATETIME,
    DateOut DATETIME,
    Odometer INTEGER,
    Issue TEXT,
    Resolution TEXT,
    Cost REAL,
    FOREIGN KEY (VehicleID) REFERENCES Vehicle(VehicleID),
    FOREIGN KEY (WorkshopID) REFERENCES Workshop(WorkshopID),
    FOREIGN KEY (TechnicianID) REFERENCES Technician(TechnicianID)
);
