import requests
import csv
import io
import os
from dotenv import load_dotenv

load_dotenv()

SHEET_ID = os.environ.get("GOOGLE_SHEET_ID")
url = f"https://docs.google.com/spreadsheets/d/1LKKOJUDim9FdqHudzvVIrR9gPkbkVhkuh2aSmoDF6GQ/export?format=csv"
response = requests.get(url)
content = response.text

reader = csv.reader(io.StringIO(content))

rows = list(reader)
header = rows[0]
data_rows = rows[1:]

drivers = []
for row in data_rows: 
    driver = {
          "name" : row[0],
          "phone": row[1],
          "city" : row[2],
          "state" : row[3],
          "lat" : row[4],
          "lon" : row[5],
          "truck_type" : row[6],
          "active" : row[7]
}
    drivers.append(driver)

for driver in drivers:
    print(f"{driver['name']} - {driver['city']}, {driver['state']} — {driver['truck_type']}")
