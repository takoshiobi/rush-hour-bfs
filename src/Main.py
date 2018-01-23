from Solver import *

"""
Run Program 
$ python3 Main.py ../filename
"""

def main(board):
    """
    Main function to solve the board given as param

    :param board: text file who contains board
    :return: None
    """
    p = BoardSolver(board)
    p.solve()
    p.display()
    for i in p.winner_car_matrix():
        print (i)
    
def readf(file):
    """
    Function used to read data from text file and return this as a string

    :param file: text file with board
    :return: string of given file
    :rtype: str
    """
    with open(file) as f:
        data=f.read()
    return data

def transform(board):
    """
    Transform text file to the board of type list of lists

    :param board: text file representing board
    :return: board
    :rtype: list of lists
    """
    with open(board) as f:
        content = f.readlines() 
    content = [list(x.strip().replace("."," ")) for x in content]
    #content[2][6].replace('>', ' ')   
    for i in content:
        print (i)


if __name__ == "__main__":
    import sys
    print ('Loading solutions:')
    n=str(sys.argv[1])
    print("Initial board")
    transform(n)
    board=readf(n)
    
    main(board)
