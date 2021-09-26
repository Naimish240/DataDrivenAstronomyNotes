import psycopg2

def select_all(table):
  conn = psycopg2.connect(dbname='db', user='grok')
  cursor = conn.cursor()
  cursor.execute(f'SELECT * FROM {table};')
  records = cursor.fetchall()
  return records