"""
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.
"""

# ================ Check flags ================
# Time: O(n)
# Space: O(1)
# Idea:
"""
test(1, "123", true);
test(2, " 123 ", true);
test(3, "0", true);
test(4, "0123", true);  //Cannot agree
test(5, "00", true);  //Cannot agree
test(6, "-10", true);
test(7, "-0", true);
test(8, "123.5", true);
test(9, "123.000000", true);
test(10, "-500.777", true);
test(11, "0.0000001", true);
test(12, "0.00000", true);
test(13, "0.", true);  //Cannot be more disagree!!!
test(14, "00.5", true);  //Strongly cannot agree
test(15, "123e1", true);
test(16, "1.23e10", true);
test(17, "0.5e-10", true);
test(18, "1.0e4.5", false);
test(19, "0.5e04", true);
test(20, "12 3", false);
test(21, "1a3", false);
test(22, "", false);
test(23, "     ", false);
test(24, null, false);
test(25, ".1", true); //Ok, if you say so
test(26, ".", false);
test(27, "2e0", true);  //Really?!
test(28, "+.8", true);  
test(29, " 005047e+6", true);  //Damn = =|||
"""
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False
        # get rid of leading and tailing spaces
        s = s.strip()
        if not s:
            return False

        number_seen = False
        dot_seen = False
        e_seen = False
        number_after_e = True
        for idx, c in enumerate(s):
            if c.isdigit():
                number_seen = True
                # this will be set false when see e
                # and will be set to true if there are digits after e
                number_after_e = True
            # if already seen e or dot, false
            elif c == '.':
                if e_seen or dot_seen:
                    return False
                dot_seen = True
            # if if already seen e or haven't seen digits, false
            elif c == 'e':
                if e_seen or not number_seen:
                    return False
                e_seen = True
                # if no digits after e, false
                number_after_e = False
            # - and + could only appear at the first char or first after e
            elif c == '-' or c == '+':
                if idx != 0 and s[idx - 1] != 'e':
                    return False
            # all other chars are false
            else:
                return False
        # only seen digits and seen digits after e(if e exist)
        return number_seen and number_after_e
