from matplotlib import pyplot
from openpyxl import load_workbook

wb = load_workbook('data_analysis_lab.xlsx')

sheet = wb['Data']

def getvalue(x): return x.value

dates = [i.value for i in sheet['A'][1:]]
rel_temp = [i.value for i in sheet['C'][1:]]
sun_activity = [i.value for i in sheet['D'][1:]]

'''dates = list(map(getvalue, cells_in_A_column))
rel_temp = list(map(getvalue, cells_in_C_column))
sun_activity = list(map(getvalue, cells_in_D_column))'''

pyplot.plot(dates, rel_temp, label="Относительная температура")
pyplot.plot(dates, sun_activity, label="Активность солнца")

pyplot.legend(loc='best')
pyplot.show()