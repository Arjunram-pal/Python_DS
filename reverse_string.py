class stack:
    
    def __init__(self,max_size):
        
        self.max_size=max_size
        self.top =-1
        self.stack_arr=[None]*max_size
        
        
    def push(self,stri):
        
        if self.top == self.max_size-1:
            print("Stack is empty!!")
            return
        
        for str_ch in stri:
            self.top+=1
            self.stack_arr[self.top]=str_ch
            
    def reverser_str(self):
        
        if self.top==-1:
            print("Stack is empty!!")
            return
        
        while self.top != -1:
            print(self.stack_arr[self.top])
            self.top -=1
            
            
st=stack(5)
name="arjun"
st.push(name)
st.reverser_str()
            