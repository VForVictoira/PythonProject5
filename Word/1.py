#导入openpyxl库
import openpyxl
#设置分公司名称列表(myNames)
myNames=['北京分公司','上海分公司','深圳分公司','西安分公司',
         '沈阳分公司','重庆分公司','武汉分公司']
#循环列表(myNames)的分公司名称(myName)
for myName in myNames:
     #根据分公司名称(myName)设置Excel文件的名称
     myPath='结果表-'+myName+'2020年度利润表.xlsx'
     #新建空白工作簿(myBook)
     myBook=openpyxl.Workbook()
     #根据参数(myPath)保存空白工作簿(myBook),即创建(保存)多个空白的Excel文件
     myBook.save(myPath)