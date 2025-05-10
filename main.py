from fastapi import FastAPI
import pandas as pd
import os
import numpy as np

app = FastAPI()

@app.get("/species")
def get_species_list():
    # Return all CSV filenames in the directory without ".csv"
    files = os.listdir(".")
    species = [f.replace(".csv", "") for f in files if f.endswith(".csv")]
    return species

@app.get("/species/{name}")
def get_species_data(name: str):
    filename = f"{name.lower()}.csv"
    try:
        df = pd.read_csv(filename)
        df.replace({np.nan: ""}, inplace=True)  # JSON-safe: replace NaN
        return df.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}
