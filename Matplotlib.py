import matplotlib.pyplot as plt
#plt.plot([1, 2, 5], [1, 4, 9])
#plt.show()

#plt.title("Sample Plot")

#import matplotlib.pyplot as plt
#x=[1,2,3]
#y=[5,10,15]

#plt.plot(x,y)
#plt.title("Sales Report")
#plt.show()
#plt.xlabel("Months")
#plt.ylabel("Sales")

#months=["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
#sales=[1000, 1500, 2000, 2500, 3000, 3500]

#plt.plot(months,sales)
#plt.title("Sales Report")
#plt.xlabel("Months")
#plt.ylabel("Sales")
#plt.plot(months,sales,color="red")
#plt.show()

#students=["John", "Alice", "Bob", "Eve"]
#marks=[85, 90, 78, 92]

#plt.bar(students,marks,color="green")
#plt.title("Student Marks")
#plt.xlabel("Students")
#plt.ylabel("Marks") 
#plt.show()


students=["John", "Alice", "Bob", "Eve","Hari","Nath","Reddy","Ravi","Suresh","Kumar"]
marks=[85, 90, 78, 92,88, 95, 80, 75, 82, 89]

plt.barh(students,marks,color="orange")
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks") 
plt.show()