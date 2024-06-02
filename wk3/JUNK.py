### Ingestion Template
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs):
    """
    Template code for loading data from any source.

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your data loading logic here

    return {}


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'













import requests
from io import BytesIO
from typing import List
import pandas as pd
import os

def fetch_and_store_data(url: str, filename: str) -> None:
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(response.text)
    with open(filename, 'wb') as file:
        file.write(response.content)


def read_data_and_print_rows(filename: str) -> None:
    df = pd.read_parquet(filename)
    print(f"Number of rows: {len(df)}")

## Specify the URL and filename
url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-03.parquet"
filename = "data.parquet"

## Fetch and Store data
fetch_and_store_data(url, filename)
## Read Data and print number of rows
read_data_and_print_rows(filename)