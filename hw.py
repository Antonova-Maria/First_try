with open('C:\\Users\\manny\\OneDrive\\Рабочий стол\\Classifiers_Array_WO_Signs.txt', "w") as newopen:
	with open('C:\\Users\\manny\\OneDrive\\Рабочий стол\\Classifiers\\masking.yaml', encoding="utf8") as o1:
		for line in o1:
			print(line, end="", file=newopen)
		print("\n", file=newopen)
	with open('C:\\Users\\manny\\OneDrive\\Рабочий стол\\Classifiers\\no_objects.yaml', encoding="utf8") as o2:
		for line in o2:
			print(line, end="", file=newopen)
		print("\n", file=newopen)
	with open('C:\\Users\\manny\\OneDrive\\Рабочий стол\\Classifiers\\road.yaml', encoding="utf8") as o3:
		for line in o3:
			print(line, end="", file=newopen)
		print("\n", file=newopen)
	with open('C:\\Users\\manny\\OneDrive\\Рабочий стол\\Classifiers\\road_defects.yaml', encoding="utf8") as o4:
		for line in o4:
			print(line, end="", file=newopen)
		print("\n", file=newopen)
	with open('C:\\Users\\manny\\OneDrive\\Рабочий стол\\Classifiers\\road_markup.yaml', encoding="utf8") as o5:
		for line in o5:
			print(line, end="", file=newopen)
		print("\n", file=newopen)
	with open('C:\\Users\\manny\\OneDrive\\Рабочий стол\\Classifiers\\road_objects.yaml', encoding="utf8") as o6:
		for line in o6:
			print(line, end="", file=newopen)
		print("\n", file=newopen)
	with open('C:\\Users\\manny\\OneDrive\\Рабочий стол\\Classifiers\\tech_mark.yaml', encoding="utf8") as o7:
		for line in o7:
			print(line, end="", file=newopen)
		print("\n", file=newopen)
	with open('C:\\Users\\manny\\OneDrive\\Рабочий стол\\Classifiers\\vehicles.yaml', encoding="utf8") as o8:
		for line in o8:
			print(line, end="", file=newopen)
		print("\n", file=newopen)