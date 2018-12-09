class quick_union_weighted(object):
    '''dyamic connectivity with logN complexity'''
    def __init__(self,N):
        self.id = list(range(N))
        self.size = [1 for i in range(N)]
    def find_root(self,p):
        while self.id[p] != p:
            p = self.id[p]
        return p
    def union_two_points(self,p,q):
        p_root = self.find_root(p)
        q_root = self.find_root(q)
        if(p_root == q_root):
            return
        elif(self.size[p_root]>=self.size[q_root]):
            self.id[q_root] = p_root
            self.size[p_root] += self.size[q_root]
        elif(size[p]<size[q]):
            self.id[p_root] = q_root
            self.size[q_root] += self.size[p_root]
    def find_if_connected(self,p,q):
        return self.find_root(p) == self.find_root(q)
connect = quick_union_weighted(10)
connect.union_two_points(2,5)
connect.union_two_points(7,3)
connect.union_two_points(4,3)
connect.union_two_points(2,3)
print(connect.find_if_connected(7,4))


