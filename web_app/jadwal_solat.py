import requests
from bs4 import BeautifulSoup
from datetime import datetime

PRAYER_NAMES=["Subuh","Zuhur","Ashar","Maghrib","Isya"]

def get_prayer_times(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the prayer time table
        prayer_times_table = soup.find('table', class_='prayer-times')

        if prayer_times_table:
            # Extract the current date
            current_date = datetime.now().strftime('%a %-d %b')

            # Extract the prayer times for today
            today_prayer_times = []
            rows = prayer_times_table.find_all('tr')
            for row in rows:
                columns = row.find_all('td')
                prayer_time = [column.text.strip() for column in columns]
                if len(prayer_time) == 7 and prayer_time[0] == current_date:  # Filter by current date
                    today_prayer_times.append(prayer_time)

            return today_prayer_times
        else:
            return "Prayer times not found on the webpage."
    else:
        return "Failed to retrieve data. Check your internet connection or URL."

def convert_to_sec(time):
    hr, min = time.split(":")
    secs = 3600 * int(hr) + 60*int(min)
    return secs

def different_time(today_prayer_times,current_time):
    try:    
        time_index = None
        for i, prayer_time in enumerate(today_prayer_times[0][1:]):
            time_difference = (convert_to_sec(prayer_time) - convert_to_sec(current_time))
            if time_difference > 0:
                time_index = i
                break

        # Calculate time remaining until the closest prayer time
        hours, remainder = divmod(time_difference, 3600)
        minutes, seconds = divmod(remainder, 60)

        print(f"Today's date: {today_prayer_times[0][0]}.\nClosest time to next prayer is {PRAYER_NAMES[time_index]} on {prayer_time}.\nYou have {int(hours)} hours {int(minutes)} minutes left.")
    except:
        print("It's Isya time. You can check next prayer time tomorrow.")

# Example usage
if __name__ == "__main__":
    url = "https://www.muslimpro.com/en/find?country_code=ID&country_name=Indonesia&city_name=Cibinong&coordinates=-6.4901067,106.8306951"
    current_time = datetime.now().strftime('%H:%M')
    today_prayer_times = get_prayer_times(url)
    del today_prayer_times[0][2]
    if isinstance(today_prayer_times, list):
        print("Today's Prayer Times:")
        for i in range(len(today_prayer_times[0][1:])):
            for prayer_time in today_prayer_times:
                print(PRAYER_NAMES[i] + ": " + prayer_time[i+1])

        print("\n")
        different_time(today_prayer_times,current_time)
    else:
        print(today_prayer_times)
