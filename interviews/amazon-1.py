"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] 
the number of days you have to wait after the ith day to get a warmer temperature. 

If there is no future day for which this is possible, keep 
answer[i] == 0 instead.
 
Example 1:
                      [(1-0),(2-1),(6-2),(5-3),(5-4),]
Input: temperatures = [73,74,75,71,69,72,76,73] Output: [1,1,4,2,1,1,0,0]
                                 i        j  
                            t[j] > t[i] return false
                      
Example 2:

Input: temperatures = [30,40,50,60] Output: [1,1,1,0]

Example 3:

Input: temperatures = [30,60,90] Output: [1,1,0]

"""

def daily_temperatures(temps):
          output = [0] * len(temps)
          stack =[]
          for idx, current_temp in enumerate(temps):
               while len(stack) > 0 and  current_temp > temps[stack[-1]]:
                    last_temp_idx = stack.pop()
                    output[last_temp_idx] = idx - last_temp_idx
               stack.append(idx)
          return output



print(daily_temperatures([73,74,75,71,69,72,76,73]))

print(daily_temperatures([30,40,50,60]))