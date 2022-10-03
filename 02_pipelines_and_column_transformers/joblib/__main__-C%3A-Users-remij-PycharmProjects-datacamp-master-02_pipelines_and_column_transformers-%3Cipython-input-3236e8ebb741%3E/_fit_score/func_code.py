# first line: 1
def _fit_score(model, X, y, train_idx, test_idx):
    X_train = X.iloc[train_idx]
    X_test = X.iloc[test_idx]
    y_train = y.iloc[train_idx]
    y_test = y.iloc[test_idx]
    model = clone(model)
    model.fit(X_train, y_train)
    return model.score(X_test, y_test)
