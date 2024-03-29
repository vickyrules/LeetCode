
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result  = [intervals[0]]
        
        for a,b in intervals[1:]:
        
           
            if a <= result[-1][1]:
                result[-1][1] = max(result[-1][1] ,b)
                
            else:
                result.append([a,b])
                
        return result
            
            
        
#         if len(intervals) <= 1:
#             return intervals
            
#         intervals.sort()
#         result  = []
#         minX =intervals[0][0]
#         maxY =intervals[0][1]
        
#         for a,b in intervals[1:]:
#             # a,b = intervals[i][0],intervals[i][1]
        
#             if a <= maxY:
#                 maxY = max([maxY,b])
                
#             else:
#                 result.append([minX,maxY])
#                 minX = a
#                 maxY = b
        
#         result.append([minX,maxY])
#         return result
            
            
                
          