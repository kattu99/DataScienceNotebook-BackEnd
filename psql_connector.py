import psycopg2

def connect_to_db(database, user, password, host, port):
    engine = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="narnaul1",
        host="database-2.c7schjdjwua9.us-east-2.rds.amazonaws.com",
        port='5432'
    )
    return engine

def get_all_tables(engine): 
    cur = engine.cursor()
    cur.execute("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';")
    resp = cur.fetchall()
    for table in resp: 
        table_name = table[0]
        cur.execute("select COLUMN_NAME, DATA_TYPE from INFORMATION_SCHEMA.columns where table_name='{table}'".format(table=table_name))
        resp = cur.fetchall()
        print(resp)

def get_rows_columns(engine, rows, columns): 


engine = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="narnaul1",
        host="database-2.c7schjdjwua9.us-east-2.rds.amazonaws.com",
        port='5432'
    )
