from API import api
from UI import ui

def main():
    queryData = ui.getQueryData()

    filteredResults_df = api.getData(queryData)
    soilData = api.getSoilData(filteredResults_df)
    resultsTable = api.dataTable(soilData)

    ui.showData(resultsTable)


if __name__ == "__main__":
    main()
