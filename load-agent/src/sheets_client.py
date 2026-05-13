import requests
import csv
import io
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from dotenv import load_dotenv
load_dotenv()

def get_drivers():
    SHEET_ID = "1LKKOJUDim9FdqHudzvVIrR9gPkbkVhkuh2aSmoDF6GQ"
    url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv"
    
    response = requests.get(url)
    content = response.text
    
    reader = csv.reader(io.StringIO(content))
    rows = list(reader)
    data_rows = rows[1:]
    
    drivers = []
    for row in data_rows:
        try:
            driver = {
                "name": row[0],
                "phone": row[1],
                "city": row[2],
                "state": row[3],
                "lat": float(row[4]) if row[4] else 0.0,
                "lon": float(row[5]) if row[5] else 0.0,
                "truck_type": row[6],
                "active": row[7] if len(row) > 7 else "yes"
            }
            drivers.append(driver)
        except Exception as e:
            print(f"Sətir xətası: {e} | {row}")
    
    return drivers