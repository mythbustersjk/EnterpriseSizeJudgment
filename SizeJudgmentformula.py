class Size:
    """
    传入模版中income，num_people，total_assets值，判读企业规模
    """

    def __init__(self, single_dict):
        self.income = int(single_dict['income'])
        self.num_people = int(single_dict['num_people'])
        self.total_assets = int(single_dict['total_assets'])

    def single_income_jg(self, _max, _2nd, _min):
        if self.income >= _max:
            group_size = '大型企业'
        elif _2nd <= self.income < _max:
            group_size = '中型企业'
        elif _min <= self.income < _2nd:
            group_size = '小型企业'
        elif 0 <= self.income < _min:
            group_size = '微型企业'
        return group_size

    def single_people_jd(self, _max, _2nd, _min):
        if self.num_people >= _max:
            group_size = '大型企业'
        elif _2nd <= self.num_people < _max:
            group_size = '中型企业'
        elif _min <= self.num_people < _2nd:
            group_size = '小型企业'
        elif 0 <= self.num_people < _min:
            group_size = '微型企业'
        return group_size

    def people_income_jd(self, pe_max, in_max, pe_2nd, in_2nd, pe_min, in_min):
        if self.income >= in_max and self.num_people >= pe_max:
            group_size = '大型企业'
        elif self.income >= in_max and self.num_people < pe_max:
            group_size = '中型企业'
        elif self.income < in_max and self.num_people >= pe_max:
            group_size = '中型企业'
        elif in_min <= self.income < in_max and pe_2nd <= self.num_people < pe_max:
            group_size = '中型企业'
        elif in_min <= self.income < in_max and self.num_people < pe_2nd:
            group_size = '小型企业'
        elif self.income < in_min and pe_2nd <= self.num_people < pe_max:
            group_size = '小型企业'
        elif in_min <= self.income < in_2nd and pe_min <= self.num_people < pe_2nd:
            group_size = '小型企业'
        elif in_min <= self.income < in_2nd and self.num_people < pe_min:
            group_size = '微型企业'
        elif self.income < in_max and pe_min <= self.num_people < pe_2nd:
            group_size = '微型企业'
        elif self.income < in_min or self.num_people < pe_min:
            group_size = '微型企业'
        return group_size

    def in_as_jd(self, as_max, in_max, as_2nd, in_2nd, as_min, in_min):
        if self.income >= in_max and self.total_assets >= as_max:
            group_size = '大型企业'
        elif self.income >= in_max and self.total_assets < as_max:
            group_size = '中型企业'
        elif self.income < in_max and self.total_assets >= as_max:
            group_size = '中型企业'
        elif in_min <= self.income < in_max and as_2nd <= self.total_assets < as_max:
            group_size = '中型企业'
        elif in_min <= self.income < in_max and self.total_assets < as_2nd:
            group_size = '小型企业'
        elif self.income < in_min and as_2nd <= self.total_assets < as_max:
            group_size = '小型企业'
        elif in_min <= self.income < in_2nd and as_min <= self.total_assets < as_2nd:
            group_size = '小型企业'
        elif in_min <= self.income < in_2nd and self.total_assets < as_min:
            group_size = '微型企业'
        elif self.income < in_max and as_min <= self.total_assets < as_2nd:
            group_size = '微型企业'
        elif self.income < in_min or self.total_assets < as_min:
            group_size = '微型企业'
        return group_size

    def pe_as_jd(self, as_max, pe_max, as_2nd, pe_2nd, as_min, pe_min):
        if self.num_people >= pe_max and self.total_assets >= as_max:
            group_size = '大型企业'
        elif self.num_people >= pe_max and self.total_assets < as_max:
            group_size = '中型企业'
        elif self.num_people < pe_max and self.total_assets >= as_max:
            group_size = '中型企业'
        elif pe_min <= self.num_people < pe_max and as_2nd <= self.total_assets < as_max:
            group_size = '中型企业'
        elif pe_min <= self.num_people < pe_max and self.total_assets < as_2nd:
            group_size = '小型企业'
        elif self.num_people < pe_min and as_2nd <= self.total_assets < as_max:
            group_size = '小型企业'
        elif pe_min <= self.num_people < pe_2nd and as_min <= self.total_assets < as_2nd:
            group_size = '小型企业'
        elif pe_min <= self.num_people < pe_2nd and self.total_assets < as_min:
            group_size = '微型企业'
        elif self.num_people < pe_max and as_min <= self.total_assets < as_2nd:
            group_size = '微型企业'
        elif self.num_people < pe_min or self.total_assets < as_min:
            group_size = '微型企业'
        return group_size
