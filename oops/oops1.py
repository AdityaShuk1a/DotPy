class student:
    def __init__(self, name , marks):
        self.name = name
        self.marks = marks
    def getMarks(self):
        
        s=0
        for i in self.marks:
            s+=i
        s/= len(self.marks)
        return s
            
raju = student("raju", [97,93,91])
print(f"Avg marks of student is {raju.getMarks()}")
# raju.getMarks()