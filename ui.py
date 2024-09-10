from tabulate import tabulate

def getQueryData():
    departamento = input("Ingrese Departamento: ").upper()
    municipio = input("Ingrese Municipio: ").upper()
    cultivo = input("Ingrese Cultivo: ").title()
    numeroRegistros = input("Ingrese numero de registros a consultar: ")

    queryData = [departamento, municipio, cultivo, numeroRegistros]

    return (queryData)


def showData(resultsTable):
    
    resultsTable = resultsTable.rename(columns={
    "ph_agua_suelo_2_5_1_0_mediana": 'pH',
    "f_sforo_p_bray_ii_mg_kg_mediana": 'Fósforo (mg/kg)',
    "potasio_k_intercambiable_cmol_kg_mediana": 'Potasio (cmol/kg)'
    })

    table = tabulate(resultsTable, headers='keys', tablefmt='grid')
    print(table)

