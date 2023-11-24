-- Create the departments table
CREATE TABLE departments (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Create the positions table
CREATE TABLE positions (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL
);

-- Create the locations table
CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Create the statuses table
CREATE TABLE statuses (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Create the employees table with foreign keys
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    contact_info VARCHAR(255) UNIQUE NOT NULL,
    department_id INT,
    position_id INT,
    location_id INT,
    status_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(id),
    FOREIGN KEY (position_id) REFERENCES positions(id),
    FOREIGN KEY (location_id) REFERENCES locations(id),
    FOREIGN KEY (status_id) REFERENCES statuses(id)
);

-- Insert data into the departments table
INSERT INTO departments (name)
VALUES
    ('HR'),
    ('Sales'),
    ('IT'),
    ('asd');

-- Insert data into the positions table
INSERT INTO positions (title)
VALUES
    ('Manager'),
    ('Sales Representative'),
    ('Software Engineer'),
    ('Assistant Manager');

-- Insert data into the locations table
INSERT INTO locations (name)
VALUES
    ('New York'),
    ('Los Angeles'),
    ('San Francisco'),
    ('Singapore');

-- Insert data into the statuses table
INSERT INTO statuses (name)
VALUES
    ('Active'),
    ('Not Started'),
    ('Terminated');

-- Insert data into the employees table
INSERT INTO employees (first_name, last_name, contact_info, department_id, position_id, location_id, status_id)
VALUES
    ('John', 'Doe', 'john@example.com', 1, 1, 1, 1),
    ('Jane', 'Smith', 'jane@example.com', 2, 2, 2, 1),
    ('Alice', 'Johnson', 'alice@example.com', 3, 3, 3, 2),
    ('OO5Test', '005', 'email@example.com', 4, 4, 4, 3);
