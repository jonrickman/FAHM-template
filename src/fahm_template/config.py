# TODO: There was not much rejoicing
MONGO_USER = "admin"
MONGO_PASSWORD = "pass"
MONGO_PORT = 27017
MONGO_URL = "localhost"
MONGO_DB = "yt"

MONGODB_URL = f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_URL}/{MONGO_DB}?retryWrites=true&w=majority"

API_PROTOCOL = "http"
API_BASE = "localhost"
API_PORT = 8000
API_URL = f"{API_PROTOCOL}://{API_BASE}:{API_PORT}"
