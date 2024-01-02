class Robot:

    def __init__(self, width: int, height: int):
        self.width = width -1
        self.height = height -1
        self.location = [0,0]
        self.dir = ["East","North","West","South"]
        self.face = 0
        
    def step(self, num: int) -> None:
        num = num%((self.width + self.height)*2)
        if num == 0 :
            if self.location == [0,0]:
                self.face = 3
            elif self.location == [self.width,0]:
                self.face = 0
            elif self.location ==[self.width,self.height] :
                self.face = 1
            elif self.face == [0,self.height]:
                self.face = 2

        
        while num > 0:
            if self.face == 0:
                num = self.location[0] + num - self.width
                if num <= 0:
                    self.location[0] = self.width + num
                else:
                    self.face = (self.face + 1)%4
                    self.location[0] = self.width
                
            elif self.face == 1:
                num = self.location[1] + num - self.height
                if num <= 0:
                    self.location[1] = self.height + num
                else:
                    self.face = (self.face + 1)%4
                    self.location[1] = self.height
            
            elif self.face == 2:
                num = self.location[0] - num

                if num >=0:
                    self.location[0] = num
                    num = 0
                else:
                    self.face = (self.face + 1)%4
                    self.location[0] = 0
                    num = abs(num)

            elif self.face == 3:
                num = self.location[1] - num

                if num >=0:
                    self.location[1] = num
                    num = 0
                else:
                    self.face = (self.face + 1)%4
                    self.location[1] = 0
                    num = abs(num)

    def getPos(self) -> List[int]:
        
        return self.location

    def getDir(self) -> str:
        
        return self.dir[self.face]
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()