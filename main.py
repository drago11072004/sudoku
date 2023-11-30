from typing import Tuple, List
# No other imports allowed

# PART OF THE DRIVER CODE

def input_sudoku() -> List[List[int]]:
	"""Function to take input a sudoku from stdin and return
	it as a list of lists.
	Each row of sudoku is one line.
	"""
	sudoku= list()
	for _ in range(9):
		row = list(map(int, input().rstrip(" ").split(" ")))
		sudoku.append(row)
	return sudoku

def print_sudoku(sudoku:List[List[int]]) -> None:
	"""Helper function to print sudoku to stdout
	Each row of sudoku in one line.
	"""
	for i in range(9):
		for j in range(9):
			print(sudoku[i][j], end = " ")
		print()

# You have to implement the functions below

def get_block_num(sudoku:List[List[int]], pos:Tuple[int, int]) -> int:
	"""This function takes a parameter position and returns
	the block number of the block which contains the position.
	"""
	if pos[0]<=3 and pos[0]>=1 and pos[1]<=3 and pos[1]>=1:
		return 1
	if pos[0]<=3 and pos[0]>=1 and pos[1]<=6 and pos[1]>=4:
		return 2
	if pos[0]<=3 and pos[0]>=1 and pos[1]<=9 and pos[1]>=7:
		return 3
	if pos[0]<=6 and pos[0]>=4 and pos[1]<=3 and pos[1]>=1:
		return 4
	if pos[0]<=6 and pos[0]>=4 and pos[1]<=6 and pos[1]>=4:
		return 5
	if pos[0]<=6 and pos[0]>=4 and pos[1]<=9 and pos[1]>=7:
		return 6
	if pos[0]<=9 and pos[0]>=7 and pos[1]<=3 and pos[1]>=1:
		return 7
	if pos[0]<=9 and pos[0]>=7 and pos[1]<=6 and pos[1]>=4:
		return 8
	if pos[0]<=9 and pos[0]>=7 and pos[1]<=9 and pos[1]>=7:
		return 9
	# your code goes here

def get_position_inside_block(sudoku:List[List[int]], pos:Tuple[int, int]) -> int:
	"""This function takes parameter position
	and returns the index of the position inside the corresponding block.
	"""
	for i in range(0,2):
		if pos[0]>=4:
			pos[0]=pos[0]-3
		else:
			break
	for i in range(0,2):
		if pos[1]>=4:
			pos[1]=pos[1]-3
		else:
			break
	if pos[0]==1:
		return pos[0]+pos[1]-1
	elif pos[0]==2:
		return pos[0]+pos[1]+1
	elif pos[0]==3:
		return pos[0]+pos[1]+3
	# your code goes here


def get_block(sudoku:List[List[int]], x: int) -> List[int]:
	"""This function takes an integer argument x and then
	returns the x^th block of the Sudoku. Note that block indexing is
	from 1 to 9 and not 0-8.
	"""
	z=(x-1)%3
	p=3*((x-1)//3)
	l1=sudoku[p][3*z:3*(z+1)]
	l2=sudoku[p+1][3*z:3*(z+1)]
	l3=sudoku[p+2][3*z:3*(z+1)]
	l=l1+l2+l3
	# your code goes here
	return list(l)
	

def get_row(sudoku:List[List[int]], i: int)-> List[int]:
	"""This function takes an integer argument i and then returns
	the ith row. Row indexing have been shown above.
	"""
	l=sudoku[i-1]
	# your code goes here
	return list(l)

def get_column(sudoku:List[List[int]], x: int)-> List[int]:
	"""This function takes an integer argument i and then
	returns the ith column. Column indexing have been shown above.
	"""
	l=[]
	for i in range(0,9):
		l.append(sudoku[i][x-1])
	# your code goes here
	return list(l)

def find_first_unassigned_position(sudoku : List[List[int]]) -> Tuple[int, int]:
	"""This function returns the first empty position in the Sudoku. 
	If there are more than 1 position which is empty then position with lesser
	row number should be returned. If two empty positions have same row number then the position
	with less column number is to be returned. If the sudoku is completely filled then return `(-1, -1)`.
	"""
	for i in range(0,9):
		for j in range(0,9):
			if sudoku[i][j]==0:
				return (i+1,j+1)
				n=4
				break
			else:
				n=6
		if n==4:
			break
		
	# your code goes here
	return (-1,-1)

def valid_list(lst: List[int])-> bool:
	"""This function takes a lists as an input and returns true if the given list is valid. 
	The list will be a single block , single row or single column only. 
	A valid list is defined as a list in which all non empty elements doesn't have a repeating element.
	"""
	l1=[]
	for i in range(0,len(lst)):
		if lst[i]!=0:
			l1.append(lst[i])
		else:
			pass
	st=set(l1)
	l2=list(st)
	if len(l1)!=len(l2):
		return False
	else:
		return True

	# your code goes here

def mi(l):
	for i in range(1,10):
		if i in l:
			pass
		else:
			return False
			break
	return True
def valid_sudoku(sudoku:List[List[int]])-> bool:
	"""This function returns True if the whole Sudoku is valid.
	"""
	lt=[]
	for i in range(1,10):
		l1=get_block(sudoku, i)
		lt.append(l1)
	for i in range(1,10):
		l1=get_column(sudoku, i)
		lt.append(l1)
	for i in range(1,10):
		l1=get_row(sudoku, i)
		lt.append(l1)
	for j in range(0,27):
		if valid_list(lt[j])==True:
			pass
		else:
			return False
			break

	# your code goes here
	return True


def get_candidates(sudoku:List[List[int]], pos:Tuple[int, int]) -> List[int]:
	"""This function takes position as argument and returns a list of all the possible values that 
	can be assigned at that position so that the sudoku remains valid at that instant.
	"""
	a=get_block_num(sudoku,pos)
	b=pos[0]
	c=pos[1]
	l=[]
	l1=get_block(sudoku,a)
	l2=get_row(sudoku,b)
	l3=get_column(sudoku,c)
	for i in range(1,10):
		if i not in l1 and i not in l2 and i not in l3:
			l.append(i)
	# your code goes here
	return list(l)

def make_move(sudoku:List[List[int]], pos:Tuple[int, int], num:int) -> List[List[int]]:
	"""This function fill `num` at position `pos` in the sudoku and then returns
	the modified sudoku.
	"""
	rn=pos[0]-1
	cn=pos[1]-1
	sudoku[rn][cn]=num
	# your code goes here
	return sudoku

def undo_move(sudoku:List[List[int]], pos:Tuple[int, int]):
	"""This function fills `0` at position `pos` in the sudoku and then returns
	the modified sudoku. In other words, it undoes any move that you 
	did on position `pos` in the sudoku.
	"""
	# your code goes here
	rn=pos[0]-1
	cn=pos[1]-1
	sudoku[rn][cn]=0
	return sudoku

def sudoku_solver(sudoku: List[List[int]]) -> Tuple[bool, List[List[int]]]:
    """ This is the main Sudoku solver. This function solves the given incomplete Sudoku and returns
    true as well as the solved sudoku if the Sudoku can be solved i.e. after filling all the empty positions the Sudoku remains valid.
    It return them in a tuple i.e. `(True, solved_sudoku)`.

    However, if the sudoku cannot be solved, it returns False and the same sudoku that given to solve i.e. `(False, original_sudoku)`
    """
    # your code goes here
    while find_first_unassigned_position(sudoku) != (-1,-1):
        p = find_first_unassigned_position(sudoku)
        a = get_candidates(sudoku,p)
        for each in a:
            sudoku = make_move(sudoku, p, each)
            if sudoku_solver(sudoku)[0]==False:
                undo_move(sudoku,p)
            else:
                return sudoku_solver(sudoku)
        return (False, sudoku )
    return (valid_sudoku(sudoku), sudoku)
		
			


	# to complete this function, you may define any number of helper functions.
	# However, we would be only calling this function to check correctness.


# PLEASE NOTE:
# We would be importing your functions and checking the return values in the autograder.
# However, note that you must not print anything in the functions that you define above before you 
# submit your code since it may result in undefined behaviour of the autograder.

def in_lab_component(sudoku: List[List[int]]):
	print("Testcases for In Lab evaluation")
	print("Get Block Number:")
	print(get_block_num(sudoku,(4,4)))
	print(get_block_num(sudoku,(7,2)))
	print(get_block_num(sudoku,(2,6)))
	print("Get Block:")
	print(get_block(sudoku,3))
	print(get_block(sudoku,5))
	print(get_block(sudoku,9))
	print("Get Row:")
	print(get_row(sudoku,3))
	print(get_row(sudoku,5))
	print(get_row(sudoku,9))

# Following is the driver code
# you can edit the following code to check your performance.
if __name__ == "__main__":

	# Input the sudoku from stdin
	sudoku = input_sudoku()

	# Try to solve the sudoku
	possible, sudoku = sudoku_solver(sudoku)

	# The following line is for the in-lab component
	in_lab_component(sudoku)
	# Show the result of the same to your TA to get your code evaulated

	# Check if it could be solved
	if possible:
		print("Found a valid solution for the given sudoku :)")
		print_sudoku(sudoku)

	else:
		print("The given sudoku cannot be solved :(")
		print_sudoku(sudoku)
