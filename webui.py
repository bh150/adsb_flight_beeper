import requests
import json
import os
import subprocess

# List of specific "flight" codes to match
target_flights = ["JBU394", "UPS1016", "UAL2610 ", "JBU1302 ", "LOT5N   ", "DHK366  "]  # Add more as needed

def fetch_json_data():
    response = requests.get("http://localhost:8080/dump1090/data.json")
    return json.loads(response.text)

def check_for_matches(data):
    for flight in data:
        if flight["flight"] in target_flights:
            play_sound()
            print(flight["flight"])

def play_sound():
    # Replace with your preferred sound file
    audio_file = "beep.mp3"
    subprocess.run(["paplay", audio_file])

if __name__ == "__main__":
    while True:
        data = fetch_json_data()
        check_for_matches(data)

# I am noticing an issue where flights that are no longer detected are being stored in the json file for 300 seconds after
# they stop appearing in the localhost:8080 web window and will work to implement a way to only play a tone for a matching flight
# that have a "seen" integer of > 10 so that they do not continue to play a tone after they are far out of range of the antenna
