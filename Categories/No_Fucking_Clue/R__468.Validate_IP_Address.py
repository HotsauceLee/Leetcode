"""
Write a function to check whether an input string is a valid IPv4 address or IPv6 address or neither.

IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each ranging from 0 to 255, separated by dots ("."), e.g.,172.16.254.1;

Besides, leading zeros in the IPv4 is invalid. For example, the address 172.16.254.01 is invalid.

IPv6 addresses are represented as eight groups of four hexadecimal digits, each group representing 16 bits. The groups are separated by colons (":"). For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid one. Also, we could omit some leading zeros among four hexadecimal digits and some low-case characters in the address to upper-case ones, so 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address(Omit leading zeros and using upper cases).

However, we don't replace a consecutive group of zero value with a single empty group using two consecutive colons (::) to pursue simplicity. For example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.

Besides, extra leading zeros in the IPv6 is also invalid. For example, the address 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.

Note: You may assume there is no extra space or special characters in the input string.

Example 1:
Input: "172.16.254.1"

Output: "IPv4"

Explanation: This is a valid IPv4 address, return "IPv4".
Example 2:
Input: "2001:0db8:85a3:0:0:8A2E:0370:7334"

Output: "IPv6"

Explanation: This is a valid IPv6 address, return "IPv6".
Example 3:
Input: "256.256.256.256"

Output: "Neither"

Explanation: This is neither a IPv4 address nor a IPv6 address.
"""

class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        def ipv4(addr):
            groups = addr.split('.')
            # must have 4 groups
            # min ipv4: 0.0.0.0 or 1.1.1.1
            if len(groups) != 4 or len(addr) < 7:
                return False
                
            for g in groups:
                # must have digits and # <= 3
                if not g or len(g) > 3:
                    return False
                # leading zero not allowed
                if g[0] == '0' and len(g) > 1:
                    return False

                try:
                    value = int(g)
                    # must between 0 and 255
                    if value < 0 or value > 255: return False
                    # for case like '-0'
                    if value == 0 and g[0] != '0': return False
                except:
                    return False
                    
            return True
            
        def ipv6(addr):
            groups = addr.split(':')
            # min ipv6: 0:0:0:0:0:0:0:0
            if len(groups) != 8 or len(addr) < 15:
                return False
                
            for g in groups:
                # empty token not allowed
                if not g or len(g) > 4:
                    return False
                    
                for c in g:
                    c_ascii = ord(c)
                    # check if digit is valid
                    is_digit, is_upper, is_lower = False, False, False
                    if ord('0') <= c_ascii <= ord('9'):
                        is_digit = True
                    if ord('a') <= c_ascii <= ord('f'):
                        is_lower = True
                    if ord('A') <= c_ascii <= ord('F'):
                        is_upper = True
                        
                    if not (is_digit or is_upper or is_lower):
                        return False
                        
            return True
            
        if ipv4(IP): return "IPv4"
        if ipv6(IP): return "IPv6"
        
        return "Neither"
        
        


# import re
# class Solution(object):
#     def validIPAddress(self, IP):
#         if re.match('(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])', IP) is not None:
#             return "IPv4"
#         if re.match('(([0-9a-fA-F]{1,4}):){7}([0-9a-fA-F]{1,4})', IP) is not None:
#             return "IPv6"
            
#         return "Neither"

            
