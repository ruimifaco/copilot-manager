
-- Exclui tabelas, se houver, para não atrapalhar os testes
DROP TABLE IF EXISTS tasks;
DROP TABLE IF EXISTS recurring_blocks;
DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS users;

-- Cria tabelas
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    user_name VARCHAR(25) NOT NULL,
    email VARCHAR(40) UNIQUE NOT NULL,
    telegram_user_id BIGINT UNIQUE
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
    is_fixed BOOLEAN NOT NULL DEFAULT TRUE,
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
    final_status VARCHAR(20) NOT NULL CHECK (final_status IN ('To Do', 'In progress', 'Completed')),
    user_id INTEGER NOT NULL REFERENCES users(id),
    category_id INTEGER NULL REFERENCES categories(id)
);



-- Usuário fictício
INSERT INTO users (user_name, email)
VALUES ('Rui', 'rui@gmail.com');

-- Categorias fictícias
INSERT INTO categories (category_name, is_anchor, user_id)
VALUES ('Sono', TRUE, 1);

INSERT INTO categories (category_name, is_anchor, user_id)
VALUES ('Treino', TRUE, 1);

INSERT INTO categories (category_name, is_anchor, user_id)
VALUES ('Limpeza', FALSE, 1);

-- Bloco recorrente
INSERT INTO recurring_blocks (title, days_of_week, start_time, end_time, is_fixed, user_id, category_id)
VALUES ('Academia', 'segunda,sexta', '18:00', '19:00', TRUE, 1, 2);

-- Tasks
-- sem categoria
INSERT INTO tasks (title, final_status, user_id, task_date)
VALUES ('Tirar título de eleitor', 'To Do', 1, '2026-05-21');

-- com categoria limpeza
INSERT INTO tasks (title, planned_start_time, final_status, user_id, category_id)
VALUES ('Lavar louça', '14:00', 'In progress', 1, 3);

-- com categoria treino
INSERT INTO tasks (title, planned_start_time, final_status, user_id, category_id, task_date)
VALUES ('Treino extra', '20:00', 'Completed', 1, 2, '2026-05-17');

-- com categoria sono
INSERT INTO tasks (title, final_status, user_id, category_id, task_date)
VALUES ('Dormir cedo', 'To Do', 1, 1, '2026-05-22');




-- Listar tasks do usuário
SELECT id, title, task_date, final_status, user_id
FROM tasks
WHERE user_id = 1
  AND final_status IN ('To Do', 'In progress')
ORDER BY planned_start_time;

-- Listar usuário principal
SELECT * FROM users WHERE id = 1;

-- Listar categorias do usuário
SELECT * FROM categories WHERE user_id = 1;

-- Listar categorias-âncoras do usuário
SELECT * FROM categories
WHERE user_id = 1
  AND is_anchor = TRUE;

-- Listar blocos recorrentes do usuário
SELECT * FROM recurring_blocks WHERE user_id = 1;

-- Listar blocos recorrentes por categoria
SELECT * FROM recurring_blocks WHERE category_id = 2;

-- Listar tasks de uma data específica
SELECT * FROM tasks WHERE task_date = '2026-05-21';

-- Listar tasks pendentes de uma data
SELECT * FROM tasks
WHERE task_date = '2026-05-22'
  AND final_status = 'To Do';

-- Listar tasks concluídas de uma data
SELECT *
FROM tasks
WHERE task_date = '2026-05-17'
  AND final_status = 'Completed';

-- Listar tasks por status
SELECT *
FROM tasks
WHERE final_status = 'To Do';

-- Listar tasks por categoria
SELECT *
FROM tasks
WHERE category_id = 1;

-- Listar tasks sem categoria
SELECT *
FROM tasks
WHERE category_id IS NULL;

-- Juntar task + categoria
SELECT
    t.id,
    t.title,
    t.task_date,
    t.final_status,
    c.category_name
FROM tasks t
LEFT JOIN categories c ON t.category_id = c.id;

-- Juntar bloco recorrente + categoria
SELECT
    rb.id,
    rb.title,
    rb.days_of_week,
    rb.start_time,
    rb.end_time,
    c.category_name
FROM recurring_blocks rb
JOIN categories c ON rb.category_id = c.id;

-- Buscar a visão diária simples
SELECT
    t.id,
    t.title,
    t.task_date,
    t.final_status,
    c.category_name
FROM tasks t
LEFT JOIN categories c ON t.category_id = c.id
WHERE t.task_date = '2026-05-17'
ORDER BY t.planned_start_time;
