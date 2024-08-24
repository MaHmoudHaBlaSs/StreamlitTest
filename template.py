import pyodbc as odbc
import pandas as pd
import streamlit as st
import requests as rq

API_KEY = 'your_opencage_api_key'


def connect_database() -> odbc.Connection:
    Driver = 'SQL Server'
    Server = 'MAHMOUD_GAMAL'
    Database = 'adventureworks'

    return odbc.connect(f'DRIVER={Driver};SERVER={Server};DATABASE={Database};Trusted_Connection=True')


def run_query(connection: odbc.Connection, query: str) -> pd.DataFrame:
    return pd.read_sql(query, connection)


connection = connect_database()
query = 'Select ListPrice From SalesLT.Product Where ListPrice > 99'
df = run_query(connection, query)

st.title("Data Analysis")
st.header('Line Chart')
st.line_chart(data=df)
st.bar_chart(data=df)
st.area_chart(data=df)

