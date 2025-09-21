
import task7
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Sets up model data produced by copiolet, supposed sleep regression study
#Ideally the train and test data are 2 seperate datasets but his one scails the data
#to provide a somewhat different but similarly linear set of data for testsing.
X = [
            [2, 5],
            [3, 6],
            [4, 4],
            [5, 5],
            [6, 6],
            [7, 7],
            [8, 5],
            [9, 6]
        ]
Y = [50, 55, 60, 65, 70, 75, 80, 85]

def test_preprocess():
    X_train, X_test, _, _ = train_test_split(X, Y, test_size=0.25, random_state=42)
    X_train_scaled, X_test_scaled = task7.preprocess(X_train, X_test)
    assert len(X_train_scaled) == len(X_train)
    assert len(X_test_scaled) == len(X_test)

def test_train_and_evaluate():
    X_train, X_test, Y_train, Y_test = task7.train_test_split(X, Y, test_size=0.25, random_state=42)
    X_train_scaled, X_test_scaled = task7.preprocess(X_train, X_test)
    model = task7.train_model(X_train_scaled, Y_train)
    mse, Y_pred = task7.evaluate_model(model, X_test_scaled, Y_test)
    assert mse >= 0
    assert len(Y_pred) == len(Y_test)
