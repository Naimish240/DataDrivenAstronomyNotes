import numpy as np

def get_features_targets(data):
  # complete this function
  features = np.zeros((4, len(data)))
  features[0] = data['u'] - data['g']
  features[1] = data['g'] - data['r']
  features[2] = data['r'] - data['i']
  features[3] = data['i'] - data['z']
  features = features.T
  
  targets = data['redshift']
  return features, targets


if __name__ == "__main__":
  # load the data
  data = np.load('sdss_galaxy_colors.npy')
    
  # call our function 
  features, targets = get_features_targets(data)
    
  # print the shape of the returned arrays
  print(features[:2])
  print(targets[:2])
