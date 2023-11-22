CREATE TABLE employees (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    contact_info VARCHAR(255) UNIQUE NOT NULL,
    department VARCHAR(255),
    position VARCHAR(255),
    location VARCHAR(255),
    status VARCHAR(255)
);

 
INSERT INTO employees (first_name, last_name, contact_info, department, position, location, status)
VALUES
    ('John', 'Doe', 'john@example.com', 'HR', 'Manager', 'New York', 'Active'),
    ('Jane', 'Smith', 'jane@example.com', 'Sales', 'Sales Representative', 'Los Angeles', 'Active'),
    ('Alice', 'Johnson', 'alice@example.com', 'IT', 'Software Engineer', 'San Francisco', 'Inactive'),
    ('OO5Test', '005', 'email@example.com', 'asd', 'Assistant Manager', 'Singapore', 'ACTIVE');
