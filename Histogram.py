import matplotlib.pyplot as plt
marks=[4,5,45,35,3,55,43,54,67,46,35,67,64,65,89,90,78,56,45,34,23,12,11,10,9,8,7,6,5,4]
plt.hist(marks,bins=5,color="orange",edgecolor='black')
plt.title("Histogram of Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()
