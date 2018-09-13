#This may be too tough to want to figure out for an interview, rather better you just know the concept itself and can explain if questioned about it
, 
def findFirstSubstringOccurrence(s, x):
    
    ##This is the KMP algorithm 
    partial, ret, j = partial1(x), -1, 0
    for i in range(len(s)):
        while j > 0 and s[i] != x[j]:
            j = partial[j - 1]
        if s[i] == x[j]: j += 1
        if j == len(x): 
            ret = i - (j - 1)
            break
    return ret 


def partial1(pattern):
    # Calculates the partial match table: String -> [Int]
    ret = [0]
        
    for i in range(1, len(pattern)):
        j = ret[i - 1]
        while j > 0 and pattern[j] != pattern[i]:
            j = ret[j - 1]
        ret.append(j + 1 if pattern[j] == pattern[i] else j)
    return ret

findFirstSubstringOccurrence("CodefightsIsAwesome", "IA")
findFirstSubstringOccurrence("AABAACAADAABAABA", "AABA") #This needs KMP because of overlap
