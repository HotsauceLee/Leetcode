#================== Dict ===================
# Time: O(n)
# Space: O(1)
# Ideas:
#	1. Use dict to store fixed values, from back to front, check next one.
#	2. Front to the end, substrack smaller values.
class Solution(object):
    d = {
        'I':1,
        'IV':4,
        'V':5,
        'IX':9,
        'X':10,
        'XL':40,
        'L':50,
        'XC':90,
        'C':100,
        'CD':400,
        'D':500,
        'CM':900,
        'M':1000
    }
    
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        c = len(s) - 1
        while c >= 0:
            if c >= 1:
                cur_and_prev_char = s[c-1:c+1]
                if self.d.has_key(cur_and_prev_char):
                    result += self.d[cur_and_prev_char]
                    c -= 2
                    continue
                
            cur_char = s[c]
            result += self.d[cur_char]
            c -= 1
            
        return result
        
        """
        def romanToInt(self, s):
            roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
            z = 0
            for i in range(0, len(s) - 1):
                if roman[s[i]] < roman[s[i+1]]:
                    z -= roman[s[i]]
                else:
                    z += roman[s[i]]
            return z + roman[s[-1]]
        """
        """
        public static int romanToInt(String s) {
	int res = 0;
	for (int i = s.length() - 1; i >= 0; i--) {
		char c = s.charAt(i);
		switch (c) {
		case 'I':
			res += (res >= 5 ? -1 : 1);
			break;
		case 'V':
			res += 5;
			break;
		case 'X':
			res += 10 * (res >= 50 ? -1 : 1);
			break;
		case 'L':
			res += 50;
			break;
		case 'C':
			res += 100 * (res >= 500 ? -1 : 1);
			break;
		case 'D':
			res += 500;
			break;
		case 'M':
			res += 1000;
			break;
		}
	}
	return res;
}
        """
