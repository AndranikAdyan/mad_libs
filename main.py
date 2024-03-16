import functions

index_of_template = -1
while index_of_template < 0 or index_of_template > 2:
	index_of_template = int(input("Choose tamplate(1, 2, 3): ")) - 1


template = functions.get_template(index_of_template)
words = functions.get_dict(index_of_template)

if index_of_template == 0:
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
elif index_of_template == 1:
	print(template.format(
		person_name = words["person_name"],
		noun = words["noun1"],
		adjective = words["adjective1"],
		verb1 = words["verb1"],
		adjective2 = words["adjective2"],
		animal = words["animal1"],
		verb2 = words["verb2"],
		color1 = words["color1"],
		verb3 = words["verb3"],
		adverb = words["adverb_+_ly"],
		number1 = words["number1"],
		measure_of_time = words["measure_of_time"],
		color2 = words["color2"],
		animal2 = words["animal2"],
		number2 = words["number2"],
		silly_word = words["silly_word"],
		noun2 = words["noun2"],
	))
elif index_of_template == 2:
	print(template.format(
		person_name = words["person_name"],
		adjective1 = words["adjective1"],
		color = words["color"],
		animal = words["animal"],
		place = words["place"],
		adjective2 = words["adjective2"],
		magical_creature1 = words["magical_creature1"],
		adjective3 = words["adjective3"],
		magical_creature2 = words["magical_creature2"],
		room = words["room"],
		noun1 = words["noun1"],
		noun2 = words["noun2"],
		noun3 = words["noun3"],
		adjective4 = words["adjective4"],
		noun4 = words["noun4"],
		number = words["number"],
		verb = words["verb"],
		adjective5 = words["adjective5"],
		noun5 = words["noun5"],
	))
else:
	print("Something went wrong!")