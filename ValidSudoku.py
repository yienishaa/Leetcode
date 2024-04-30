class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Check rows and columns 

        for i in range(0,9):
            s = set()
            for j in range(0,9):
                val = board[i][j] #check row

                if val != "." and val in s:
                    return False
                elif val !=".":
                    s.add(val)


        for i in range(0,9):
            s = set()
            for j in range(0,9):
                val = board[j][i] #check col
                if val != "." and val in s:
                    return False
                elif val !=".":
                    s.add(val)

        #for the 9 squares we can think of each square as a separate square and run the above code. But
        #we need the top left cordinate

        start = [(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]

        for i in start:
            s = set()
            for j in range(3):
                for k in range(3):
                    row = i[0]+j
                    col = i[1]+k
                    val = board[row][col]
                    if val != "." and val in s:
                        return False
                    elif val !=".":
                        s.add(val)
        return True

                
