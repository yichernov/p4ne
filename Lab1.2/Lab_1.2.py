from matplotlib import pyplot
from openpyxl import load_workbook

wb = load_workbook('data_analysis_lab.xlsx')

sheet = wb['Data']

cells_in_A_column = sheet['A'][1:]
cells_in_C_column = sheet['C'][1:]
cells_in_D_column = sheet['D'][1:]


def getvalue(x): return x.value

dates = [i.value for i in cells_in_A_column]
rel_temp = [i.value for i in cells_in_C_column]
sun_activity = [i.value for i in cells_in_D_column]

'''dates = list(map(getvalue, cells_in_A_column))
rel_temp = list(map(getvalue, cells_in_C_column))
sun_activity = list(map(getvalue, cells_in_D_column))'''

pyplot.plot(dates, rel_temp, label="Относительная температура")
pyplot.plot(dates, sun_activity, label="Активность солнца")

pyplot.legend(loc='best')
pyplot.show()


'''cells_in_a_column = sheet['A'][1:]

date_list = [i.value for i in cells_in_a_column]

print(date_list)'''