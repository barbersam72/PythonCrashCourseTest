import csv
import matplotlib.pyplot as plt
import numpy as np

def load_data(filename):
    distances = []
    velocities = []
    
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        
        for row in reader:
            distance = float(row[1]) * 3.086e19  # Convert distance from Mpc to km
            velocity = float(row[2])
            distances.append(distance)
            velocities.append(velocity)
    
    return distances, velocities

def plot_graph(distances, velocities):
    plt.scatter(distances, velocities)
    plt.xlabel('Distance (km)')
    plt.ylabel('Velocity')
    plt.title('Velocity vs Distance')

    # Perform linear fit
    slope, intercept = np.polyfit(distances, velocities, 1)
    fit_line = slope * np.array(distances) + intercept
    plt.plot(distances, fit_line, color='red', label='Linear Fit')

    # Calculate inverse of slope, multiply by 0.96, and convert to billions of years
    inverse_slope = 1 / slope
    inverse_slope *= 0.96
    inverse_slope /= 3.154e16  # Convert from seconds to billions of years
    plt.text(0.1, 0.9, f'Age: {inverse_slope:.2f} billion years', transform=plt.gca().transAxes)

    plt.legend()
    plt.show()

filename = 'galaxies.csv'
distances, velocities = load_data(filename)
plot_graph(distances, velocities)