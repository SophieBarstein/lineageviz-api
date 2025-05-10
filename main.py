from fastapi import FastAPI
import pandas as pd
import numpy as np

app = FastAPI()

@app.get("/species/{name}")
def get_species(name: str):
    try:
        df = pd.read_csv(f"{name.lower()}.csv")
        df.replace({np.nan: ""}, inplace=True)  # Replace NaNs with empty string
        return df.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}
