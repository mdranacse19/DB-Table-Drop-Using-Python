import psycopg2

# establishing the connection
conn = psycopg2.connect(
    database="robi_ums", user='postgres', password='Asdf@1234', host='10.101.74.236', port='5432'
    # database="AAAA", user='postgres', password='12345678', host='localhost', port='5432'
)

# Setting auto commit false
conn.autocommit = True

# Creating a cursor object using the cursor() method
cursor = conn.cursor()
# Doping EMPLOYEE table if already exists
# query = cursor.execute("SELECT * FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema'")
query = cursor.execute("DROP SCHEMA public CASCADE")
query = cursor.execute("CREATE SCHEMA public")
# print(query)

# Commit your changes in the database
conn.commit()

# Closing the connection
conn.close()
