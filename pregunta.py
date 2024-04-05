"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
from datetime import datetime
import re

def clean_data():


    df_original = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)
    df = df_original.copy()

    df = df.dropna()

    #sexo
    df["sexo"] = df["sexo"].str.lower()

    #tipo de emprendimiento
    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.lower()

    #idea de negocio
    df["idea_negocio"] = df["idea_negocio"].str.lower().str.replace("-"," ").str.replace("_"," ")

    #barrio
    df["barrio"] = df["barrio"].str.lower().str.replace("-"," ").str.replace("_"," ")

    #estrato
    df["estrato"] = df["estrato"].astype(int)

    #comuna
    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int)

    #fecha
    df["fecha_de_beneficio"] = [
        (
            datetime.strptime(date, "%d/%m/%Y")
            if bool(re.search(r"\d{1,2}/\d{2}/\d{4}", date))
            else datetime.strptime(date, "%Y/%m/%d")
        )
        for date in df["fecha_de_beneficio"]
        ]
    
    #monto del credito
    df["monto_del_credito"] = df["monto_del_credito"].str.strip("$").str.replace(r"\.00", "", regex=True).str.replace(",","").astype(int)

    #linea de credito
    df["línea_credito"] = df["línea_credito"].str.strip().str.lower().str.replace("-", " ").str.replace("_", " ").str.replace(". ", ".")


    df = df.drop_duplicates()

    return df
