class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        biS=str(bin(n))[2:]
        while len(biS)<32:
            biS='0'+biS
        reverse=biS[::-1]
        return int(reverse,2)
        
