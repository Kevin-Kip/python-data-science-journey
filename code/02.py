import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('../assets/02.csv')
print(data)

heights = data['height(cm)']

print("Mean height is {0}".format(heights.mean()))
print("Standard deviation is {0}".format(heights.std()))
print("Min height is {0}".format(heights.min()))
print("Max height is {0}".format(heights.max()))

plt.hist(heights)
plt.title('Height Distribution of US Presidents')
plt.xlabel('height (cm)')
plt.ylabel('number');
plt.show()
