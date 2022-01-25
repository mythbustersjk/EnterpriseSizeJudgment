from openpyxl import Workbook, load_workbook
import creat_dict
import IndustryJudgment
import DefaultRange
import SizeJudgmentformula
import Value
from openpyxl.styles import *


def main():
    a = ['gongye', 'pfye', 'lsye', 'ysye', 'cangchuye', 'yzye', 'zhusuye', 'cyye', 'xxcsye', 'riye', 'wygl']
    b = ['jzye', 'fdcye']
    wb = load_workbook('test.xlsx')
    ws = wb.active
    main_dict_list = creat_dict.dict(ws.rows)
    cell_row_num = 1
    for single_dict in main_dict_list:
        cell_row_num = + 1
        size = SizeJudgmentformula.Size(single_dict)
        # 获取企业所涉及行业名称
        name = IndustryJudgment.code_judgment(single_dict['industry_code'])
        # 获取行业对应的划型范围
        range_dict = DefaultRange.industry_range(name)
        if name == 'yueye':
            _max, _2nd, _min = Value.in_single_value(range_dict)
            group_size = size.single_people_jd(_max, _2nd, _min)
        elif name == 'other':
            _max, _2nd, _min = Value.pe_single_value(range_dict)
            group_size = size.single_people_jd(_max, _2nd, _min)
        elif name in a:
            pe_max, pe_2nd, pe_min, in_max, in_2nd, in_min = Value.pe_in_value(range_dict)
            group_size = size.people_income_jd(pe_max, in_max, pe_2nd, in_2nd, pe_min, in_min)
        elif name in b:
            in_max, in_2nd, in_min, as_max, as_2nd, as_min = Value.in_as_value(range_dict)
            group_size = size.in_as_jd(as_max, in_max, as_2nd, in_2nd, as_min, in_min)
        elif name == 'zlswye':
            pe_max, pe_2nd, pe_min, as_max, as_2nd, as_min = Value.pe_as_value(range_dict)
            group_size = size.pe_as_jd(as_max, pe_max, as_2nd, pe_2nd, as_min, pe_min)
        print(group_size)


if __name__ == '__main__':
    main()
