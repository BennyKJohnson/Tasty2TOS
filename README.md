# Tasty2TOS

Tasty2TOS is a Python script that converts Tastytrade positions to Thinkorswim positions. I wrote this script so I could easily analyze my TastyTrade positions inside of the Risk Profile of Thinkorswim

## Prerequisites

### TastyTrade Account with Open API access
You need to provide your TastyTrade login credentials for an account that has API access in order for the script to work. This account will only be used to lookup underlying information on the positions you provide. For instructions on how to enable API access, visit https://support.tastyworks.com/support/solutions/articles/43000700385-tastytrade-open-api#:~:text=Open%20API%20Access,our%20API%27s%20terms%20and%20conditions.

Before running Tasty2TOS, make sure you have the following installed on your machine:
- Python 3.x - Installation - including python requirements.txt

Install the requirements
```bash
cd Tasty2TOS
pip3 install -r requirements.txt
```

## Usage

### Exporting positions
In order for Tasty2TOS to work, you need to provide it with the location of your TastyTrade positions in a CSV file.

To export your positions, open the TastyTrade application and go to the `POSITIONS` tab, find the small button in the top right corner with 'CSV', click it and save the csv when prompted. The location of this file is required to run the script.

Run the following command from the project directory to execute the script:

````bash
python3 script.py --username YOUR_TASTYTRADE_USERNAME --password YOUR_TASTYTRADE_PASSWORD PATH_TO_CSV_FILE
````
Replace YOUR_TASTYTRADE_USERNAME and YOUR_TASTYTRADE_PASSWORD with your TastyTrade login credentials and PATH_TO_CSV_FILE with the path to your Tastytrade positions CSV file.

Example

````bash
python3 script.py --username johndoe --password mypassword123 tastytrade_positions_2023-05-08.csv
````
