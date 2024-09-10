
def getQueryData():
    departamento = input("Ingrese Departamento: ").upper()
    municipio = input("Ingrese Municipio: ").upper()
    cultivo = input("Ingrese Cultivo: ").title()
    numeroRegistros = input("Ingrese numero de registros a consultar: ")

    queryData = [departamento, municipio, cultivo, numeroRegistros]

    return (queryData)


def showData(resultsTable):
    
    print(resultsTable)

