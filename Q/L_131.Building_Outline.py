class Node(object):
    def __init__(self, pos, height):
        self.pos = pos
        self.height = height
        
    def __cmp__(self, other):
        return self.pos - other.pos

import heapq
class Solution:
    # @param buildings: A list of lists of integers
    # @return: A list of lists of integers
    def buildingOutline(self, buildings):
        # write your code here
        if not buildings:
            return []
            
        # max_right = float('-inf')
        # for b in buildings:
        #     max_right = max(max_right, max(b[0], b[1]))
        
        # heights = [[] for i in xrange(max_right + 2)]
        # for b in buildings:
        #     heights[b[0]].append(b[2])
        #     heights[b[1] + 1].append(b[2]*-1)
        
        critical_points = []
        for b in buildings:
            critical_points.append(Node(b[0], b[2]))
            critical_points.append(Node(b[1], b[2]*-1))

        critical_points.sort()
        
        print [(c.pos, c.height) for c in critical_points[-10:]]
        
        result, heap = [], [0]
        cur_start, cur_height = 0, 0
        for c in critical_points:
            # print heap
            if c.height > 0:
                # print "pushing %s" % c.height
                heapq.heappush(heap, c.height*-1)
                if c.height > cur_height:
                    if cur_height != 0:
                        result.append([cur_start, c.pos, cur_height])
                    cur_start = c.pos
                    cur_height = c.height
            else:
                # print "removing %s" % c.height
                heap.remove(c.height)
                heapq.heapify(heap)
                c_height = abs(c.height)
                # print "cur_height: %s, c.height: %s" % (cur_height, c.height)
                if c_height == cur_height:
                    if cur_height != 0:
                        if c_height == 145:
                            print "appending"
                        result.append([cur_start, c.pos, c_height])
                    cur_start = c.pos
                    cur_height = abs(heap[0])
                
        return result
        # first_point = critical_points[0]
        # result, heap = [], [0, first_point.height]
        # cur_height = first_point.height
        # cur_start = first_point.pos
        # for c in critical_points[1:]:
        #     # put in
        #     if c.height > 0:
        #         # print heap
        #         # print "pushing %s" % c.height
        #         insort(heap, c.height)
        #         # higher than before
        #         if c.height > cur_height:
        #             if cur_height != 0:
        #                 result.append([cur_start, c.pos, cur_height])
        #             cur_start = c.pos
        #             cur_height = c.height
        #         # if equal or smaller than before, don't do anything
                    
        #     # kick out
        #     else:
        #         kicked_out_height = abs(c.height)
        #         # if kicking out max height
        #         if cur_height == kicked_out_height:
        #             if cur_height == 145:
        #                 print heap
        #                 print "cur_height: %s, cur_start: %s, c.pos: %s" % (cur_height, cur_start, c.pos)
        #             result.append([cur_start, c.pos, cur_height])
        #             heap.pop()
        #             cur_height = heap[-1]
        #             cur_start = c.pos
        #         # otherwise do nothing
        #         else:
        #             # print heap
        #             # print "removing %s" % kicked_out_height
        #             heap.remove(kicked_out_height)
                    
        # return result
        # heap = [0]
        # outline = [0]*(max_right + 2)
        # for i in xrange(max_right + 2):
        #     for h in heights[i]:
        #         if h > 0:
        #             insort(heap, h)
        #         elif h < 0:
        #             heap.remove(abs(h))
        #     outline[i] = heap[-1]

        # print heights
        # print outline
        # result = []
        # i = 0
        # while i < len(outline):
        #     # move to the start of a building
        #     # don't record flat ground
        #     while i < len(outline) and outline[i] == 0:
        #         i += 1
        #     if i >= len(outline):
        #         break

        #     i_copy = i
        #     # move to the end of the building
        #     while i_copy + 1 < len(outline) and outline[i_copy] == outline[i_copy + 1]:
        #         i_copy += 1
            
        #     start, end = i, i_copy
        #     if start > 1 and outline[start - 1] != 0 and outline[start - 1] > outline[start]:
        #         start -= 1
        #     if end < len(outline) - 1 and outline[end + 1] != 0 and outline[end + 1] > outline[end]:
        #         end += 1
            
        #     result.append([start, end, outline[i]])
        #     i = i_copy + 1

            # # if the build length is 1
            # if i == i_copy:
            #     # if it is at the end
            #     if i == max_right:
            #         result.append([i - 1, i, outline[i]])
            #     # if in the beginning
            #     elif i == 1:
            #         result.append([i, i + 1, outline[i]])
            #     # if in the middle
            #     else:
            #         result.append([i - 1, i + 1, outline[i]])
            #     # move forward by 1
            #     i += 1
            # # building length > 1
            # else:
            #     result.append([start, end, outline[i]])
            #     # go the the next one of the end of the building
            #     i = i_copy + 1
                
        # return result
