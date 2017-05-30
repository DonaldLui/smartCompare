import openpyxl
from difflib import SequenceMatcher

fruit = []
fruit2 = []
compareScore = []
matchingName = []
matchingRatioNum = []
wb = openpyxl.load_workbook('Owlshead_AMIS_CMMS_5.12.2017.xlsx')
aSheet = wb.get_sheet_by_name('AMIS')
cSheet = wb.get_sheet_by_name('CMMS')

for col in aSheet['F']:
    fruit.append(col.value)

for col in cSheet['E']:
    fruit2.append(col.value)

length = len(fruit)
length2 = len(fruit2)
i = 0
i2 = 0

for i in range(0, length):
    for i2 in range(0, length2):
        ratio = SequenceMatcher(None, fruit[i], fruit2[i2]).ratio()
        compareScore.append(ratio)
        i2 += 1
    matchRatio = compareScore.index(max(compareScore))
    match = fruit2[matchRatio]
    ratioNum = compareScore[matchRatio]
    matchingName.append(match)
    matchingRatioNum.append(ratioNum)
    compareScore = []
    i += 1

i3 = 0
for i3 in range(0, length):
    V = "V" + str(i3+1)
    aSheet[V] = matchingName[i3]
    del V
    i3 += 1

i4 = 0
for i4 in range(0, length):
    W = "W" + str(i4+1)
    aSheet[W] = matchingRatioNum[i4]
    del W
    i4 += 1
wb.save('Owlshead_AMIS_CMMS_5.12.2017.xlsx')
