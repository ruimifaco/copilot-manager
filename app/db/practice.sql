CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    user_name VARCHAR(25) NOT NULL,
    email VARCHAR(40) UNIQUE NOT NULL
);

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    category_name VARCHAR(25) NOT NULL,
    is_anchor BOOLEAN NOT NULL DEFAULT FALSE,
    user_id INTEGER NOT NULL REFERENCES users(id)  
);

CREATE TABLE recurring_blocks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(25) NOT NULL,
    days_of_week TEXT NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    is_fixed BOOLEAN NOT NULL,
    user_id INTEGER NOT NULL REFERENCES users(id),
    category_id INTEGER NOT NULL REFERENCES categories(id)
);

CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(40) NOT NULL,
    task_date DATE NULL,
    planned_start_time TIME,
    planned_end_time TIME,
    actual_start_time TIME,
    actual_end_time TIME,
    final_status VARCHAR(20) NOT NULL CHECK (final_status IN ('pendente', 'em andamento', 'concluída')),
    user_id INTEGER NOT NULL REFERENCES users(id),
    category_id INTEGER NULL REFERENCES categories(id)
);