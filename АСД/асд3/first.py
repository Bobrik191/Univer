import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

def counting_sort(array):
    # Find the maximum value in the array
    max_value = max(array)

    # Initialize count array
    count = [0] * (max_value + 1)

    # Store the count of each element in count array
    for num in array:
        count[num] += 1

    # Generate the sorted array
    sorted_array = []
    for i in range(len(count)):
        for j in range(count[i]):
            sorted_array.append(i)

    # Create animation function
    def update_hist(frame):
        plt.cla()  # Clear the current plot
        current_array = sorted_array[:frame+1]  # Get the array up to the current frame
        plt.hist(current_array, bins=max(current_array), alpha=0.7, rwidth=0.85)
        plt.xlabel('Number')
        plt.ylabel('Frequency')
        plt.title('Counting Sort Animation')

    # Create animation
    fig = plt.figure()
    anim = FuncAnimation(fig, update_hist, frames=len(sorted_array), interval=500, repeat=False)
    plt.show()

    return sorted_array

# Пример использования
array = [4, 2, 5, 1, 3, 2, 5, 4, 3, 1]
counting_sort(array)
