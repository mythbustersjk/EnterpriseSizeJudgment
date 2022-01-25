def size(industry, industry3, single_dict):
	global group_size
	size_dict = single_dict.copy()
	income = int(size_dict['income'])
	num_people = int(size_dict['num_people'])
	total_assets = int(size_dict['total_assets'])
	# 农业规模判断
	if industry == 'A':
		if income >= 20000:
			group_size = '大型企业'
		elif 500 <= income < 20000:
			group_size = '中型企业'
		elif 50 <= income < 500:
			group_size = '小型企业'
		elif 0 <= income < 50:
			group_size = '微型企业'
	# 建筑业规模判断
	elif industry == 'E':
		if income >= 80000 and total_assets >= 80000:
			group_size = '大型企业'
		elif income >= 80000 > total_assets < 80000:
			group_size = '中型企业'
		elif income < 80000 and total_assets >= 80000:
			group_size = '中型企业'
		elif 6000 <= income < 80000 and 5000 <= total_assets < 80000:
			group_size = '中型企业'
		elif 6000 <= income < 80000 and total_assets < 5000:
			group_size = '小型企业'
		elif income < 6000 and 5000 <= total_assets < 80000:
			group_size = '小型企业'
		elif 300 <= income < 6000 and 300 <= total_assets < 5000:
			group_size = '小型企业'
		elif 300 <= income < 6000 and total_assets < 300:
			group_size = '微型企业'
		elif income < 300 and 300 <= total_assets < 5000:
			group_size = '微型企业'
		elif income < 300 or total_assets < 300:
			group_size = '微型企业'
	# 批发业及零售业规模判断
	elif industry == 'F':
		# 批发业规模判断
		if industry3 == 'F51':
			if income >= 40000 and num_people >= 200:
				group_size = '大型企业'
			elif income >= 40000 and num_people < 200:
				group_size = '中型企业'
			elif income < 40000 and num_people >= 200:
				group_size = '中型企业'
			elif 5000 <= income < 40000 and 20 <= num_people < 200:
				group_size = '中型企业'
			elif 5000 <= income < 40000 and num_people < 20:
				group_size = '小型企业'
			elif income < 5000 and 20 <= num_people < 200:
				group_size = '小型企业'
			elif 1000 <= income < 5000 and 5 <= num_people < 20:
				group_size = '小型企业'
			elif 1000 <= income < 5000 and num_people < 5:
				group_size = '微型企业'
			elif income < 1000 and 5 <= num_people < 20:
				group_size = '微型企业'
			elif income < 1000 or total_assets < 5:
				group_size = '微型企业'
		# 零售业规模判断
		if industry3 == "F52":
			if income >= 20000 and num_people >= 300:
				group_size = '大型企业'
			elif income >= 20000 and num_people < 300:
				group_size = '中型企业'
			elif income < 20000 and num_people >= 300:
				group_size = '中型企业'
			elif 500 <= income < 20000 and 50 <= num_people < 300:
				group_size = '中型企业'
			elif 500 <= income < 20000 and num_people < 50:
				group_size = '小型企业'
			elif income < 500 and 50 <= num_people < 300:
				group_size = '小型企业'
			elif 100 <= income < 500 and 10 <= num_people < 50:
				group_size = '小型企业'
			elif 100 <= income < 500 and num_people < 10:
				group_size = '微型企业'
			elif income < 100 and 10 <= num_people < 50:
				group_size = '微型企业'
			elif income < 100 or total_assets < 10:
				group_size = '微型企业'
	# 邮政业规模判断
	elif industry == 'F':
		if income >= 20000 and num_people >= 300:
			group_size = '大型企业'
		elif income >= 20000 and num_people < 300:
			group_size = '中型企业'
		elif income < 20000 and num_people >= 300:
			group_size = '中型企业'
		elif 500 <= income < 20000 and 50 <= num_people < 300:
			group_size = '中型企业'
		elif 500 <= income < 20000 and num_people < 50:
			group_size = '小型企业'
		elif income < 500 and 50 <= num_people < 300:
			group_size = '小型企业'
		elif 100 <= income < 500 and 10 <= num_people < 50:
			group_size = '小型企业'
		elif 100 <= income < 500 and num_people < 10:
			group_size = '微型企业'
		elif income < 100 and 10 <= num_people < 50:
			group_size = '微型企业'
		elif income < 100 or total_assets < 10:
			group_size = '微型企业'

	return group_size
