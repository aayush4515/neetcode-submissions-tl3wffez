class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # rows_bucket = [[] for i in range(10)]
        # cols_bucket = [[] for i in range(10)]

        # for i in range(0, len(board)):
        #     for j in range(0, len(board)):
        #         if board[i][j] == '.':
        #             continue
                
        #         rows_bucket[int(board[i][j])].append(i)
        #         cols_bucket[int(board[i][j])].append(j)

        # print(rows_bucket)
        # print(cols_bucket)
            
        # # case I: check for repetition in rows:
        # for bucket in rows_bucket:
        #     if len(set(bucket)) < len(bucket):
        #         return False
        # # case II: check for repetition in columns:
        # for bucket in cols_bucket:
        #     if len(set(bucket)) < len(bucket):
        #         return False
        
        # # case III: check for repetition in 3*3 grids
        # for bucket_r, bucket_c in zip(rows_bucket[1:], cols_bucket[1:]):
        #     for i in range(len(bucket_r) - 1):
        #         r1, r2, c1, c2 = bucket_r[i], bucket_r[i + 1], bucket_c[i], bucket_c[i + 1]

        #         rem_r1 = r1 % 3
        #         rem_r2 = r2 % 3
        #         rem_c1 = c1 % 3
        #         rem_c2 = c2 % 3
        #         # check if grid exceeded
        #         if rem_r2 <= rem_r1 or rem_c2 <= rem_c1:
        #             continue
                
        #         # check for repetition
        #         # calculate manhattan distance
        #         m_distance = abs(r1 - r2) + abs(c1 - c2)

        #         if m_distance <= 4:
        #             print(f"Repeated number: {rows_bucket.index(bucket_r)}")
        #             print("This ran")
        #             return False

        # return True


        rows = defaultdict(set)     # key: row numbers, value: set of numbers in that row
        cols = defaultdict(set)     # key: col numbers, value: set of numbers in that col
        squares = defaultdict(set)  # keys: (r // 3, c // 3), value: set of numbers in that square

        for r in range(9):
            for c in range(9):
                curr_val = board[r][c]
                if curr_val == ".":
                    continue
                if (curr_val in rows[r] or
                    curr_val in cols[c] or
                    curr_val in squares[(r // 3, c // 3)]):
                    return False
                rows[r].add(curr_val)
                cols[c].add(curr_val)
                squares[(r // 3, c // 3)].add(curr_val)
        return True


            


