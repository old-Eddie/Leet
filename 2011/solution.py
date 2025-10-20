class Solution(object):
    def finalValueAfterOperations(self, operations):
        X=0
        for o in operations:
            if "+" in o:
                X=X+1
            else:
                X=X-1
        return X