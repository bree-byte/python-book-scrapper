# Book Price Scraper

## Overview
This project is a Python script that scrapes book titles and their prices in GBP from the website [Books to Scrape](https://books.toscrape.com/), converts the prices to Kenyan Shillings (KES) using an exchange rate API, and saves the results to a JSON file (`books_prices.json`). The script uses web scraping and API requests to gather and process data.

## Features
- Scrapes book titles and prices (in GBP) from the first 10 products listed on the website.
- Fetches the current USD to KES exchange rate using the [ExchangeRate-API](https://www.exchangerate-api.com/).
- Converts book prices from GBP to KES using a hardcoded exchange rate (129.235 KES per GBP).
- Saves the processed data (book title, price in GBP, and price in KES) to a JSON file.
- Handles special characters in the output file using UTF-8 encoding.

## Prerequisites
To run this project, you need to have the following installed:
- Python 3.x
- Required Python libraries:
  - `requests`
  - `beautifulsoup4`

Additionally, you need an API key from [ExchangeRate-API](https://www.exchangerate-api.com/) to fetch exchange rates. Store the API key in a `.env` file as follows:
```
API_KEY=your_api_key_here
```

## Project Structure
- `books_prices.json`: The output file containing the scraped book data with prices in GBP and KES.
- `.env`: File to store the API key for the ExchangeRate-API (not included in version control).
- Main script: The Python script that performs the scraping, conversion, and file output.

## How It Works
1. **Web Scraping**:
   - The script fetches the HTML content from [Books to Scrape](https://books.toscrape.com/).
   - It parses the HTML to extract book titles and prices for the first 10 products listed.

2. **Exchange Rate Conversion**:
   - The script fetches the latest USD to KES exchange rate from the ExchangeRate-API.
   - Prices in GBP are converted to KES using a hardcoded exchange rate (129.235 KES per GBP).

3. **Data Storage**:
   - The scraped and converted data (book title, price in GBP, and price in KES) is stored in a list of dictionaries.
   - The data is saved to `books_prices.json` in a formatted JSON structure with proper encoding for special characters.

4. **Output**:
   - The script prints the exchange rate, the converted prices in KES, and a confirmation that the data has been saved.
   - The `books_prices.json` file is created/updated with the scraped data.

## Usage
1. Clone or download the project files.
2. Ensure you have the required dependencies installed (see **Prerequisites**).
3. Add your ExchangeRate-API key to a `.env` file in the project root.
4. Run the script using Python.
5. Check the output:
   - The terminal will display the exchange rate, the list of book prices in KES, and a confirmation that the data has been saved.
   - The `books_prices.json` file will be created/updated with the scraped data.

## Notes
- The script uses a hardcoded GBP to KES exchange rate (129.235). To make it dynamic, you can modify the script to fetch the GBP to KES rate directly from the API.
- The API key should be stored securely in a `.env` file and not hardcoded in the script.
- The script scrapes only the first 10 products for simplicity. You can modify it to scrape more or all products.
## License
This project is for educational purposes and uses publicly available data from [Books to Scrape](https://books.toscrape.com/), a website designed for practicing web scraping.
