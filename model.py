def train_regression(table, train_variables, target): 
    regressor = LinearRegression()
    X = table[train_variables]
    y = table[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    regressor.fit(X_train, y_train)
    return regressor

def predict_values(model, values):
    y_pred = model.predict(values)
    return y_pred

def train_clustering(table, train_variables, num_clusters=n): 
    