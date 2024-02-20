import numpy as np
import pandas as pd


def gen_data() -> pd.DataFrame:
    num = 100000
    return pd.DataFrame(dict(
        x=np.random.normal(size=num),
        y=np.random.normal(size=num)
    ))


_DF = gen_data()


def get_df() -> pd.DataFrame:
    return _DF
