class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def calc_avg(self):
        avg = sum(self.marks)/len(self.marks) 
        print("Average marks of",self.name,"is",avg)       
s1 = student("yogendra",[90,80,70])
s1.calc_avg()