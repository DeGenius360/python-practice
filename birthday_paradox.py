import datetime
import random
import calendar




def generate_birthdays(max):
	result_list = []
	start = 1
	while start <= max:	
		# generate the random month
		random_month = random.randint(1,12)

		# get maximum number of days in a month
		max_days = calendar.monthrange(datetime.datetime.now().year, random_month)[1]

		# generate random day based on maximum number of days
		random_day = random.randint(1,max_days)

		# generate random birthday
		random_birthday = datetime.datetime(datetime.datetime.now().year, random_month, random_day)

		# get result

		result_list.append(random_birthday)

		#increment the counter
		start += 1
	
	return result_list



def match_birthdays(birthday_list):
	answer = set()
	# search the list for repeating birthdays
	for i in range(len(birthday_list)-1):
		for j in range(i+1, len(birthday_list)):
			if birthday_list[i] == birthday_list[j]:
				answer.add(birthday_list[i])			
	return answer, len(answer) > 0



def match_birthdays_alternative(birthday_list):
	# iterate through the list
	# add the list items to the set
	# if ever the add method returns None, means repeated birthdays
	# add that specific birthday to our answer list
	answer = []
	
	unique = {x for x in birthday_list if birthday_list.count(x) > 1}
	answer.append(unique)
	return answer, len(answer) > 0


def main():
	count = 0
	print("How many birthdays shall I generate? (Max 100)")
	user_input = input(">")
	bNum = int(user_input)
	answer_1 = generate_birthdays(bNum)

	print("Here are {} birthdays".format(int(user_input)))
	for i, birthday in enumerate(answer_1):
		if i != 0:
			print(", ", end="")
		month_name = calendar.month_name[birthday.month]
		date_text = '{} {}'.format(month_name, birthday.day)
		print(date_text, end="")
	print()

	# simulation
	# generate the birthdays 100,000 times
	print("Generating {} birthdays".format(bNum))
	for i in range(100_000):
		# generate the birthdays
		answer = generate_birthdays(bNum)

		if match_birthdays(answer)[1]: # check if there is a match
			count += 1

		# give feedback
		if i % 10000 == 0:
			print("{} simulations run".format(i))


	# analyse your results
	result = round(count/100_000 * 100, 2)
	print('''Out of 100,000 simulations of {} people, there was a
		matching birthday in that group {} times
		'''.format(bNum, count))
	print('''This means that {} people  have a {} % chance  of
		having  a matching birthday in their group.
		That's propably more than you thought
		'''.format(bNum,result))

if __name__ == '__main__':
	main()