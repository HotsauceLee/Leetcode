"""
Note: This is a companion problem to the System Design problem: Design TinyURL.
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
"""

# ============= base62 ================
from urlparse import urlparse
class Codec:
    d = {}
    counter = itertools.count()
    DOMAIN = "http://tinyurl.com/"
    m = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    def __id_to_base62(self, id):
        result = ""
        while id > 0:
            cur_dec = id%62
            result = self.m[cur_dec] + result
            id /= 62
            
        result_len = len(result)
        missing_zeros = 6 - result_len
        return "0"*missing_zeros + result
                
        
    def __base62_to_id(self, base62):
        """
        0 - 9 => 0 - 9
        a - z => 10 - 35
        A - Z => 36 - 61
        """
        id = 0
        for c in base62:
            if ord('0') <= ord(c) <= ord('9'):
                id = id*62 + int(c)
            elif ord('a') <= ord(c) <= ord('z'):
                id = id*62 + (ord(c) - ord('a') + 10)
            else:
                id = id*62 + (ord(c) - ord('A') + 36)
                
        return id
        
    def get_uri(self, url):
        return urlparse(url).path[1:]
        
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        new_id = next(self.counter)
        self.d[new_id] = longUrl
        base62 = self.__id_to_base62(new_id)
        return self.DOMAIN + base62
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        base62 = self.get_uri(shortUrl)
        id = self.__base62_to_id(base62)
        return self.d[id]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
