import matplotlib.pyplot as plt
import numpy as np

# Print all elements in 'elems' one per row.
def print_elems(elems):
	for elem in elems:
		print(elem)

def main():
  X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
  C,S = np.cos(X), np.sin(X)

  plt.plot(X,C)
  plt.plot(X,S)

  plt.show()

if __name__ == '__main__':
  main()
