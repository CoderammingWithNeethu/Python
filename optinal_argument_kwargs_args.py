def mood_today(*mood):
	if mood:
		return f'Today, I am feeling {mood}'
	else:
		return 'Today, I am feeling neutral'

print(mood_today())
'''
 *args and **kwargs keywords allow you to pass a variable number of arguments to a Python function. 
 *args keyword sends a list of values to a function. 
 **kwargs sends a dictionary to a function.
'''