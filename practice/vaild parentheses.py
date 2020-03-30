class Solution(object):
def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        length=len(s)
        if not length%2==0:
            return False
        
        w=int(length/2)
        h=2
        index =[[0 for x in range(w)] for y in range(h)]
        left=0;
        #right=w-1
        right=0
        for i in range(0,length):
            if s[i] =='(' or s[i] =='[' or s[i] =='{' :
                index[0][left]=i
                left+=1
            else:
                index[1][right]=i
                #right-=1
                right+=1
        """
        from index 0 to index w-1
        check from next pair of parentheses
        """
        for i in range(0,w-1):
            for j in range (i+1, w):
                if index[0][j]<index[1][i]:
                    return False
        return True
            
                
