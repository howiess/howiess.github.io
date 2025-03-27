# discover_ids.py
import os, time, requests
from dotenv import load_dotenv
import pandas as pd

load_dotenv()
API_KEY = os.getenv("API_KEY")
DISCOVER_URL = "https://api.themoviedb.org/3/discover/movie"

movie_id = []
for page in range(1, 1001):
    resp = requests.get(DISCOVER_URL, params={
        "api_key": API_KEY,
        "with_original_language": "en",
        "primary_release_date.gte": "1970-01-01",
        "sort_by": "popularity.desc",
        "page": page
    }).json()

    results = resp.get("results", [])
    if not results:
        print('Error: Could not find results')
        continue  

    movie_id.extend([m["id"] for m in resp.get("results", [])])
    print(f"Page {page}/1000 → total {len(movie_id)} movies")
    time.sleep(0.25)

df_ids = pd.DataFrame({"id": movie_id})
df_ids.to_csv('movie_id.csv', index=False)



