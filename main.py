from openpyxl import Workbook, load_workbook
import creat_dict
import SizeJudgment
from openpyxl.styles import *


def main():
    wb = load_workbook('test.xlsx')
    ws = wb.active
    main_dict_list = creat_dict.dict(ws.rows)
    cell_row_num = 1
    for single_dict in main_dict_list:
        cell_row_num = + 1
        SizeJudgment.size(single_dict['industry_code'][0],single_dict['industry_code'][0:3], single_dict)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
