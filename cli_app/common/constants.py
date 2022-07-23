from decouple import config

API_KEY = config('SPLIT_API_KEY')
WORKSPACE = config('WORKSPACE')

SPLIT_BASE_URI = "https://api.split.io/internal/api/v2"
BASE_HEADERS = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {API_KEY}"
}