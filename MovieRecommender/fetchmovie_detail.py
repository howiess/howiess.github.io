import os, time, requests
from dotenv import load_dotenv
import pandas as pd
import json

load_dotenv()
API_KEY = os.getenv("API_KEY")
DETAIL_URL = "https://api.themoviedb.org/3/movie/{}"

df_ids = pd.read_csv('movie_id.csv')

with open("movies_raw.ndjson", "a", encoding="utf-8") as fout:
    for idx, mid in enumerate(df_ids["id"], start=1):
        resp = requests.get(DETAIL_URL.format(mid), params={
        "api_key": API_KEY,
        "append_to_response": "credits.cast,keywords,similar,recommendations,release_dates"
    }).json()
        fout.write(json.dumps(resp) + "\n")  # write one JSON object per line

        if idx % 100 == 0:
            print(f"Fetched {idx}/{len(df_ids)} movies")
        time.sleep(0.25)

print("Done — saved NDJSON for all movies.")