# ============ BFS + DFS ==============
class Solution(object):
	def findLadders(self, start, end, dict):
		if not start or not end or not dict:
			return []
		if start == end:
		    return [[start, end]]
		
		# Build transform dict	
		one_letter_transform = {}
		dict.update([start, end])
		for d in dict:
			one_letter_transform[d] = set()
			for c in xrange(len(d)):
				for l in xrange(ord('a'), ord('z') + 1):
					cur_letter = chr(l)
					if cur_letter == d[c]: continue
					cur_word = d[:c] + cur_letter + d[c+1:]
					if cur_word in dict:
						one_letter_transform[d].add(cur_word)

        # BFS
		q = collections.deque([start])
		visited = set([start])
		dist = 0
		found = False
		while len(q) > 0 and not found:
			cur_len = len(q)
			for i in xrange(cur_len):
				cur_word = q.pop()
				for trans in one_letter_transform[cur_word]:
					if trans == end:
						found = True
						break
					if trans not in visited:
						q.appendleft(trans)
						visited.add(trans)
				if found: break
			dist += 1
			if found: break
				
		# Return if not found
		if not found: return []
		
		def dfs(level, max_level, word, end, cur_path, result, trans_map, visited):
			if level > max_level:
				return
			if level == max_level:
				if word == end:
					result.append(cur_path[:])
				return
				
			for next_word in trans_map[word]:
				if next_word in visited:
					continue
				cur_path.append(next_word)
				visited.add(next_word)
				dfs(level + 1, max_level, next_word, end, cur_path, result, trans_map, visited)
				visited.remove(next_word)
				cur_path.pop()
		
		visited = set([start])
		result = []
		dfs(0, dist, start, end, [start], result, one_letter_transform, visited)
		return result
