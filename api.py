import pandas as pd
from sodapy import Socrata

client = Socrata("www.datos.gov.co", None)

def getData(queryData):

    departamento = queryData[0]
    municipio = queryData[1]
    cultivo = queryData[2]
    numeroRegistros = queryData[3]

    query = f"departamento='{departamento}' AND municipio='{municipio}' AND cultivo='{cultivo}'"


    filteredResults = client.get("ch4u-f3i5", where=query, limit=numeroRegistros)
    filteredResults_df = pd.DataFrame.from_records(filteredResults)

    return filteredResults_df


def getSoilData(filteredResults_df):

    variablesEdaficas = ["ph_agua_suelo_2_5_1_0", "f_sforo_p_bray_ii_mg_kg", "potasio_k_intercambiable_cmol_kg"]

    for variable in variablesEdaficas:
        filteredResults_df[variable] = pd.to_numeric(filteredResults_df[variable], errors='coerce')

    medianas = filteredResults_df[variablesEdaficas].median()

    return [variablesEdaficas, medianas, filteredResults_df]


def dataTable(soilData):

    pd.set_option('display.max_columns', None)

    variablesEdaficas = soilData[0]
    medianas = soilData[1]
    filteredResults_df = soilData[2]

    resultsTable = filteredResults_df[["departamento", "municipio", "cultivo", "topografia"]].copy()

    for variable in variablesEdaficas:
        resultsTable[variable + '_mediana'] = medianas[variable]

    return resultsTable
