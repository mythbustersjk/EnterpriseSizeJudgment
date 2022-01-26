"""
根据所属行业，调用Value和SizeJudgmentformula，为主程序返回最终企业划型结果
"""

import Value
import SizeJudgmentformula


def range_value(name, single_dict, range_dict):
    a = ['gongye', 'pfye', 'lsye', 'ysye', 'cangchuye', 'yzye', 'zhusuye', 'cyye', 'xxcsye', 'riye', 'wygl']
    b = ['jzye', 'fdcye']
    size = SizeJudgmentformula.Size(single_dict)
    if name == 'yuye':
        _max, _2nd, _min = Value.in_single_value(range_dict)
        group_size = size.single_income_jg(_max, _2nd, _min)
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
    return group_size

