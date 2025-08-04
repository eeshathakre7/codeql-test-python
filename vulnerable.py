import sqlite3

def get_user_info(user_input):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    # 🚨 Vulnerable to SQL Injection
    query = f"SELECT * FROM users WHERE email = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

# Sample call
get_user_info("admin@example.com")

