from API import api
from UI import ui

queryData = ui.getQueryData()

filteredResults_df = api.getData(queryData)
soilData = api.getSoilData(filteredResults_df)
resultsTable = api.dataTable(soilData)

ui.showData(resultsTable)



