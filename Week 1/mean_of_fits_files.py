# Write your mean_fits function here:
from astropy.io import fits

def mean_fits(arr):
  data = fits.open(arr[0])[0].data
  for img in arr[1:]:
    data += fits.open(img)[0].data
  data /= len(arr)
  return data


if __name__ == '__main__':
  
  # Test your function with examples from the question
  data  = mean_fits(['image0.fits', 'image1.fits', 'image2.fits'])
  print(data[100, 100])

  # You can also plot the result:
  import matplotlib.pyplot as plt
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()