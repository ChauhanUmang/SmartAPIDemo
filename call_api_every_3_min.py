import requests
import time
from datetime import datetime, timedelta

# Successfully tested for calling the API every 3rd minute.
# Just put the starting time as the time when we want to send the first API request.
# Have also tested it for the scenario where api call and processing request take some time by adding sleep time of 20s.

# Set the start time and end time for API calls
start_time = datetime.now().replace(hour=9, minute=15, second=0, microsecond=5)
end_time = datetime.now().replace(hour=15, minute=30, second=0, microsecond=0)

# Define the time interval for API calls (3 minutes)
interval = timedelta(minutes=3)

# Calculate the initial delay until the next scheduled API call
current_time = datetime.now()
next_call_time = start_time
if current_time < next_call_time:
    initial_delay = (next_call_time - current_time).total_seconds()
    time.sleep(initial_delay)

# Main loop for making API calls
while datetime.now() < end_time:
    if datetime.now() >= next_call_time:
        # Make the API call here
        print(f"API CALL IS MADE AT: {datetime.now()}")
        time.sleep(20)
        # response = requests.get('https://api.example.com')

        # Process the response
        # ...

        # Calculate the elapsed time since the start of the interval
        elapsed_time = (datetime.now() - next_call_time).total_seconds()

        # Adjust the next call time based on the elapsed time
        next_call_time += interval

        # Calculate the remaining time until the next interval
        remaining_time = (next_call_time - datetime.now()).total_seconds()

        # If the remaining time is greater than the elapsed time,
        # subtract the elapsed time from the remaining time
        if remaining_time > elapsed_time:
            time.sleep(remaining_time - elapsed_time)

print("API calls completed.")
