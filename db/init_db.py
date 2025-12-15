import psycopg2

conn = psycopg2.connect(
    dbname="todo_app_db",
    user="postgres",
    password="Testmash123#",
    host="localhost",
    port="5432"
)

print("Connected to the database successfully!")

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS todos (
        task_id SERIAL PRIMARY KEY,
        task_title TEXT NOT NULL,
        task_body TEXT NOT NULL,
        is_completed BOOLEAN DEFAULT FALSE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
""")

conn.commit()
  
print("Table created successfully!")

cur.close()
conn.close()

