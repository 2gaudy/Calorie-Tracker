import requests
from datetime import datetime

APP_ID = "4f3406cd"
API_KEY = "4a36817c0933073139a73fc712b15759"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

exercise_params = {
    "query": input("Tell me what exercises you did: "),
    "gender": "male",
    "weight_kg": 115.2,
    "height_cm": 188.976,
    "age": 21
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

sheety_endpoint = "https://api.sheety.co/0fb28b01142c17aa77e816af0f36d0c8/austin'sWorkouts/workouts"

response = requests.post(url=exercise_endpoint, headers=headers, json=exercise_params)
response.raise_for_status()
workout = response.json()

today = datetime.now()

todays_date = f"{today.strftime('%d')}/{today.strftime('%m')}/{today.strftime('%Y')}"
current_time = today.strftime('%X')
exercise_type = workout['exercises'][0]['name']
exercise_duration = f"{workout['exercises'][0]['duration_min']} minutes"
exercise_calories = workout['exercises'][0]['nf_calories']

print(todays_date)
print(current_time)
print(exercise_type)
print(exercise_calories)
print(exercise_duration)

sheety_auth = {
    "Authorization": "Basic bnVsbDpudWxs"
}


for exercise in workout['exercises']:
    sheety_add_row = {
         "workout": {
                "date": todays_date,
                "time": current_time,
                "exercise": workout['exercises'][0]['name'].title(),
                "duration": workout['exercises'][0]['duration_min'],
                "calories": workout['exercises'][0]['nf_calories']
         }
    }

    sheety_update = requests.post(url=sheety_endpoint, json=sheety_add_row, headers=sheety_auth)
    sheety_update.raise_for_status()
    print(sheety_update.text)


