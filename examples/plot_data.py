import matplotlib.pyplot as plt
import numpy as np

extension_length = np.array([20, 25, 30, 35, 40, 50, 60, 70])
smallest_focal_distance = np.array([344, 278, 252, 226, 206, 176, 160, 146])
focal_length = np.array([154, 97, 41, 30, 21, 20, 9, 6])

plt.xlim([0, 80])
plt.grid('on')
plt.title('Focusing range')
plt.errorbar(extension_length, smallest_focal_distance+focal_length/2.0, yerr=focal_length/2.0, fmt='o')
plt.xlabel('extension length (mm)')
plt.ylabel('distance from lens (mm)')
plt.show()
