import os
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import logging

#Delete in production
#from dotenv import load_dotenv
#load_dotenv()

key_vault_uri = os.getenv("KEYVAULT_URI")

#Azure auth
credential = DefaultAzureCredential()

#Create client key vautl
client = SecretClient(vault_url=key_vault_uri, credential=credential)

#Method that request secret
def get_secret(name_secret: str) -> str:
    try:
        return client.get_secret(name_secret).value
    except Exception as ex:
        logging.error("ERROR GET SECRET {%s}", ex)