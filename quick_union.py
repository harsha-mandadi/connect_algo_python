class quick_union(object):
    '''connect 2 points by connecting the roots
    Assume a data structure of arrays initialized to its own roots
    union: Set id of P's root to id of Q's root
    find: if p q have same root'''
    def __init__(self,N):
        self.id =list(range(N))
    def find_root(self,p):
        while self.id[p] != p:
            p = self.id[p]
        return p
    def union_two_points(self,p,q):
        '''Avergae time is less compared to quick_find'''
        p_root = self.find_root(p)
        q_root = self.find_root(q)
        if(p_root != q_root):
            self.id[p_root] = q_root
    def find_if_connected(self,p,q):
        return self.find_root(p) == self.find_root(q)
connect = quick_union(10)
connect.union_two_points(2,5)
connect.union_two_points(7,3)
connect.union_two_points(4,3)
connect.union_two_points(2,4)
print(connect.find_if_connected(7,4))




