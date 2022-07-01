import sys

def is_non_negative(number):
	if number >= 0:
			return True
	else:
		print("Please write a non negative value for owed change:")
		return False
		
def is_rounded_to_cents(number):

	if abs(number - round(number,2)) ==0:
		return True
	else:
		print("Please round change to Cents:")
		return False


def is_float(number):
	try:
		number = float(number)
	except ValueError:
		print("Sorry, please write a number:")
		return False
		
	return True



def get_float_input():

	"""
	Re-prompt if user fails to provide a float. 

	"""
	while True:
		last_input = input('Change owed:')
		if is_float(last_input):
			float_input = float(last_input)
			print (float_input)
			return float_input
		
def get_change():
			
	"""
	Re-prompt if user fails to provide a non negative number
	or an amount that is not rounded to cents.
	"""
	if len(sys.argv) > 1:
	
		if is_float(sys.argv[1]):
			change_owed = float(sys.argv[1])
		
		while True:
			if is_non_negative(change_owed) and is_rounded_to_cents(change_owed) ==True:
				break	
			change_owed = get_float_input()

		return round(100*change_owed, 2)		
	


def min_number_of_coins(change_owed):

	coin_values = [25,10,5,1]
	change_owed =int(change_owed)


	coin_counter=0
	for coin in coin_values:
		if change_owed/coin > 0:
		#print(f'coin counter:{coin_counter} change owed {change_owed}')
			coin_counter+= change_owed//coin
			change_owed = change_owed%coin
	#prnt(f'coin counter:{coin_counter} change owed {change_owed}')	
	return coin_counter
	
	
#min_number_of_coins()
#cents = get_cents_owed()		


change_owed = int(get_change())
number = min_number_of_coins(change_owed)

print(number)
