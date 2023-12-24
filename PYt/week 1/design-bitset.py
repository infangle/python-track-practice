class Bitset(object):

    def __init__(self, size):
        self.arr=[0]*size
        self.sz=size
        self.on=0
        self.fp=0

    def fix(self, idx):
        self.fp=self.fp%2
#         here what we do 
        if self.fp==1:
            if self.arr[idx]==1:self.on-=1
            #set that bit accoring to curr flip no 
            # here we set zero because after 1 flip it become 1 wherever flip the bit end result find
            self.arr[idx]=0
        else:
            if self.arr[idx]==0:self.on+=1
               # when no of flip is zero then just replace bit by original 1
            self.arr[idx]=1
        
                

    def unfix(self, idx):
        self.fp=self.fp%2
        if self.fp==1:
            if self.arr[idx]==0:self.on+=1
            self.arr[idx]=1
        else:
            if self.arr[idx]==1:self.on-=1
            self.arr[idx]=0
        

    def flip(self):
        self.fp=self.fp+1
        self.fp=self.fp%2

    def all(self):
        self.fp=self.fp%2
        if self.fp>0 and self.on==0:return True
        elif self.fp==0 and self.on==self.sz:return True
        return False
        

    def one(self):
        self.fp=self.fp%2
        if self.fp>0 and self.on==self.sz:return False
        elif self.fp==0 and self.on==0:return False
        return True
        

    def count(self):
        self.fp=self.fp%2
        t=self.on
        if self.fp>0:
            t=self.sz-self.on
        return t
        

    def toString(self):
        self.fp=self.fp%2
        t=0
        if self.fp>0:            
            for i in range(self.sz):
                self.arr[i]=1-self.arr[i]
                t+=self.arr[i]
            self.fp=0
            self.on=t
        return "".join([str(ele) for ele in self.arr])
        
# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()