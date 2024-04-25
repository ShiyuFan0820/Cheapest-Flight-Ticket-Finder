# Data Manager

I already created a spreadsheet in Google Sheets and filled in the city where I want to search for the flight in the spreadsheet.

<div align=center>
<img width="351" alt="image" src="https://github.com/ShiyuFan0820/CSLearningNote/assets/149340606/ed9d5f17-f992-4e16-9653-1f0877b7b195">
</div>

This Data Manager class is responsible for getting and updating information in the Google Sheet with Sheety API.

**Step 1. Getting city data in the Google Sheet by using Sheety.**

After getting data by using Sheet API, notice that if the content of one column is empty, it won't return any result, so if the initial `IATA Code` column is empty when we get the data and print the result, it won't contain any value relates to `IATA Code` like this:

<div align=center>
<img width="500" alt="image" src="https://github.com/ShiyuFan0820/CheapestFlightTicketFinder/assets/149340606/22e7c7f6-f95f-416c-95a6-88028420bbec">
</div>

**Step 2. Updating city data to the Google Sheet by using Sheety.**

Use `request.put` to add content to the row, use `id` to indicate which row of values to modify.

**Step 3. Write a similar method to update the cheapest flight information.**
