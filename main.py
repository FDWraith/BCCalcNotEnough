def unify(A, B):
    return [ x for x in A if x not in B] + intersect(A,B) + [ x for x in B if x not in A ]
def intersect(A, B):
    return [ x for x in A if x in B ]
def setDiff(A, B):
    return [ x for x in A if x not in B]
def symDiff(A, B):
    return unify( setDiff(A,B), setDiff(B,A))
def cartProd(A, B):
    return [ [a,b] for a in A for b in B]

print unify( [1,2,3], [2,3,4])
print intersect( [1,2,3], [2,3])
print setDiff( [1,2,3], [2,3,4])
print setDiff( [2,3,4], [1,2,3])
print symDiff( [1,2,3], [2,3,4])
print cartProd( [1,2,3], ['red', 'blue', 'green'])
