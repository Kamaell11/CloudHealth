from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Configuration settings
settings = {
    'host': os.getenv('COSMOS_URL', 'https://default-url.com'),
    'master_key': os.getenv('COSMOS_KEY', 'default_master_key'),
    'database_id': os.getenv('COSMOS_DATABASE', 'default_db'),
    'container_id': os.getenv('COSMOS_CONTAINER', 'default_container'),
}