from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

#Sets up and trains a linear regression model from scikit-Learn

#Pre processes the data by scaling/ normalizing the points
def preprocess(X_train, X_test):
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled

#Fits and returns a linear regression model to training data
def train_model(X_train, Y_train):
    model = LinearRegression()
    model.fit(X_train, Y_train)
    return model

#Produces the prediction then evaluates it by the root mean squared error which is then returned
def evaluate_model(model, X_test, Y_test):
    Y_pred = model.predict(X_test)
    mse = mean_squared_error(Y_test, Y_pred)
    print("Predictions:", Y_pred)
    print("Mean Squared Error:", mse)
    return mse, Y_pred
