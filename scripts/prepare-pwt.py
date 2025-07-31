import pandas as pd
from kjst_growth_course.data import _data_dir, _get_data_raw

pwt = pd.read_stata(_get_data_raw("pwt1001.dta"))
pwt.to_parquet(_data_dir / "bin" / "pwt.parquet")

