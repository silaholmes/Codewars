import requests
import json

username = "AalaaAyesh"
api_key = "https://www.codewars.com/api/v1/users/AalaaAyesh"

url = f"https://www.codewars.com/api/v1/users/{username}/code-challenges/completed"

response = requests.get(url, headers={"Authorization": f"Bearer {api_key}"})

if response.status_code == 200:
    data = response.json()

    with open("solutions.json", "w") as file:
        json.dump(data, file, indent=4)

    print("تم جلب الحلول وحفظها في solutions.json.")
else:
    print(f"خطأ: {response.status_code}, {response.text}")
