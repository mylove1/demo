#coding:utf-8
import xlrd
data = xlrd.open_workbook(r"C:\Users\cooper\Desktop\0001.xlsx")

table = data.sheets()[0]
d = table.row_values(1)
print table.nrows
print table.row_values(0)
print len(d)