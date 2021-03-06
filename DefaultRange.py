"""
企业规模划型标准定义函数
"""

import yaml


def industry_range(industry_name):
    try:
        with open('DefaultSetting.yaml', 'r', encoding='utf-8') as range_file:
            ids_dict = yaml.load(range_file, Loader=yaml.FullLoader)
        return ids_dict[industry_name]
    except FileNotFoundError:
        ids_dict = {'yuye': {'income_max': 20000, 'income_2nd': 500, 'income_min': 50},
                    'gongye': {'num_people_max': 1000, 'num_people_2nd': 300, 'num_people_min': 20,
                               'income_max': 40000, 'income_2nd': 2000, 'income_min': 300},
                    'jzye': {'income_max': 80000, 'income_2nd': 6000, 'income_min': 300,
                             'total_assets_max': 8000, 'total_assets_2nd': 5000, "total_assets_min": 300},
                    'pfye': {'num_people_max': 200, 'num_people_2nd': 20, 'num_people_min': 5,
                             'income_max': 40000, 'income_2nd': 5000, 'income_min': 1000},
                    'lsye': {'num_people_max': 300, 'num_people_2nd': 50, 'num_people_min': 10,
                             'income_max': 20000, 'income_2nd': 500, 'income_min': 100},
                    'ysye': {'num_people_max': 1000, 'num_people_2nd': 300, 'num_people_min': 20,
                             'income_max': 30000, 'income_2nd': 3000, 'income_min': 200},
                    'cangchuye': {'num_people_max': 200, 'num_people_2nd': 100, 'num_people_min': 20,
                                  'income_max': 30000, 'income_2nd': 1000, 'income_min': 100},
                    'yzye': {'num_people_max': 1000, 'num_people_2nd': 300, 'num_people_min': 20,
                             'income_max': 30000, 'income_2nd': 2000, 'income_min': 100},
                    'zhusuye': {'num_people_max': 300, 'num_people_2nd': 100, 'num_people_min': 10,
                                'income_max': 10000, 'income_2nd': 2000, 'income_min': 100},
                    'cyye': {'num_people_max': 300, 'num_people_2nd': 100, 'num_people_min': 10,
                             'income_max': 10000, 'income_2nd': 2000, 'income_min': 100},
                    'xxcsy': {'num_people_max': 2000, 'num_people_2nd': 100, 'num_people_min': 10,
                              'income_max': 100000, 'income_2nd': 1000, 'income_min': 100},
                    'rjye': {'num_people_max': 300, 'num_people_2nd': 100, 'num_people_min': 10,
                             'income_max': 10000, 'income_2nd': 1000, 'income_min': 50},
                    'fdcye': {'income_max': 200000, 'income_2nd': 1000, 'income_min': 100,
                              'total_assets_max': 10000, 'total_asset_2nd': 5000, "total_assets_min": 2000},
                    'wygl': {'num_people_max': 1000, 'num_people_2nd': 300, 'num_people_min': 100,
                             'income_max': 5000, 'income_2nd': 1000, 'income_min': 500},
                    'zlswye': {'num_people_max': 300, 'num_people_2nd': 100, 'num_people_min': 10,
                               'total_assets_max': 120000, 'total_assets_2nd': 8000, "total_assets_min": 100},
                    'other': {'num_people_max': 300, 'num_people_2nd': 100, 'num_people_min': 10}
                    }
        with open('DefaultSetting.yaml', "w", encoding='utf-8') as create_range_file:
            yaml.dump(data=ids_dict, stream=create_range_file, allow_unicode=True)
        return ids_dict[industry_name]
