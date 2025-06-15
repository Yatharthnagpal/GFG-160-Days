class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        if len(arr) <2:
            return -1
        larg=float('-inf')
        sndlarg= float('-inf')
        
        for x in arr:
            if x > larg:
                sndlarg = larg
                larg = x
            elif x< larg and x> sndlarg:
                sndlarg = x
        
        if sndlarg == float('-inf'):
            return -1
        else:
            return sndlarg