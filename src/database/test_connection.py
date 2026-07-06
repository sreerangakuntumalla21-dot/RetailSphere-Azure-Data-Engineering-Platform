from db_connection import get_connection

conn = get_connection()

if conn:
    print("✅ PostgreSQL connection successful!")
    conn.close()