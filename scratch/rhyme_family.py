from itertools import combinations

"""
    Given many sets of possible words this modules consolodates
    the sets into specific rhyming families

    returns a map of family to set union
"""

"""
    Takes two sets, returns percentage of similiar words
"""
def match_percentage(listA,listB):
    return (2.*len(listA&listB))/(len(listA)+len(listB))

"""
    Takes a list of sets 
    returns a map of family to set union
"""
def make_families(listOfSets):
    seen = {}
    set_num = 0
    for s in listOfSets:
        seen[set_num]=[s,False]
        set_num+=1

    mpr = {}
    combs = combinations(listOfSets, 2)
    q = 0
    for i in combs:
        if match_percentage(i[0],i[1]) > .49:
            mpr[q]=i[0]|i[1]
            q+=1
            mark_seen(i[0],seen)
            mark_seen(i[1],seen)
    for s in seen:
        if (not seen[s][1]):
            mpr[q]=seen[s][0]
            q+=1
    return mpr

def mark_seen(setA,seen):
    for s in seen:
        if (seen[s][0]==setA):
            seen[s][1]=True

print make_families([set([1,2,3]),set([1]),set([3,4,5])])
