"""
There are two properties in the node student id and scores, to ensure that each student will have at least 5 points, find the average of 5 highest scores for each person.

Have you met this question in a real interview? Yes
Example
Given results = [[1,91],[1,92],[2,93],[2,99],[2,98],[2,97],[1,60],[1,58],[2,100],[1,61]]

Return 

"""
# ============ Heap ==============
# Time: O(n)
# Space: O(n)
'''
Definition for a Record
class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score
'''
import heapq
class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, results):
        # Write your code here
        if not results:
            return {}
            
        r = {}
        for record in results:
            if record.id in r:
                heapq.heappush(r[record.id], record.score)
                if len(r[record.id]) > 5:
                    heapq.heappop(r[record.id])
            else:
                r[record.id] = [record.score]
        
        for key, heap in r.iteritems():
            cur_sum = 0
            for score in heap:
                cur_sum += score
            r[key] = cur_sum/5.0
            
        return r
        
