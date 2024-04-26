# Cheapest Flight Ticket Finder

This project aims to use related API to find the cheapest flight ticket from one location to another from tomorrow of the current date to 3 months later, and format the result in a Spreadsheet.

## Example

Suppose we want to find the cheapest flights from London to other cities within 3 months:

[<img width="500" alt="image" src="https://github.com/ShiyuFan0820/CheapestFlightTicketFinder/assets/149340606/132f5c3b-dc2f-42af-97a8-e847c1dd3317">](https://youtu.be/3JmRTRkgSH0)


## Instructions for Use 

1. [Flight Deal Google Sheet](https://docs.google.com/spreadsheets/d/1ccQtFQE5aoiHjkyCRJJ4hPTghZLmrfm4bqOYlNipnrM/edit#gid=0), open this link, create your own Google Sheet acount and make your own copy of the starting Google Sheet, I already fill in some city names, you can change them to the city that you want to go. It should be noted that the `IATA Code` in the spreadsheet is **International Air Transport Association** code, which is a three-letter code assigned to the airport around the world, These codes are used for airline ticketing, flight planning, and baggage handling. They provide a standardized way to identify airports globally. But a city can have multiple airports, and here, I will only collect the city code, not the airport code.
2. Sign up to these API websites, you will use them in the code later.
- [Google Sheet Data Management -- Sheety API](https://sheety.co/)
- [Tequila Flight Search API Documentation](https://tequila.kiwi.com/portal/docs/tequila_api)
3. Sheety API
- Create a free account for Sheety API, and sign in with your Google Sheet account. Don't forget to open the access when signing in to your account.

<div align=center>
<img width="500" alt="image" src="https://github.com/ShiyuFan0820/CheapestFlightTicketFinder/assets/149340606/69e40039-a52c-4c05-a54a-18682873583a">
</div>

- After entering your Sheety API account, create a new project from Google Sheets, and paste your Google Sheet URL in the place it shows you.

<div align=center>
<img width="500" alt="image" src="https://github.com/ShiyuFan0820/CheapestFlightTicketFinder/assets/149340606/bc07592a-3786-4e0f-980f-0c3f04d91609">
</div>


<div align=center>
<img width="500" alt="image" src="https://github.com/ShiyuFan0820/CheapestFlightTicketFinder/assets/149340606/28983520-46c5-4649-a395-e2846eb7f4d2">
</div>

- If you don't log in to Google Sheets and Sheety API with the same account, your spreadsheet can't be edited with Sheety API.

<div align=center>
<img width="500" alt="image" src="https://github.com/ShiyuFan0820/CheapestFlightTicketFinder/assets/149340606/6304a89f-5934-4e0c-8d9c-615c1bc173fc">
</div>

- Open all access limitations of your project in Sheety API, and then your Sheety API is all set.

<div align=center>
<img width="500" alt="image" src="https://github.com/ShiyuFan0820/CheapestFlightTicketFinder/assets/149340606/f3e65386-85ef-49b9-b167-9321dc3d115c">
</div>

4. Tequila Flight Search API
- Create a free personal account for Tequila API.
- Create a solution in the tools bar `My solutions`.
<div align=center>
<img width="500" alt="image" src="https://github.com/ShiyuFan0820/CheapestFlightTicketFinder/assets/149340606/f1cc9b71-d316-4084-a2f3-ee6caba3ec29">
</div>

- Choose `Meta Search API integration`, and choose `One-way and Return` and save. Then, your Tequila Flight Search API is all set. You can go to the [documentation page](https://tequila.kiwi.com/portal/docs/tequila_api) to check how to make a request.
<div align=center>
<img width="500" alt="image" src="https://github.com/ShiyuFan0820/CheapestFlightTicketFinder/assets/149340606/81590ffd-7aa2-4e7a-a55a-676c6a00e7aa">
</div>

<div align=center>
<img width="500" alt="image" src="https://github.com/ShiyuFan0820/CheapestFlightTicketFinder/assets/149340606/1ce9fd4c-f29a-4717-ba5d-0fac4e3e6d4a">
</div>

5. Download the Python code file in the directory `src` and open files in Pycharm or other code editors.
6. Replace the code where I marked it should be replaced.
7. Run the `main.py` script and get results in your Google Sheet.





