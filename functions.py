def get_template(index: int):
	templates = [
"""
It was about {number} {measure_of_time} ago when I arrived at the  hospital in a {mode_of_transportation}.
The hospital is a/an {adjective} place, there are a lot of {adjective2} {noun1} here. There are nurses here who have {color}
{part_of_the_body}. If someone wants to come into my room I told them that they have to {verb1} first. I've decorated my room with
{number2} {noun2}. Today I talked to a doctor and they were wearing a {noun3} on their {part_of_the_body2}. I heard that all doctors
{verb2} {noun4} every day for breakfast. The most {adjective3} thing about  being in the hospital is the {silly_word} {noun5} !
""",

"""
This weekend I am going camping with {person_name}.I packed my lantern, sleeping bag, and {noun}. I am so {adjective} to {verb1}
in a tent. I am {adjective2} we might see a(n) {animal}, I hear they're kind of dangerous. While we're camping, we are going to hike,
fish, and {verb2}. I have heard that the {color1} lake is great for {verb3}. Then we will {adverb} hike through theforest for {number1} {measure_of_time}.
If I see a {color2} {animal2} while hiking, I am going to bring it home as a pet! At night we will tell {number2} {silly_word} stories and roast {noun2} around the campfire!!
""",
		
"""
Dear {person_name}, I am writing to you from a {adjective1} castle in an enchanted forest. I found myself here one day after going for a
ride on a {color} {animal} in {place}. There are {adjective2} {magical_creature1} and {adjective3} {magical_creature2} here! In the
{room} there is a pool full of {noun1}. I fall asleep each night on a {noun2} of {noun3} and dream of {adjective4} {noun4}. It feels as though I
have lived here for {number}. I hope one day you can visit, although the only way to get here now is {verb} on a {adjective5} {noun5}!!
"""
	]

	return templates[index]

def get_dict(index: int):
	words = {}
	if index == 0:
		words["number1"] = input("Input a number: ")
		while not check_number(words["number1"]):
			print("Please check input format!")
			words["number1"] = input("Input a number: ")
		words["measure_of_time"] = input("Input a measure of time: ")
		words["mode_of_transportation"] = input("Input a mode of transportation: ")
		words["adjective1"] = input("Input a adjective: ")
		words["adjective2"] = input("Input a adjective: ")
		words["noun1"] = input("Input a noun: ")
		words["color"] = input("Input a color: ")
		words["part_of_the_body1"] = input("Input a part of the body: ")
		words["verb1"] = input("Input a verb: ")
		words["number2"] = input("Input a number: ")
		while not check_number(words["number2"]):
			print("Please check input format!")
			words["number2"] = input("Input a number: ")
		words["noun2"] = input("Input a noun: ")
		words["noun3"] = input("Input a noun: ")
		words["part_of_the_body2"] = input("Input a part of the body: ")
		words["verb2"] = input("Input a verb: ")
		words["noun4"] = input("Input a noun: ")
		words["adjective3"] = input("Input a adjective: ")
		words["silly_word"] = input("Input a silly word: ")
		words["noun5"] = input("Input a noun: ")

	elif index == 1:
		words["person_name"] = input("Input a preson name: ")
		words["noun1"] = input("Input a noun: ")
		words["adjective1"] = input("Input a adjective (feeling): ")
		words["verb1"] = input("Input a verb: ")
		words["adjective2"] = input("Input a adjective (feeling): ")
		words["animal1"] = input("Input a animal: ")
		words["verb2"] = input("Input a verb: ")
		words["color1"] = input("Input a color: ")
		words["verb3"] = input("Input a verb + ing: ")
		while words["verb3"][-3:] != "ing":
			print("Please check input format!")
			words["verb3"] = input("Input a verb + ing: ")
		words["adverb_+_ly"] = input("Input a adverb: ")
		words["number1"] = input("Input a number: ")
		words["measure_of_time"] = input("Input a measure of time: ")
		words["color2"] = input("Input a number: ")
		words["animal2"] = input("Input a animal: ")
		words["number2"] = input("Input a number: ")
		while not check_number(words["number2"]):
			print("Please check input format!")
			words["number2"] = input("Input a number: ")
		words["silly_word"] = input("Input a silly_word: ")
		words["noun2"] = input("Input a noun: ")

	else:
		words["person_name"] = input("Input a person name: ")
		words["adjective1"] = input("Input a adjective: ")
		words["color"] = input("Input a color: ")
		words["animal"] = input("Input animal: ")
		words["place"] = input("Input place: ")
		words["adjective2"] = input("Input a adjective: ")
		words["magical_creature1"] = input("Input a magical creature: ")
		words["adjective3"] = input("Input a adjective: ")
		words["magical_creature2"] = input("Input a magical creature: ")
		words["room"] = input("Input room: ")
		words["noun1"] = input("Input noun: ")
		words["noun2"] = input("Input noun: ")
		words["noun3"] = input("Input noun: ")
		words["adjective4"] = input("Input a adjective: ")
		words["noun4"] = input("Input noun: ")
		words["number"] = input("Input number: ")
		while not check_number(words["number"]):
			print("Please check input format!")
			words["number"] = input("Input a number: ")
		words["verb"] = input("Input verb (ending in ing): ")
		while words["verb"][-3:] != "ing":
			print("Please check input format!")
			words["verb"] = input("Input verb (ending in ing): ")
		words["adjective5"] = input("Input a adjective: ")
		words["noun5"] = input("Input noun: ")
		
	return words

def check_number(num: str):
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	for i in num:
		if i not in numbers:
			return False
	return True

def strlen(string: str):
	len = 0
	for _ in string:
		len += 1
	return len

def char_to_digit(number: str):
	numbers = "0123456789"
	
	for i in range(10):
		if number == numbers[i]:
			return i;