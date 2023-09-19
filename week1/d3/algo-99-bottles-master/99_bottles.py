def bottle_song(num):
	# write your code here!
	# escape condition
	if num == 1:
		print('1 bottle of beer on the wall, 1 bottle of beer.')
		print('Take one down and pass it around, no more bottles of beer on the wall.')
		print('No more bottles of beer on the wall, no more bottles of beer.')
		print('Go to the store and buy some more, 99 bottles of beer on the wall.')
	else:
		# Recursive print
		print(f'{num} bottles of beer on the wall, {num} bottles of beer.')
		print(f'Take one down and pass it around, {num - 1} bottles of beer on the wall.')
		# Call recursive function
		return bottle_song(num -1)
	
bottle_song(99)