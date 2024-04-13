# Data Manager

I already created a spreadsheet in Google Sheets and filled in the city where I want to search for the flight in the spreadsheet.

<div align=center>
<img width="351" alt="image" src="https://github.com/ShiyuFan0820/CSLearningNote/assets/149340606/ed9d5f17-f992-4e16-9653-1f0877b7b195">
</div>

This Data Manager class is responsible for getting and updating information in the Google Sheets with Sheety API.

**Step 1. Getting city data in the Google Sheets by using Sheety.**

```py
import requests

sheety_endpoint = "https://api.sheety.co/596407487435113fa1b524e86a87b95d/flightDeal/prices"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    ## Define a method to get the city names from the Google Sheet.
    @classmethod
    def GetCityInfo(cls):
        response = requests.get(sheety_endpoint)
        city_info = response.json()
        return city_info
```

