import pandas as pd
import pandas_datareader.data as web
from datetime import datetime
def fetch_cpi_data():
    # Define the start and end date for data fetching
    start_date = "2018-01-01"
    end_date = datetime.today().strftime('%Y-%m-%d')

    # Fetch CPI data from FRED (Federal Reserve Economic Data)
    cpi = web.DataReader("CPIAUCSL", "fred", start_date, end_date)
    cpi = cpi.resample('Q').mean()  # Resample to quarterly average

    # Calculate inflation as % change over the past 4 quarters
    cpi['Inflation (%)'] = cpi['CPIAUCSL'].pct_change(periods=4) * 100

    # Return the last 4 quarters of inflation data
    return cpi.iloc[-4:]

if __name__ == "__main__":
    inflation_data = fetch_cpi_data()
    print(inflation_data)
