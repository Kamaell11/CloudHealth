from azure.cosmos import CosmosClient
import config

# Retrieve Cosmos DB URL and Key from config
HOST = config.settings['host']
MASTER_KEY = config.settings['master_key']
DATABASE_ID = config.settings['database_id']
CONTAINER_ID = config.settings['container_id']

# Check if the required environment variables are set
if not HOST or not MASTER_KEY:
    raise ValueError("Missing required environment variables.")

print(f"COSMOS_URL: {HOST}")
print(f"COSMOS_KEY: {MASTER_KEY}")

# Connect to Cosmos DB
client = CosmosClient(HOST, credential=MASTER_KEY)

# Create database if it does not exist
database = client.create_database_if_not_exists(DATABASE_ID)

# Create containers (collections) in Cosmos DB
users_container = database.create_container_if_not_exists(
    id="Users",
    partition_key={"paths": ["/id"], "kind": "Hash"}
)

health_container = database.create_container_if_not_exists(
    id="HealthMetrics",
    partition_key={"paths": ["/user_id"], "kind": "Hash"}
)

activities_container = database.create_container_if_not_exists(
    id="Activities",
    partition_key={"paths": ["/user_id"], "kind": "Hash"}
)
