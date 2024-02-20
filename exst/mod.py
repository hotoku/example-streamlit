import pandas as pd

_DF = pd.DataFrame({
    "x": [1, 2, 3, 4],
    "x2": [11, 12, 13, 14],
    "y": [10, 20, 30, 40]
})


def get_df() -> pd.DataFrame:
    return _DF
