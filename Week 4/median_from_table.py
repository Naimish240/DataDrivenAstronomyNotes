import psycopg2
import numpy as np

def column_stats(table, column):
  conn = psycopg2.connect(dbname='db', user='grok')
  cursor = conn.cursor()
  cursor.execute(f'SELECT {column} FROM {table};')
  records = cursor.fetchall()
  data = np.array(records)
  return np.mean(data), np.median(data)

if __name__ == '__main__':
  print(column_stats('Star', 't_eff'))