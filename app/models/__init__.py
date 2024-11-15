from .connection import connect

create_blog_table_query = '''
    CREATE TABLE IF NOT EXISTS blogs (
        id SERIAL PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        content TEXT NOT NULL,
        category VARCHAR(255),
        tags TEXT[],
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP
    );
'''

conn = connect()
with conn.cursor() as cursor:
    cursor.execute(create_blog_table_query)
    conn.commit()
