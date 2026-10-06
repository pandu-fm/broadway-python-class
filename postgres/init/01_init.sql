CREATE TABLE IF NOT EXISTS students (
    id         SERIAL PRIMARY KEY,
    name       VARCHAR(100) NOT NULL,
    email      VARCHAR(150) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO students (name, email) VALUES
    ('Ram', 'ram@example.com'),
    ('Sita', 'sita@example.com')
ON CONFLICT (email) DO NOTHING;
