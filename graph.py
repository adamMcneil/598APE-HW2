import matplotlib.pyplot as plt
import numpy as np

base_line_diabetes = [5.77,]
para_diabetes = [1.12, 1.13, 1.15]
stack = [0.62, 0.59]
sort = [0.58, 0.53, 0.53]
diabetes_data = [base_line_diabetes, para_diabetes, stack, sort]

base_line_cancer = [65.09, ]
para_cancer = [21.87, 22.18, ]
stack = [17.59, 17.85]
sort = [10.74, 10.55, 10.93]
cancer_data = [base_line_cancer, para_cancer, stack, sort]

base_line_housing = [180.04,]
para_housing = [43.20, ]
stack = [17.59, 25.40, 22.98]
sort = [15.59, 15.82, 17.33]
housing_data = [base_line_housing, para_housing, stack, sort]

# Calculate the means and standard deviations
diabetes_means = [np.min(data) for data in diabetes_data]
diabetes_std_devs = [np.std(data) for data in diabetes_data]

cancer_means = [np.min(data) for data in cancer_data]
cancer_std_devs = [np.std(data) for data in cancer_data]

housing_means = [np.min(data) for data in housing_data]
housing_std_devs = [np.std(data) for data in housing_data]

# Define categorical x-axis labels
x_labels = ["baseline", "parallism", "stack", "sort"]
x = np.arange(len(x_labels))  # Numeric positions for categorical labels

plt.errorbar(x, diabetes_means, yerr=diabetes_std_devs, capsize=5, linestyle='-', marker='^', color='red', label='Diabetes')
plt.errorbar(x, cancer_means, yerr=cancer_std_devs, capsize=5, linestyle='--', marker='o', color='blue', label='Cancer')
plt.errorbar(x, housing_means, yerr=housing_std_devs, capsize=5, linestyle='-.', marker='D', color='green', label='Housing')

plt.xticks(x, x_labels)  # Set the categorical labels
plt.xlabel('Optimization Stage')
plt.ylabel('Time (sec)')
plt.title('Speed Increase')
plt.ylim(bottom=0)

plt.legend()
plt.legend(loc='upper right')  # Places the legend in the upper-right corner
plt.grid(True)

plt.show()
