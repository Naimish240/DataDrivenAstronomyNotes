import numpy as np
from sklearn.tree import DecisionTreeRegressor

# paste your get_features_targets function here
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

# paste your median_diff function here
def median_diff(predicted, actual):
  return np.median(np.abs(predicted - actual))

# write a function that splits the data into training and testing subsets
# trains the model and returns the prediction accuracy with median_diff
def validate_model(model, features, targets):
  # split the data into training and testing features and predictions
  split = features.shape[0] // 2
  x_train, x_test = features[:split], features[split:]
  y_train, y_test = targets[:split], targets[split:]
  # train the model
  model.fit(x_train, y_train)
  # get the predicted_redshifts
  pred = model.predict(x_test)
  # use median_diff function to calculate the accuracy
  return median_diff(y_test, pred)


if __name__ == "__main__":
  data = np.load('sdss_galaxy_colors.npy')
  features, targets = get_features_targets(data)

  # initialize model
  dtr = DecisionTreeRegressor()

  # validate the model and print the med_diff
  diff = validate_model(dtr, features, targets)
  print('Median difference: {:f}'.format(diff))
