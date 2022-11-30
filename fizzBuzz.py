class Solution(object):
    def fizzBuzz(self, n):
        result = []
        for i in range(1, n+1):
            temp = ""
            if i % 15 == 0:
                temp += "FizzBuzz"     
            elif i % 3 == 0:
                temp += "Fizz"
            elif i % 5 == 0:
                temp += "Buzz"
            else:
                temp += str(i)
            result.append(temp)
        return result
            
