-- Create satellite data table
CREATE TABLE satellite_data (
    satellite_name TEXT,
    tle_line1 TEXT,
    tle_line2 TEXT
);

-- Create debris data table
CREATE TABLE debris_data (
    debris_id TEXT,
    x_position REAL,
    y_position REAL,
    z_position REAL,
    velocity_km_s REAL
);
