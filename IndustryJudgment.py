"""
判断客户所属行业类型
"""


def code_judgment(code):
    industry_name = ''
    gy = ['B', 'C', "D"]
    ysy = ['G54', 'G56', 'G57', 'G58', 'G69']
    xx = ['I63', 'I64']
    # 鱼业
    if code[0] == 'A':
        industry_name = 'yuye'
    # 工业
    elif code[0] in gy:
        industry_name = 'gongye'
    # 建筑业
    elif code[0] == 'E':
        industry_name = 'jzye'
    # 批发及零售业
    elif code[0] == 'F':
        if code[0:3] == 'F51':
            industry_name = 'pfye'
        elif code[0:3] == 'F52':
            industry_name = 'lsye'
    # 运输业
    elif code[0] in ysy:
        industry_name = 'ysye'
    # 仓储业
    elif code[0:3] == 'G59':
        industry_name = 'cangchuye'
    # 邮政业
    elif code[0:3] == 'G60':
        industry_name = 'yzye'
    # 住宿业
    elif code[0:3] == 'H61':
        industry_name = 'zhusuye'
    # 餐饮业
    elif code[0:3] == 'H62':
        industry_name = 'cyye'
    # 信息传输业
    elif code[0:3] in xx:
        industry_name = 'xxcsye'
    # 软件和信息技术服务业
    elif code[0:3] == 'I65':
        industry_name = 'rjye'
    # 房地产开发经营
    elif code[0:4] == 'K701':
        industry_name = 'fdcye'
    # 物业管理
    elif code[0:4] == 'K702':
        industry_name = 'wygl'
    # 租赁和商务服务业
    elif code[0] == 'L':
        industry_name = 'zlswye'
    else:
        industry_name = 'other'
    return industry_name
