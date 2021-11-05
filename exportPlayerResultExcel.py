import json
import pandas as pd
import xlsxwriter

INPUT_FILE = "outputPlayer.json"

def read_file(inputFile):
    f = open(inputFile, "r")
    return f.read()

def export():
    data = json.loads(read_file(INPUT_FILE))
    df_total = pd.DataFrame(data)
    df_total = df_total.filter(items=["demandSupplyByPeriodOffers","totalDemandSupply","totalSatisfied","totalCostsProfitsByPeriodOffers","totalCostsProfits",""])
    if data["playerPeriodsResult"][0]["transactionType"] == "selling":
        df_periods = pd.DataFrame(data["playerPeriodsResult"], columns=["period","transactionType","supply","satisfied","marketPrice","profits"])
    else:
        df_periods = pd.DataFrame(data["playerPeriodsResult"], columns=["period","transactionType","demand","satisfied","marketPrice","costs"])
    
 # Define Excel file
    writer = pd.ExcelWriter("outputPlayer.xlsx", engine="xlsxwriter")
    
    # Export data
    df_periods.to_excel(writer, sheet_name="ExportedData", startcol=1, startrow=2, index=False)
    df_total.iloc[0:1].to_excel(writer, sheet_name="ExportedData", startcol=1, startrow=30, index=False)
    workbook = writer.book
    worksheet = writer.sheets['ExportedData']
    for i in range(24):
        worksheet.write(i+3, 0, data["playerId"])
    
    # Format data
    header_format = workbook.add_format({
        'bold': True,
        'text_wrap': True,
        'valign': 'top',
        'fg_color': '#D7E4BC',
        'border': 1})
    for col_num, value in enumerate(df_periods.columns.values):
        worksheet.write(2, col_num + 1, value, header_format)
    for col_num, value in enumerate(df_total.columns.values):
        worksheet.write(30, col_num + 1, value, header_format)
    worksheet.write(2, 0, "playerId", header_format)

    format1 = workbook.add_format({'border': 1})
    worksheet.set_column(0, 6, 27)
    worksheet.conditional_format('A4:G27', {'type': 'top',
                                            'criteria': "!=",
                                            'value': 'none',
                                            'format': format1})
    worksheet.conditional_format('C4:C27', {'type': 'text',
                                            'criteria': 'not containing',
                                            'value': 'none',
                                            'format': format1})
    worksheet.conditional_format('A4:A27', {'type': 'text',
                                            'criteria': 'not containing',
                                            'value': 'none',
                                            'format': format1})
    worksheet.conditional_format('B32:F32', {'type': 'top',
                                             'criteria': "!=",
                                             'value': 'none',
                                             'format': format1})
    writer.save()

if __name__ == "__main__":
	export()