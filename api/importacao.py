import sqlite3

import pandas as pd
#from custoobra.api.models import Cublista

con = sqlite3.connect("custoobra/db.sqlite3")


# Load the data into a DataFrame
dadoscub = pd.read_pickle('custoobra/cublista.pkl')
#surveys_df = pd.read_sql_query("SELECT * from cublista", con)
cursor = con.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())
dadosdb = pd.read_sql_query("SELECT * from api_cublista", con)
#dadosdb.to_pickle('dadosdb.pkl')
print(dadosdb.info())

# for indice in dadoscub.index:
#     p=Cublista(projeto=dadoscub.loc[indice]['projeto'],
#              tipo=dadoscub.loc[indice]['tipo'], 
#              padrao=dadoscub.loc[indice]['padrao'],
#              estado= dadoscub.loc[indice]['estado'],
#              mes=dadoscub.loc[indice]['mes'],
#              ano= dadoscub.loc[indice]['ano'],
#              valor=dadoscub.loc[indice]['valor'])
#     p.save()
    
    

# Select only data for 2002
#surveys2002 = surveys_df[surveys_df.year == 2002]

# Write the new DataFrame to a new SQLite table
dadoscub.to_sql("api_cublista", con, if_exists = "replace")

con.close()
