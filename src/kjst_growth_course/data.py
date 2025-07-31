from pathlib import Path

import pandas as pd

_data_dir = Path(__file__).parent / "data"

def _get_data_raw(file: str) -> Path: 
    f = _data_dir / "raw" / file
    if f.exists():
        return f.resolve()
    else:
        raise FileNotFoundError

def _get_data(file: str) -> Path:
    f = _data_dir / "bin" / file
    if f.exists():
        return f.resolve()
    else:
        raise FileNotFoundError
    
def load(name: str, *, columns: list[str] | None = None) -> pd.DataFrame:
    """
    Load installed data

    Parameters
    ----------
    name: str
        Name of the dataset. Possible values are:
        * pwt : Penn World Table v10.01

    columns: list[str]
        List of columns to load.  

    Return
    ------
    Pandas DataFrame object

    """
    return pd.read_parquet(_get_data(name + ".parquet"), columns=columns)
