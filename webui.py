import requests
import json
import os
import subprocess

# List of specific "flight" codes to match
# This list is not normalized and requires the text to match exactly as shown in the json file which adds whitespace until it is exactly 8 characters long
target_flights = ["JBU394", "UPS1016", "UAL2610 ", "JBU1302 ", "LOT5N   ", "DHK366  ", "JBU1236 ", "JBU612  ", "UAL134  "]  # Add more as needed


def fetch_json_data():
    response = requests.get("http://localhost:8080/dump1090/data.json")
#    print(response)
    return json.loads(response.text)

# This function is checking for flights that are in the above list and prints the flight being detected into the terminal along with its seen time
# seen is a integer that counts the seconds since the last time dump1090 has detected the aircraft. This script will beep until the aircraft has been lost from detection for 10 seconds
def check_for_matches(data):
    for flight in data:
        if flight["flight"] in target_flights and flight["seen"] < 10:
            play_sound()
            print(flight["flight"])
            print(flight["seen"])

def play_sound():
    # Replace with your preferred sound file
    audio_file = "beep.mp3"
    # This line will vary based on your current setup and is passing a command to the operating system to play an audio file that I have included as beep.mp3
    # Currently set to work on linux with pulseaudio
    subprocess.run(["paplay", audio_file])

if __name__ == "__main__":
    while True:
        data = fetch_json_data()
        check_for_matches(data)
