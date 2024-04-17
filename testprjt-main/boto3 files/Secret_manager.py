import boto3
import json

client = boto3.client('secretsmanager')

def createSecret():
    response = client.create_secret(
        Name='Teststr1',
        SecretString='{"username": "root", "password": "employee123"}'
    )
    return response

#createresp = createSecret()
#print(createresp)

response = client.get_secret_value(
  SecretId='Teststr1'
   )
database_secrets = json.loads(response['SecretString'])
User = database_secrets['username']
    
response = client.get_secret_value(
    SecretId='Teststr1'
    )
database_secrets = json.loads(response['SecretString'])
pwd = database_secrets['password']
 

print(User)
print(pwd)

