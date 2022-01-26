"""
返回各行业判断边界值
"""


def in_single_value(tmp_dict):
    in_max = tmp_dict['income_max']
    in_2nd = tmp_dict['income_2nd']
    in_min = tmp_dict['income_min']
    return in_max, in_2nd, in_min


def pe_single_value(tmp_dict):
    pe_max = tmp_dict['num_people_max']
    pe_2nd = tmp_dict['num_people_2nd']
    pe_min = tmp_dict['num_people_min']
    return pe_max, pe_2nd, pe_min


def pe_in_value(tmp_dict):
    pe_max = tmp_dict['num_people_max']
    pe_2nd = tmp_dict['num_people_2nd']
    pe_min = tmp_dict['num_people_min']
    in_max = tmp_dict['income_max']
    in_2nd = tmp_dict['income_2nd']
    in_min = tmp_dict['income_min']
    return pe_max, pe_2nd, pe_min, in_max, in_2nd, in_min


def in_as_value(tmp_dict):
    in_max = tmp_dict['income_max']
    in_2nd = tmp_dict['income_2nd']
    in_min = tmp_dict['income_min']
    as_max = tmp_dict['total_assets_max']
    as_2nd = tmp_dict['total_assets_2nd']
    as_min = tmp_dict['total_assets_min']
    return in_max, in_2nd, in_min, as_max, as_2nd, as_min


def pe_as_value(tmp_dict):
    pe_max = tmp_dict['num_people_max']
    pe_2nd = tmp_dict['num_people_2nd']
    pe_min = tmp_dict['num_people_min']
    as_max = tmp_dict['total_assets_max']
    as_2nd = tmp_dict['total_assets_2nd']
    as_min = tmp_dict['total_assets_min']
    return pe_max, pe_2nd, pe_min, as_max, as_2nd, as_min
