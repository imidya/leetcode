import string
import random


class Codec:

    def __init__(self):
        self.mapping = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        encoding = 'http://tinyurl.com/'
        if longUrl in self.mapping.keys():
            return self.mapping[longUrl]
        else:
            cands = string.ascii_uppercase + string.ascii_lowercase + string.digits
            tinyurl = encoding + ''.join(random.choice(cands) for _ in range(6))
            self.mapping[longUrl] = tinyurl
            return tinyurl



    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        for k in self.mapping.keys():
            if self.mapping[k] == shortUrl:
                return k
        return None

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

if __name__ == '__main__':
    url = 'https://leetcode.com/problems/design-tinyurl'
    codec = Codec()
    print(codec.encode(url))
    print(codec.decode(codec.encode(url)))
