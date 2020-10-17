class Solution:
    def isValid(self, s: str) -> bool:

        if (s== '' or len(s)==1): 

            return False
        tmp=[]
         
        for i in range (len(s)):
            
            if(s[i]=="(" or s[i]=="[" or s[i]=="{"):
                tmp.append(s[i])
            
            else:
                
                if(len(tmp)==0):
                    return False
                
                if((s[i]==")" and tmp.pop()=="(") or (s[i]=="]"and tmp.pop()=="[") or (s[i]=="}" and tmp.pop()=="{")):
                    continue
                
                else:    
                    return False
                
        
        if (len(tmp)==0):
            return True
        else:
            return False
