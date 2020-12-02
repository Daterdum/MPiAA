def lcs(X, Y):
    return _lcs(X, Y)[::-1]


def _lcs(X, Y):
    if len(X) == 0 or len(Y) == 0:
        return ""
    elif X[-1] == Y[-1]:
        return X[-1] + _lcs(X[:-1], Y[:-1])
    else:
        X_1 = _lcs(X[:-1], Y)
        Y_1 = _lcs(X, Y[:-1])
        return X_1 if len(X_1) > len(Y_1) else Y_1


if __name__ == "__main__":
    X = "kjhdasd"
    print(X)
    Y = "uiyzxvdasduiuv"
    string = "parapa"
    print(lcs(X, Y))
