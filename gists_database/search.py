from .models import Gist
from datetime import datetime, date
import sqlite3

db_conn = conn = sqlite3.connect('tests/populated_gists_database.db')
def search_gists(db_conn, **kwargs):
   cursor = db_conn.cursor()
   if len(kwargs) == 0:
       q = '''SELECT * FROM gists'''
   else:
       for key, val in kwargs.items():
           if key == 'created_at':
               val_1 = datetime.strftime(val, '%Y-%m-%dT%H:%M:%SZ')
           else:
               val_1 = val
               
           q = '''SELECT * FROM gists
                   WHERE {var_1} = '{val_1}'
               '''.format(var_1 = key, 
                          val_1 = val_1
                         )
   print(q)
   cursor.execute(q)
   gists = cursor.fetchall()
   print(type(gists))
   print(len(gists))
   result = []
   for row in gists:
       result.append(Gist(row))
       print(result)
   return result
