from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/species")
def get_species_list():
    return ["c_elegans"]

@app.get("/species/c_elegans")
def get_c_elegans_data():
    df = pd.read_csv("c_elegans.csv")
    return df.to_dict(orient="records")