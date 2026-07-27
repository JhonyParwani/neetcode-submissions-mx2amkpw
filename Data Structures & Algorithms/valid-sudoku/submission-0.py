class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import Counter
        for i in range(len(board[0])):
            final=""
            for j in range(len(board[0])):
                final=final+board[i][j]
            final=final.replace(".","")
            counter=Counter(final)
            duplicate=[counter for key,value in counter.items() if value>1]
            if len(duplicate)>0:
                return False

        for i in range(len(board[0])):
            final=""
            for j in range(len(board[0])):
                final=final+board[j][i]
            final=final.replace(".","")
            print(final)
            counter=Counter(final)
            duplicate=[counter for key,value in counter.items() if value>1]
            if len(duplicate)>0:
                return False

        from collections import Counter

        for row in range(0, 9, 3):      # 0,3,6
            for col in range(0, 9, 3):  # 0,3,6

                values = ""

                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        values += board[i][j]

                values = values.replace(".", "")
                counter = Counter(values)

                if any(v > 1 for v in counter.values()):
                    return False

        return True
        

        


            

        