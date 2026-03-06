import pandas as pd 
import requests 
import sqlite3
import schedule
import time

class COVID_ETL:
    def __init__(self):
        self.api_url = "https://disease.sh/v3/covid-19/countries"
        self.csv_file = "C:/Users/Admin/pandas_project/Rest API/covid_data.csv"
        self.db_file = "C:/Users/Admin/pandas_project/Rest API/covid19_data.db"
        self.df = None

    def extract(self):
        try:
            responce = requests.get(self.api_url, timeout=10)
            responce.raise_for_status()
            data = responce.json()
            print("Data Extracted Successfully")
            return data 
        except requests.exceptions.Timeout:
            print("Request timed out. Check your internet connection.")
        except requests.exceptions.RequestException as e:
            print("Request failed:", e)
            return None
    
    def transform(self, data):
        try:
            df = pd.DataFrame(data)
            df = df[['country', 'cases', 'deaths', 'recovered', 'updated']]
            df.fillna(0, inplace=True)
            self.df = df
            print("Data transformed successfully.")
        except Exception as e:
            print("Transformation Error:", e)

    def load_csv(self):
        try:
            if self.df is None:
                print("No data available to save to CSV.")
                return 
            self.df.to_csv(self.csv_file, index=False)
            print("Data saved to CSV file.")
        except Exception as e:
            print("CSV Loading Error:", e)

    def load_db(self):
        try:
            if self.df is None:
                print("No data available to save to database.")
                return
            conn = sqlite3.connect(self.db_file)
            self.df.to_sql("covid_stats", conn, if_exists="replace", index=False)
            conn.close()
            print("Data saved to SQLite database.")
        except Exception as e:
            print("Database Loading Error:", e)

    def run(self):
        data = self.extract()
        if data:
            self.transform(data)
            self.load_csv()
            self.load_db()
        print("ETL Pipeline Finished.")

if __name__ == "__main__":

    pipeline = COVID_ETL()

    schedule.every(10).seconds.do(pipeline.run)

    print("Scheduler started...")

    for i in range(12):
        schedule.run_pending()
        time.sleep(1)

    print("Scheduler stopped.")
