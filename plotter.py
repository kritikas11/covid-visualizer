import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="darkgrid")

def plot_daily_cases(daily_df, country_name):
    """
    Plots daily COVID-19 cases for a given country.

    Parameters:
        daily_df (DataFrame): DataFrame with 'Date' and 'Daily Cases' columns.
        country_name (str): Country name to display in the title.
    """
    try:
        plt.figure(figsize=(12, 6))
        plt.plot(daily_df['Date'], daily_df['Daily Cases'], label='Daily Cases', color='skyblue')
        plt.xlabel('Date')
        plt.ylabel('Daily Cases')
        plt.title(f'📊 Daily COVID-19 Cases in {country_name}')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.legend()
        plt.show()
    except Exception as e:
        print(f"❌ Error plotting data: {e}")
