## Load Libraries
import os
import sys

import pickle
import pandas as pd
from datetime import date

## Load Model function
def load_model(model_pth):
    with open(model_pth, 'rb') as f:
        dv, model = pickle.load(f)

    return dv, model


categorical = ["PULocationID", "DOLocationID"]

## Load Data function
def read_data(filename):
    df = pd.read_parquet(filename)

    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')
    
    return df

def save_result(df, y_pred, output_file, year, month):
    df["ride_id"] = f"{year:04d}/{month:02d}_" + df.index.astype("str")

    ## Save predictions to dataframe
    df_results = pd.DataFrame(columns = ["predictions", "ride_id"])
    df_results["predictions"] = y_pred
    df_results["ride_id"] = df["ride_id"]
    
    df_results.to_parquet(
        output_file,
        engine = 'pyarrow',
        compression = None,
        index = False
    )

def apply_model(input_file, model_file, output_file, year, month):

    print(f"reading the data from {input_file}...")
    df = read_data(input_file)

    ## Isolating stated catgeories, call dict vectorizer and predict
    dicts = df[categorical].to_dict(orient='records')

    print(f'loading the model with RUN_ID={model_file}...')
    retrv_model = load_model(model_file)
    dv = retrv_model[0]
    model = retrv_model[1]

    X_val = dv.transform(dicts)

    print(f'applying the model...')
    y_pred = model.predict(X_val)
    
    ## Output 1
    print(f"Q6. Mean of predictions: {round(y_pred.mean(), 3)}")

    print(f'saving the result to {output_file}...')
    save_result(df, y_pred, output_file, year, month)

    return output_file


def run():
    taxi_type = sys.argv[1] #yellow
    year = int(sys.argv[2]) #2024
    month = int(sys.argv[3]) #3

    ## Fetch Data
    input_file = f"https://d37ci6vzurychx.cloudfront.net/trip-data/{taxi_type}_tripdata_{year:04d}-{month:02d}.parquet" 

    # model_pth = "../models/model.bin"
    model_pth = "model.bin"

    output_pth = "../output_files"
    if not os.path.exists(f"{output_pth}/{taxi_type}"):
        os.makedirs(f"{output_pth}/{taxi_type}")

    output_file = f"{output_pth}/{taxi_type}/{year:04d}-{month:02d}.parquet"

    apply_model(
        input_file = input_file,
        model_file = model_pth,
        output_file = output_file,
        year = year,
        month = month
    )

    # print(get_ipython().system(" ls -lh ../output_files/* | awk '{print $5, $9}'"))
    # $5, $9: These represent the 5th and 9th fields of each line.
    # (i.e., in kilobytes (K), megabytes (M), gigabytes (G), etc.)



if __name__ == '__main__':
    run()