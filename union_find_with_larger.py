class quick_union_weighted(object):
    '''dyamic connectivity with logN complexity'''
    def __init__(self,N):
        self.id = list(range(N))
        self.size = [1 for i in range(N)]
        self.larger = list(range(N))
    def find_root(self,p):
        while self.id[p] != p:
            p = self.id[p]
        return p
    def union(self,p,q):
        p_root = self.find_root(p)
        q_root = self.find_root(q)
        if(p_root == q_root):
            return
        elif(self.size[p_root]>=self.size[q_root]):
            self.id[q_root] = p_root
            self.size[p_root] += self.size[q_root]
            if self.larger[p_root]<self.larger[q_root]:
                    self.larger[p_root] = self.larger[q_root]
         else(size[p]<size[q]):
            self.id[p_root] = q_root
            self.size[q_root] += self.size[p_root]
            if self.larger[q_root]<self.larger[p_root]:
                    self.larger[q_root] = self.larger[p_root]
            
    def connected(self,p,q):
        return self.find_root(p) == self.find_root(q)
    def find(self,p):
         p_root = self.find_root(p)
         return self.larger(p_root)
