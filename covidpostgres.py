import requests
import pandas as pd
import schedule
import time
from sqlalchemy import create_engine

import psycopg2

conn = psycopg2.connect(
    host="127.0.0.1",
    database="covid_db",
    user="postgres",
    password="Ayush.zen123@",
    port="5432"
)

print("Connected Successfully")
conn.close()


class COVID_ETL:

    def __init__(self):

        self.api_url = "https://disease.sh/v3/covid-19/countries"

        self.csv_file = "C:/Users/Admin/pandas_project/Rest API/covid_data.csv"
        self.engine = create_engine(
            "postgresql+psycopg2://postgres:Ayush.zen123%40@127.0.0.1:5432/covid_db"
        )

    def extract(self):
        try:
            response = requests.get(self.api_url)
            data = response.json()

            self.df = pd.DataFrame(data)

            print("Data Extracted Successfully")

        except Exception as e:
            print("Extraction Error:", e)

    def transform(self):
        try:

            self.df = self.df[[
                "country",
                "cases",
                "todayCases",
                "deaths",
                "todayDeaths",
                "recovered",
                "active",
                "population"
            ]]

            self.df.rename(columns={
                "country": "Country",
                "cases": "Total_Cases",
                "todayCases": "Today_Cases",
                "deaths": "Total_Deaths",
                "todayDeaths": "Today_Deaths",
                "recovered": "Recovered",
                "active": "Active_Cases",
                "population": "Population"
            }, inplace=True)

            print("Data Transformed Successfully")

        except Exception as e:
            print("Transformation Error:", e)

    def save_csv(self):
        try:
            self.df.to_csv(self.csv_file, index=False)

            print("Data Saved to CSV")

        except Exception as e:

            print("CSV Saving Error:", e)

    def load_to_database(self):
        try:

            self.df.to_sql(
                "covid_data",
                self.engine,
                if_exists="replace",
                index=False
            )

            print("Data Loaded to PostgreSQL Successfully")

        except Exception as e:

            print("Database Loading Error:", e)

    def run(self):

        print("ETL Pipeline Started")

        self.extract()
        self.transform()
        self.save_csv()
        self.load_to_database()

        print("ETL Pipeline Finished")


if __name__ == "__main__":

    pipeline = COVID_ETL()
    schedule.every(10).seconds.do(pipeline.run)

    print("Scheduler Started...")

    for i in range(12):
        schedule.run_pending()
        time.sleep(1)

    print("Scheduler Stopped")
