# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Churn_Modelling.csv')
X = dataset.iloc[:, 3:13].values
y = dataset.iloc[:, 13].values

# Encoding categorical data
# Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer

labelencoder_X_country = LabelEncoder()
X[:, 1] = labelencoder_X_country.fit_transform(X[:, 1])
labelencoder_X_gender = LabelEncoder()
X[:, 2] = labelencoder_X_gender.fit_transform(X[:, 2])

column_transformer = ColumnTransformer(
    transformers=[
        ('onehot', OneHotEncoder(), [1])
    ],
    remainder='passthrough'  # This will keep the other columns unchanged
)

# Fit and transform the data
X = column_transformer.fit_transform(X)

# Avoiding the dummy variable trap
X = X[:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from keras.models import Sequential
from keras.layers import Dense
#Dropout
from keras.layers import Dropout

#Initiation
classifier = Sequential()

#Ajouter la couche d'entrée et une couche cachée
classifier.add(
    Dense(
        6,
        activation='relu',
        kernel_initializer='uniform',
        input_dim=11
    )
)

classifier.add(Dropout(0.1))

#Ajouter une deuxième couche cachée
classifier.add(
    Dense(
        6,
        activation='relu',
        kernel_initializer='uniform'
    )
)

classifier.add(Dropout(0.1))

#Ajouter la couche de sortie
classifier.add(
    Dense(
        1,
        activation='sigmoid',
        kernel_initializer='uniform'
    )
)

#Reseau de neurones initialisés
#Compiler le réseau de neurones
classifier.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

#Entraîner le réseau de neurones
classifier.fit(
    X_train,
    y_train,
    batch_size=10,
    epochs=100
)

# Prediction des résultats du set de test
y_pred_prob = classifier.predict(X_test)

# Convert probabilities to binary class labels
y_pred = (y_pred_prob > 0.5).astype(int)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

pred_accuracy = (cm[0][0]+cm[1][1])/2000

#Test one particular entry against the model
# New entry
new_entry = np.array([[0.0, 0, 600, 0, 40, 3, 60000, 2, 1, 1, 50000]])

# Feature scaling
new_entry = sc.fit_transform(new_entry)
print(new_entry)

# Make the prediction
new_pred_prob = classifier.predict(new_entry)

# Convert probability to binary class label
new_pred = (new_pred_prob > 0.5).astype(int)

print(f"Prediction: {new_pred[0][0]}")

#KFold cross validation
# from keras.wrappers.scikit_learn import KerasClassifier
# from sklearn.model_selection import cross_val_score
# from sklearn.model_selection import GridSearchCV

# def build_classifier():
#     classifier = Sequential()

#     classifier.add(
#         Dense(
#             6,
#             activation='relu',
#             kernel_initializer='uniform',
#             input_dim=11
#         )
#     )

#     classifier.add(
#         Dense(
#             6,
#             activation='relu',
#             kernel_initializer='uniform'
#         )
#     )

#     classifier.add(
#         Dense(
#             1,
#             activation='sigmoid',
#             kernel_initializer='uniform'
#         )
#     )

#     classifier.compile(
#         optimizer='adam',
#         loss='binary_crossentropy',
#         metrics=['accuracy']
#     )
#     return classifier

# keras_classifier = KerasClassifier(build_classifier, batch_size=10, epochs=100)
# precisions = cross_val_score(keras_classifier, X_train, y=y_train, cv=10, n_jobs=-1)


# mean_acc = precisions.mean()
# acc_variance = precisions.std()

#Grid Search
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import GridSearchCV

def build_classifier(units, optimizer):
    classifier = Sequential()

    classifier.add(
        Dense(
            units=units,
            activation='relu',
            kernel_initializer='uniform',
            input_dim=11
        )
    )

    classifier.add(
        Dense(
            units=units,
            activation='relu',
            kernel_initializer='uniform'
        )
    )

    classifier.add(
        Dense(
            1,
            activation='sigmoid',
            kernel_initializer='uniform'
        )
    )

    classifier.compile(
        optimizer=optimizer,
        loss='binary_crossentropy',
        metrics=['accuracy']
    )
    return classifier

keras_classifier = KerasClassifier(build_classifier)
parameters = {
    'batch_size': [16, 32, 64],
    'epochs': [100, 200, 500],
    'optimizer': ['adam', 'rmsprop'],
    'units': [5, 6, 7, 8, 9, 10, 11]
}

grid_search = GridSearchCV(
    keras_classifier,
    parameters,
    scoring='accuracy',
    cv=10
)

grid_search.fit(X_train, y_train)

best_parameters = grid_search.best_params_
best_accuracy = grid_search.best_score_