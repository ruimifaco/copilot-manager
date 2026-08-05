

get_category_sql = "SELECT id, category_name, is_anchor, user_id FROM categories ORDER BY id;"
get_tasks_sql = "SELECT id, title, task_date, planned_start_time, planned_end_time, actual_start_time, actual_end_time, final_status, user_id, category_id FROM tasks ORDER BY id;"
get_recurring_blocks_sql = "SELECT title, days_of_week, start_time, end_time, is_fixed, user_id, category_id FROM recurring_blocks ORDER BY id;"

get_category_by_id_sql = "SELECT id, category_name, is_anchor, user_id FROM categories WHERE id = :id_searched;"
get_task_by_id_sql = "SELECT id, title, task_date, planned_start_time, planned_end_time, actual_start_time, actual_end_time, final_status, user_id, category_id FROM tasks WHERE id = :id_searched;"
get_recurring_block_by_id_sql = "SELECT id, title, days_of_week, start_time, end_time, is_fixed, user_id, category_id FROM recurring_blocks WHERE id = :id_searched;"

post_category_sql = "INSERT INTO categories (category_name, is_anchor, user_id) VALUES (:category_name, :is_anchor, :user_id) RETURNING id, category_name, is_anchor, user_id;"
post_task_sql = "INSERT INTO tasks (title, task_date, planned_start_time, planned_end_time, actual_start_time, actual_end_time, final_status, user_id, category_id) VALUES (:title, :task_date, :planned_start_time, :planned_end_time, :actual_start_time, :actual_end_time, :final_status, :user_id, :category_id) RETURNING id, title, task_date, planned_start_time, planned_end_time, actual_start_time, actual_end_time, final_status, user_id, category_id;"
post_recurring_block_sql = "INSERT INTO recurring_blocks (title, days_of_week, start_time, end_time, is_fixed, user_id, category_id) VALUES (:title, :days_of_week, :start_time, :end_time, :is_fixed, :user_id, :category_id) RETURNING id, title, days_of_week, start_time, end_time, is_fixed, user_id, category_id;"
