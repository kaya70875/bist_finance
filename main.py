import os
import argparse
from lib.scraper import setup_driver , choose_pair
from lib.downloader import get_excel
from lib.utils import get_download_path

def main():
    print('Starting...')
    parser = argparse.ArgumentParser(description="Download Historical Data For Turkish Stocks.")
    parser.add_argument('-p', '--pair', nargs='+', required=True ,help='Pair Name')
    parser.add_argument('-y', '--year', type=str, default='2020', help="Start Year")
    parser.add_argument('-m', '--month', type=str , default='Ocak', help="Start Month")
    parser.add_argument('-P' ,'--path' , type=str , required=True , help='Download Path')

    args = parser.parse_args()

    driver = setup_driver()
    choose_pair(driver , pair_name=args.pair , year=args.year , month=args.month)
    print('Downloading...')

    download_path = get_download_path()
    df = get_excel(driver , download_path)
    print('Fecthing File...')
    desktop_path = args.path
    csv_file_path = os.path.join(desktop_path, f'results-{args.pair}-{args.year}.csv')
    df.to_csv(csv_file_path, index=False)
    
    print(f'{args.pair} successfully completed.')

if __name__ == "__main__":
    main()