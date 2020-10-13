import random as rd

def map_generator():
	lines = [[0 , 0, 0, 0, 0, 0, 0, 0],
			 [0 , 0, 0, 0, 0, 0, 0, 0],
			 [0 , 0, 0, 0, 0, 0, 0, 0],
			 [0 , 0, 0, 0, 0, 0, 0, 0],
			 [0 , 0, 0, 0, 0, 0, 0, 0],
			 [0 , 0, 0, 0, 0, 0, 0, 0],
			 [0 , 0, 0, 0, 0, 0, 0, 0],
			 [0 , 0, 0, 0, 0, 0, 0, 0]]
	fila = 0 
	value = 0

	while fila < 8:
		if value < 8:
			if rd.randint(0, 1) == 1:
				lines[fila][value] = 'X'
			else:
				lines[fila][value] = '0'
			#print(' ',lines[fila][value], end='') # erase this for stop printing the basic map
			value += 1
		elif value == 8:
			value = 0
			fila += 1
			#print() # erase this for stop printing the basic map
	print(lines)
	return lines

# Now create the types of shots functions
# The functions are intended to return points that are going to be set to 0
"""
 a b c
 d e f
 g h i


 X 0 X 0 X 0 
"""

def shot_surround(x_point, y_point):
	points = [[x_point-1, y_point-1],  #a
				  [x_point, y_point-1], #b
				  [x_point+1, y_point-1], #c
				  [x_point-1, y_point],  #d
				  [x_point, y_point],  #e
				  [x_point+1, y_point],  #f
				  [x_point-1, y_point+1],  #g
				  [x_point, y_point+1],  #h
				  [x_point+1, y_point+1]]  #i
	return points
def shot_cross(x_point, y_point):
	points = [[x_point, y_point-1],[x_point-1, y_point],[x_point, y_point],[x_point+1, y_point],[x_point, y_point+1]]
	return points
def shot_ex(x_point, y_point):
	points = [[x_point-1, y_point-1],[x_point+1, y_point-1],[x_point, y_point],[x_point-1, y_point+1],[x_point+1, y_point+1]]
	return points
def shot_slash(x_point, y_point):
	points = [[x_point+1, y_point-1],[x_point, y_point],[x_point-1, y_point+1]]
	return points
def shot_back_slash(x_point, y_point):
	points = [[x_point-1, y_point-1],[x_point, y_point],[x_point+1, y_point+1]]
	return points
def shot_doughnut(x_point, y_point):
	points = [[x_point-1, y_point-1],[x_point, y_point-1],[x_point+1, y_point-1],[x_point-1, y_point],[x_point+1, y_point],[x_point-1, y_point+1],[x_point, y_point+1],[x_point+1, y_point+1]]
	return points
def shot_simple(x_point, y_point):
	points = [[x_point, y_point]]
	return points


def checker(trigger_points): # This is a function for returning the valid values
	# Check if there are negative values or greater to 7 in trigger_points list. Delete the ones that finded
	to_delete = [] # Creating a list for the index of elements to be deleted
	counter = 0 # counter will be appended to "to_delete" list if the element is greater than seven or less than 0
	for i in trigger_points: # First cycle will go wiht each array in list
		for j in i:	# This cycle will check each value
			if counter not in to_delete: 
				if j < 0 or j > 7: # If one of the points is less than zero, delete de two point from array # If one of the points is higher than seven, delete the two points from array
						to_delete. append(counter)
		counter += 1
	to_delete.sort(reverse = True) # Reversing the array for not having index problems while removing the elements from the list
	for i in to_delete: # Cycle for deleting the specified values in "to_delete" list
		trigger_points.pop(i)
	return trigger_points





def interactive_mode():
	board = map_generator()
	#print(board) 
	
	game_on = True

	# Variable to store to get initial number of ships
	initial_ships = 0
	while game_on == True:

		# Cycle for printing the upper columns number
		for j in range(0, 8):
			print(' ', j, end='')
		print()

		board_count = 0
		value_count = 0
		ship_counter = 0

		# Cycle for printing the number of line, with the X's and 0's of the board
		for i in range(0, 8):
			# printing number of line with the 0's corresponding to each line
			separator = '  '
			print(i, separator.join(board[board_count]))
			
			# Ship counter. Checks the number of X's in the line and adds it to its variable
			x = board[board_count]
			ship_counter += x.count('X')
			board_count += 1

		if initial_ships == 0: # Here we check if  the initial value of ships have not been added
			initial_ships += ship_counter # If it have no changed, it will be added the number of ships

		print(ship_counter)

		# Ask input of number of line, number of column and type of shot
		y_coordinate = int(input('Disparo r='))
		if y_coordinate < 0:
			print("Score =0%s"%(initial_ships - ship_counter))
			print("Restantes =0%s"%(ship_counter))
			exit()
		x_coordinate = int(input('Disparo c='))
		# IF statements to check if value is negative or positive
		if x_coordinate < 0:
			# We will print the calculation of the socore and restating 
			print("Score =0%s"%(initial_ships - ship_counter))
			print("Restantes =0%s"%(ship_counter))
			exit()
		shot_type = input('Tipo disparo(-,+,*,x,/,\\,o)=')  # Input shot type (-,+,*,x,/,\\,o): 
		# if statements to check what to do
		if shot_type == '-':
			trigger_points = shot_simple(x_coordinate, y_coordinate)
		elif shot_type == '+':
			trigger_points = shot_cross(x_coordinate, y_coordinate)
		elif shot_type == '*':
			trigger_points = shot_surround(x_coordinate, y_coordinate)
		elif shot_type == 'x':
			trigger_points = shot_ex(x_coordinate, y_coordinate)
		elif shot_type == '/':
			trigger_points = shot_slash(x_coordinate, y_coordinate)
		elif shot_type == '\\':
			trigger_points = shot_back_slash(x_coordinate, y_coordinate)
		elif shot_type == 'o':
			trigger_points = shot_doughnut(x_coordinate, y_coordinate)
		else: 
			print('bad move')

		#print(trigger_points)

		# Passign the trigger points through check function to check if  values are greater to 7 or less than zero
		checker(trigger_points)

		#print(trigger_points)


		# for the values in "trigger points", make changes in map
		"""
		[columna, linea]
		x = columna [0]
		y = fila [1]

		
		board[fila][columna]
		board[y][x]

		"""
		# create a cycle with the list of trigger points
		for i in trigger_points:
			board[i[1]][i[0]] = '0'
		#print(board)




def automatic_mode():
	print('Hola')

def game_mode():
	mode = int(input('\nType game mode:\n \n1) Interactive\n2) Automatic\n3) Exit\n \nMode: '))
	if mode == 1:
		print('\nI N T E R A C T I V E  M O D E\n')
		interactive_mode()
	elif mode == 2:
		print('A U T O M A T I C  M O D E')
		automatic_mode()
	elif mode == 3:
		print('See ya')
		exit()
	else:
		print('\nTry again ...\n')
		game_mode()

game_mode()