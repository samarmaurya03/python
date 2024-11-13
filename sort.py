from matplotlib import pyplot as plt

x=[1,2,3,4,5,6]
y=[5,10,15,20,25,30]
plt.plot(x,y,marker="o",ms=10,mec="black",mfc="red")

plt.title("line graph")
plt.xlabel("x-axis") # Corrected function name to 'xlabel'
plt.ylabel("y-axis") # Corrected function name to 'ylabel'
plt.show()