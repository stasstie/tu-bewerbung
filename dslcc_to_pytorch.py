import pandas as pd
import zipfile as zf

class Dslcc_to_pytorch:
    pass

def open_data():
    with zf.ZipFile(".data/dscll", "w") as myfile:
        for item in myfile:
            print(item)



