
import boto3
import json
import mysql.connector

client = boto3.client('secretsmanager', region_name='us-east-1')

response = client.get_secret_value(
  SecretId='Teststr1'
   )
database_secrets = json.loads(response['SecretString'])
username = database_secrets['username']
    
response = client.get_secret_value(
    SecretId='Teststr1'
    )
database_secrets = json.loads(response['SecretString'])
password = database_secrets['password']

client = boto3.client('rds')
"""
response = client.create_db_instance(
        AllocatedStorage=10,
        DBInstanceIdentifier='empDB',
        DBInstanceClass="db.t2.micro",
        Engine="mysql",
        MasterUsername=username,
        MasterUserPassword=password,
        Port=3306
)

print (response)
"""

db_conn = mysql.connector.connect(
    host='empdb.cjqjmoxodmld.us-east-1.rds.amazonaws.com',
    port=3306,
    user=username,
    password=password,
    database='empDB',
)

cursor=db_conn.cursor()

#create_db_command = "CREATE DATABASE empDB;"

# Execute the SQL command to create the database
#cursor.execute(create_db_command)

create_table = """
CREATE TABLE Emp (
  emp_id VARCHAR(255) PRIMARY KEY,
  first_name VARCHAR(255),
 last_name VARCHAR(255),
  pri_skill VARCHAR(255),
  Department VARCHAR(255)
)"""

# Execute the SQL command to create the table
cursor.execute(create_table)

# Commit the changes
db_conn.commit()

# Close the cursor and connection
cursor.close()
db_conn.close() 