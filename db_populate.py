import pyodbc

driver = '{ODBC Driver 17 for SQL Server}'
server = 'localhost' 
database = 'POKEMON_URL' 

con_string = f'DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
conn = pyodbc.connect(con_string)

