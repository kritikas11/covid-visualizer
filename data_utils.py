import pandas as pd

DATA_URL = "https://covid.ourworldindata.org/data/owid-covid-data.csv"

def download_covid_data(file_path="data/owid-covid-data.csv"):
    """
    Downloads COVID-19 data from OWID and saves to local file.
    """
    try:
        df = pd.read_csv(DATA_URL)
        df.to_csv(file_path, index=False)
        print(f"✅ Data downloaded and saved to {file_path}")
    except Exception as e:
        print(f"❌ Error downloading data: {e}")

def load_covid_data(file_path="data/owid-covid-data.csv"):
    """
    Loads COVID-19 data from a local CSV file.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return None

def get_daily_cases(df, country="India"):
    """
    Filters the DataFrame for a specific country and returns a new DataFrame 
    with 'date' and 'new_cases' columns.
    """
    try:
        country_df = df[df['location'] == country]
        country_df['date'] = pd.to_datetime(country_df['date'])
        daily_df = country_df[['date', 'new_cases']].copy()
        daily_df.rename(columns={'date': 'Date', 'new_cases': 'Daily Cases'}, inplace=True)
        return daily_df
    except Exception as e:
        print(f"❌ Error processing data: {e}")
        return None
