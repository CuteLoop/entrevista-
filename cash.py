import sys




def is_non_negative(number):
	if number >= 0:
			return True
	else:
		print("Please write a non negative value for owed change.")
		return False
		
		
def is_rounded_to_cents(number):
	if number - round(number,2) < 0.000000000001:
		return True
	else:
		print("Please round change to Cents.")
		return False


def get_change():
	
	change_owed=0
	
	IS_NON_NEGATIVE = False
	IS_ROUNDED_TO_CENTS =False
	
	while True:
		
		try:
			change_owed = float(input('Please type how much change is owed, rounded to cents.'))
		except ValueError:
			print("Sorry, please write a number")
			continue
		if is_non_negative(change_owed) and is_rounded_to_cents(change_owed) ==True:
			break
			
	return change_owed		
	
	


def get_cents_owed():

	change_owed = float(sys.argv[1])
	return round(change_owed*100)


def min_number_of_coins():

	coin_values = [25,10,5,1]
	change_owed = int(get_change())


	coin_counter=0
	for coin in coin_values:
		if change_owed/coin > 0:
			print(f'coin counter:{coin_counter} change owed {change_owed}')
			coin_counter+= change_owed//coin
			change_owed = change_owed%coin
	print(f'coin counter:{coin_counter} change owed {change_owed}')	
	return coin_counter
	
	
#min_number_of_coins()
#cents = get_cents_owed()		

number = min_number_of_coins()

print(number)
