"""
以excel首行标题为key生成每行对应的资金列表集合
"""


def dict(rows):
    rows_list = []
    for row in rows:
        row_list = []
        for cell in row:
            row_list.append(cell.value)
        rows_list.append(row_list)
    result = []
    for i in range(len(rows_list) - 1):
        row_dict = {}
        for j in range(len(rows_list[0])):
            row_dict[rows_list[0][j]] = rows_list[i + 1][j]
        result.append(row_dict)
    return result
