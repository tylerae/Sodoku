# 1. Name:
#      -Tyler Elms-
# 2. Assignment Name:
#      Lab 06 : Sudoku Program
# 3. Assignment Description:
#      -Its meant to treat the sodoku board as an appendable list of lists-
# 4. What was the hardest part? Be as specific as possible.
#      -The hardest part was correctly appending the lists with the user choice-
# 5. How long did it take for you to complete the assignment?
#      -6-



from sklearn.svm import l1_min_c
from handle_file_f import handle_file
from handle_board_f import handle_board
from handle_input_f import handle_input

print("Draft for Sodoku game...")
arrays = handle_file()

def main():
    board = handle_board(arrays)
    print(board)

    user = input("Specify a coordinate to edit or 'Q' to save and quit: ").upper()

    if user == 'Q':
        handle_input(arrays, user)

    number = input("What number goes in {}?".format(user))


    dueled = handle_input(arrays,user)
    xAxis, yAxis = dueled

    


    
    if is_valid(arrays, number, yAxis , xAxis , board) == 2:
        number = int(number)
        l1 = arrays[yAxis]
        l1[xAxis] = number
    
    print(board)
            



    
def is_valid(arrays, number, yAxis , xAxis , board):
    for items in arrays:
        if number not in arrays[yAxis]:
            for x in range(len(items)):
                if items[xAxis] == number:
                    print('Invalid Move')
                else:
                    place = 2
                    return place
        else:
            print('Invalid Move')


    
def running(arrays):
    if (all([isinstance(item, int) for item in arrays])) == True:
        return 'stop'

    if ([isinstance(item, str) for item in arrays]) == True: 
        return True

while True:
    main()
    if running == 'stop':
        False
    


            



        
        






