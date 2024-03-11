import functions

index_of_tamplate = 0
while index_of_tamplate < 1 or index_of_tamplate > 3:
	index_of_tamplate = int(input("Choose tamplate(1, 2, 3): "))
    
index_of_tamplate -= 1

template = functions.get_template(index_of_tamplate)
words = functions.get_dict(index_of_tamplate)


if index_of_tamplate == 0:
	print(template.format(
		number = words["number1"],
		measure_of_time = words["measure_of_time"],
		mode_of_transportation = words["mode_of_transportation"],
		adjective = words["adjective1"],
		adjective2 = words["adjective2"],
		noun1 = words["noun1"],
		color = words["color"],
		part_of_the_body = words["part_of_the_body1"],
		verb1 = words["verb1"],
		number2 = words["number2"],
		noun2 = words["noun2"],
		noun3 = words["noun3"],
		part_of_the_body2 = words["part_of_the_body2"],
		verb2 = words["verb2"],
		noun4 = words["noun4"],
		adjective3 =  words["adjective3"],
		silly_word = words["silly_word"],
		noun5 = words["noun5"],
	))
elif index_of_tamplate == 1:
	pass
else:
	pass
