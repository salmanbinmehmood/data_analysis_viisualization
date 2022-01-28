import matplotlib.pyplot as plt
import pandas as pd
cn_imm=pd.read_excel(r"F:\python\pythonProject\pythonProject\datavisualization\canada_imm\Austria.xlsx",
                     skiprows=range(20))
a=cn_imm.tail(20)
print(a)