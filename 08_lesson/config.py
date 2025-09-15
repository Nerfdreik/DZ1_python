BASE_URL = "https://yougile.com/api-v2"

API_TOKEN = os.getenv("YOUGILE_API_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}
