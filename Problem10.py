import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
dataframe = pd.read_csv("C:\Shraddha\ML\line_dataset.csv")  # reading the dataset
#dataset dictionary to display dataset values
dataset_dictionary = {
'Value' : dataframe['Value'].values,
'Class' : dataframe['Class'].values
}
print(pd.DataFrame(dataset_dictionary))

# dividing data equally into training and testing data
values_train, values_test, label_train, label_test = train_test_split(dataset_dictionary['Value'], dataset_dictionary['Class'], random_state=0, train_size=0.5)
# reshaping the data feature and lables into 2D array
values_train = np.array(values_train).reshape(-1, 1)
values_test = np.array(values_test).reshape(-1, 1)

# Normalizing data
normalization = StandardScaler()
values_train = normalization.fit_transform(values_train)
values_test = normalization.transform(values_test)
# fitting the training data into classifier model
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors=3)
model.fit(values_train, label_train)
# Predicting the test set result
predict_class = model.predict(values_test)
print("Predicted Test Samples Output:", predict_class)

# creating a confusion matrix
from sklearn.metrics import confusion_matrix

model_evaluation = confusion_matrix(label_test, predict_class)
print("Confusion matrix:\n", model_evaluation)
# finding model accuracy
count = sum(sum(model_evaluation))
accuracy = (model_evaluation[0, 0] + model_evaluation[1, 1]) / count
print('Accuracy =: ', accuracy)
# finding model sensitivity
model_sensitivity = model_evaluation[0, 0] / (model_evaluation[0, 0] + model_evaluation[0, 1])
print('Sensitivity =: ', model_sensitivity)
# finding model specificity
model_specificity = model_evaluation[1, 1] / (model_evaluation[1, 0] + model_evaluation[1, 1])
print('Specificity =: ', model_specificity)
