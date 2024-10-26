import matplotlib.pyplot as plt
squares = [1,4,9,16,25]
plt.plot(squares, linewidth = 5)
plt.ylabel('Values of Squares', fontsize=14)
plt.xlabel('Values', fontsize=14)
plt.title('A Simple Line Graph 2', fontsize=24)
plt.tick_params(axis='both', labelsize=14)
plt.show()