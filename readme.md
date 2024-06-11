Historical Data Downloader for Turkish Stocks

This script downloads historical data for Turkish stocks and saves it as a CSV file. The script uses web scraping techniques to fetch the data and requires specific parameters to run.
Prerequisites

Ensure you have the following installed:

    Python 3.x
    Necessary Python packages (listed in requirements.txt if available)

Installation

    Clone the repository:

git clone https://github.com/kaya70875/bist_finance

cd bist_finance

Install the required packages:

    pip install -r requirements.txt

Usage

Run the script from the command line with the required arguments:

python main.py -p <pair_name> -P <download_path> [-y <year>] [-m <month>]

Arguments

    -p, --pair: Required. The name of the stock pair.
    -P, --path: Required. The path where the CSV file will be saved.
    -y, --year: Optional. The start year for the data (default: '2020').
    -m, --month: Optional. The start month for the data (default: 'Ocak').

Example

python main.py -p AKBNK -P ~/Downloads -y 2021 -m Mart

This command will download historical data for the AKBNK stock pair, starting from March 2021, and save the resulting CSV file in the ~/Downloads directory.
