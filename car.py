class Car:
    def _init_(self,color ,speedlimit,model,company):
        self.color=color
        self.speedlimit=speedlimit
        self.model=model
        self.company=company
    
    def start(self):
        print("started")

    def accelerate(self):
        print("accelerated")
    
