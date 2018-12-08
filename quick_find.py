class quick_find(object):
    def __init__(self,N):
        self.id = list(range(N))
    def find_if_connected(self,p,q):
        return self.id[p] == self.id[q]
    def union_two_points(self,p,q):
        pid = self.id[p]
        qid = self.id[q]
        for i in range(len(self.id)):
            if self.id[i] == pid:
                self.id[i]=qid
connect = quick_find(10)
connect.union_two_points(2,3)
print(connect.find_if_connected(2,3))




