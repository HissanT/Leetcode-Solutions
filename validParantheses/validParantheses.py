class Solution:
    def isValid(self, s: str) -> bool:
        
        opening = {'(':0,'{':1,'[':2}
        close = {')':0,'}':1,']':2}
        counter = -1
        latest = []
        
        for i in range(len(s)):
            for k in range(3):
                if s[i] == list(opening.keys())[k]:
                    latest.append([s[i], k])
                    counter += 1
                    break
                elif s[i] == list(close.keys())[k]:
                    if counter == -1:
                        return False
                    if latest[counter][1] == k:
                        latest.pop()
                        counter -= 1
                        break
                    else:
                        return False

        if counter != -1:
            return False
        return True