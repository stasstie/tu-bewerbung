import pandas as pd
import zipfile as zf

class Dslcc_to_pytorch:
    pass

    def open_data(sef, dir: str)-> pd.DataFrame:
        with zf.ZipFile(dir, "w") as myfile:
            for item in myfile:
                print(item)



