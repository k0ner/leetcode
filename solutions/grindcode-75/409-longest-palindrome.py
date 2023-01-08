class Solution:
    def longestPalindrome(self, s: str) -> int:
        import collections
        freq = list(collections.Counter(s).values())

        sum_even = 0
        sum_odds = 0
        odd_exists = False
        for num in freq:
            if not num & 1:
                sum_even += num
            else:
                odd_exists = True
                sum_odds += num-1
        sum_odds += 1 if odd_exists else 0
        return sum_even + sum_odds


if __name__ == '__main__':
    #7
    print(Solution().longestPalindrome(s="abccccdd"))
    #1
    # print(Solution().longestPalindrome(s="a"))
    #2
    # print(Solution().longestPalindrome(s="bb"))
    #983
    print(Solution().longestPalindrome(s="civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"))
