#leetcode Challange 1 from Top new comers challenges

#Input: s = "LVIII"
#Output: 58
#Explanation: L = 50, V= 5, III = 3.
#Roman to Integer


class Solution(object):
  def romanToInt(self,s):
    """
    :type s:str
    :rtype: nt
    """
    roman = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

    result=0  #initialiasing result

    for a,b in zip(s,s[1:]):
      if roman[a] <roman[b]:
        result -=roman[a]
      else:
        result+=roman[a]
    return result+ roman[s[-1]]
    

