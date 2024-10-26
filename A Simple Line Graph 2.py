import matplotlib.pyplot as plt
input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.plot(input_values,squares, linewidth=5)
plt.ylabel('Values of Squares', fontsize=14)
plt.xlabel('Values', fontsize=14)
plt.title('A Simple Line Graph', fontsize=14)
plt.tick_params(axis='both', labelsize=15)
plt.show()
