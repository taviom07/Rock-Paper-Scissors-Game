from random import choice

#counters for games wons 
userGame = 0
compGame = 0
# flag to stop the game
flag = True

# loop while the user wants to continue playing
while(flag):
	print('Let''s play a Rock Paper Scissors Game')
	
	# user set to zero to enter the loop to set the correct value
	user = 0
	while(user <1 or user >3):
		user = int(input('Enter a number: 1. Rock, 2. Paper, 3. Scissors \n'))
		userStr = ''
	
		if(user == 1):
			userStr = 'Rock'
		elif(user == 2):
			userStr = 'Paper'
		elif(user == 3):
			userStr = 'Scissors'
		else:
			print('Invalid input, please try one more time')
			
	# initiate the loop, for computer to choose a different choice than the user
	compStr = userStr 
	while(compStr == userStr):
		compStr = choice(['Rock', 'Paper', 'Scissors'])
	
	# compare choices to get the winner
	if(userStr == 'Rock'):
		if(compStr == 'Paper'):
			print('You Choose: {} \nComputer Choose: {}' .format(userStr,compStr))
			print("Computer won!")
			compGame += 1
			print('User Games: {}	Computer Games: {}'.format(userGame, compGame))
		elif(compStr == 'Scissors'):
			print('You Choose: {} \nComputer Choose: {}' .format(userStr,compStr))
			print('You Won!')
			userGame += 1
			print('User Games: {}	Computer Games: {}'.format(userGame, compGame))
	elif(userStr == 'Paper'):
		if(compStr == 'Scissors'):
			print('You Choose: {} \nComputer Choose: {}' .format(userStr,compStr))
			print("Computer won!")
			compGame += 1
			print('User Games: {}	Computer Games: {}'.format(userGame, compGame))
		elif(compStr == 'Rock'):
			print('You Choose: {} \nComputer Choose: {}' .format(userStr,compStr))
			print('You Won!')		
			userGame += 1
			print('User Games: {}	Computer Games: {}'.format(userGame, compGame))
	elif(userStr == 'Scissors'):
		if(compStr == 'Rock'):
			print('You Choose: {} \nComputer Choose: {}' .format(userStr,compStr))
			print("Computer won!")
			compGame += 1
			print('User Games: {}	Computer Games: {}'.format(userGame, compGame))
		elif(compStr == 'Paper'):
			print('You Choose: {} \nComputer Choose: {}' .format(userStr,compStr))
			print('You Won!')
			userGame += 1
			print('User Games: {}	Computer Games: {}'.format(userGame, compGame))
	
	# check if player want to continue
	again = input('Want to play one more time? Y/N \n')
	if(again == 'Y' or again == 'y'):
		# flag set to true if player want to continue game
		flag = True  
	else:
		# flag set to false if player want to end game
		flag = False
	
		
	
	
