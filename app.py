from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        dbname="todo_app_db",
        user="postgres",
        password="Testmash123#",
        host="localhost",
        port="5432"
    )

@app.route("/", methods=["GET", "POST"])
def index():
    conn = get_db_connection()
    cur = conn.cursor()

    # INSERT (Create)
    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]

        cur.execute(
            """
            INSERT INTO todos (task_title, task_body)
            VALUES (%s, %s);
            """,
            (title, body)
        )
        conn.commit()
        cur.close()
        conn.close()
        return redirect("/")  # prevents form resubmission

    # READ
    cur.execute(
        "SELECT task_id, task_title, task_body, is_completed FROM todos ORDER BY task_id ASC;"
    )
    todos = cur.fetchall()

    cur.close()
    conn.close()

    return render_template("index.html", todos=todos)


if __name__ == "__main__":
    app.run(debug=True)

