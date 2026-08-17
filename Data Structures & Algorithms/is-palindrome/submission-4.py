class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        string = ""
        for j in s:
            if j.isalnum():
                string += j
            else:
                pass
        print(string)

        n=len(string)
        for i in range(0,n):
            if string[i] == string[n-i-1]:
                pass
            else:
                return False
        return True
