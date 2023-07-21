class stack:
    
    def __init__(self,max_size):
        self.top= -1
        self.max_size=max_size
        self.start=0
        self.stack_arr=[None]*max_size
    
    def push(self, data):
        
        if self.top == self.max_size-1:
            print("Stack is Full!! Can't push the elements on it")
            return
        
        self.top+=1
        self.stack_arr[self.top]=data
        
    def pop(self):
        
        if self.top ==-1:
            print("Stack is already empty!!. Can't pop the element from it")
            return
        
        tem=self.stack_arr[self.top]
        self.top-=1
        
        return tem
    
    def peek(self):
        
        if self.top ==-1:
            print("Stack is already empty!!. Can't pop the element from it")
            return
        
        return self.stack_arr[self.top]
    
    
    def printele(self):
        
        if self.top ==-1:
            print("Stack is already empty!!. Can't pop the element from it")
            return
        
        
        while self.start<=self.top:
            print(self.stack_arr[self.start])
            self.start+=1
            
st=stack(5)
st.push(13)
st.push(14)
st.push(15)
st.pop()
st.printele()

        