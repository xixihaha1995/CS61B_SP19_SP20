class solution(object):
     
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
        if length==2:
            if s[0]=='(':
                if s[1] !=')':
                    return False
                return True
            if s[0]=='[':
                if not s[1] ==']':
                    return False
                return True
            if s[0]=='{':
                if not s[1] =='}':
                    return False
                return True
            return False
        
        indexLeftOne=[]
        indexLeftTwo=[]
        indexLeftThree=[]
        # inOne=0
        # inTwo=0
        # inThree=0
        inRightOne=0
        inRightTwo=0
        inRightThree=0        
        
        w=int(length/2)
        h=2
        index =[[0 for x in range(w)] for y in range(h)]
        left=0;
        #right=w-1
        right=0
        for i in range(0,length):
#            if left>w-1:
#                return False
            if s[i] =='(':
                indexLeftOne.append(left)
                if left>w-1:
                   return False
                index[0][left]=i
                left+=1
            if s[i]==')':
                if len(indexLeftOne)-1-inRightOne<0:
                    return False
                index[1][indexLeftOne[len(indexLeftOne)-1-inRightOne]]=i
                inRightOne+=1
                
            if s[i] =='{':
                indexLeftTwo.append(left)
                if left>w-1:
                   return False
                index[0][left]=i
                left+=1
            if s[i]=='}':
                if len(indexLeftTwo)-1-inRightTwo<0:
                    return False
                index[1][indexLeftTwo[len(indexLeftTwo)-1-inRightTwo]]=i
                inRightTwo+=1
                
            if s[i] =='[':
                indexLeftThree.append(left)
                if left>w-1:
                   return False
                index[0][left]=i
                left+=1
            if s[i]==']':
                if len(indexLeftThree)-1-inRightThree<0:
                    return False                
                index[1][indexLeftThree[len(indexLeftThree)-1-inRightThree]]=i
                inRightThree+=1        
            # if s[i] =='(' or s[i] =='[' or s[i] =='{' :
            #     index[0][left]=i
            #     left+=1
            # else:
            #     index[1][right]=i
            #     #right-=1
            #     right+=1
        """
        from index 0 to index w-1
        check from next pair of parentheses
        """
        for i in range(0,w-1):
            for j in range (i+1, w):
                if index[0][j]<index[1][i] and index[1][i]<index[1][j]:
                    return False
        return True
if __name__=='__main__':
    s= ")["
    solution().isValid(s)
    