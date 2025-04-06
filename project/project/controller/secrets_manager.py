import boto3
from aws_secretsmanager_caching import SecretCache, SecretCacheConfig 
import json

class SecretsManager:
    def __init__(self):
        secret_name = "rds!cluster-0e02b8cf-44a6-4cd8-8c58-26706dcba261"
        region_name = "us-east-1"

        session = boto3.session.Session()
        client = session.client(
            service_name='secretsmanager',
            region_name=region_name,
        )

        cache_config = SecretCacheConfig()
        cache = SecretCache(config=cache_config, client=client)

        inline_keys_values= cache.get_secret_string(secret_name)
        self.secret = json.loads(inline_keys_values)

    def get_secret(self, secret_key):
        return self.secret[secret_key]

