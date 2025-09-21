from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Assuming SimpleRegressor is defined above or imported
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

def test_load_data():
    reg = SimpleRegressor()
    X, Y = reg.load_data()
    assert len(X) == len(y) == 8
    assert isinstance(X[0], list)

def test_preprocess():
    reg = SimpleRegressor()
    # X, y = reg.load_data()
    X_train, X_test, _, _ = train_test_split(X, Y, test_size=0.25, random_state=42)
    X_train_scaled, X_test_scaled = reg.preprocess(X_train, X_test)
    assert len(X_train_scaled) == len(X_train)
    assert len(X_test_scaled) == len(X_test)

def test_train_and_evaluate():
    reg = SimpleRegressor()
    X, Y = reg.load_data()
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=42)
    X_train_scaled, X_test_scaled = reg.preprocess(X_train, X_test)
    reg.train(X_train_scaled, Y_train)
    mse, Y_pred = reg.evaluate(X_test_scaled, Y_test)
    assert mse >= 0
    assert len(Y_pred) == len(Y_test)
