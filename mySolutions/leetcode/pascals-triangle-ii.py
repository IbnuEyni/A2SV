class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            prev_row = self.getRow(rowIndex - 1)
            curr_row = [1]
            for i in range(len(prev_row)-1):
                curr_row.append(prev_row[i] + prev_row[i+1])
            curr_row.append(1)
            return curr_row

            
