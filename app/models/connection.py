import psycopg2


def connect() -> psycopg2.extensions.connection:
    try:
        conn = psycopg2.connect(
            user='matcha',
            database='montech'
        )
    except psycopg2.OperationalError:
        print('Database is not available')
        exit(1)

    return conn


if __name__ == '__main__':
    conn = connect()
    if conn is None:
        print('Database is not available')
        exit(1)
