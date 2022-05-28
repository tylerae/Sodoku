def handle_board(arrays):
    array1 = arrays[0]
    array2 = arrays[1]
    array3 = arrays[2]
    array4 = arrays[3]
    array5 = arrays[4]
    array6 = arrays[5]
    array7 = arrays[6]
    array8 = arrays[7]
    array9 = arrays[8]

    array1 = (' '.join(map(str, array1)))
    array2 = (' '.join(map(str, array2)))
    array3 = (' '.join(map(str, array3)))
    array4 = (' '.join(map(str, array4)))
    array5 = (' '.join(map(str, array5)))
    array6 = (' '.join(map(str, array6)))
    array7 = (' '.join(map(str, array7)))
    array8 = (' '.join(map(str, array8)))
    array9 = (' '.join(map(str, array9)))

    board = f""""
      A B C D E F G H I 
    1 {array1}                    
    2 {array2}                              
    3 {array3}                   
    -----------------
    4 {array3}                  
    5 {array4}               
    6 {array5}               
    -----------------   
    7 {array6}                  
    8 {array7}                
    9 {array8}                  

    """
    return board 