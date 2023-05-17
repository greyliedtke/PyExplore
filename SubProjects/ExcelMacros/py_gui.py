from tkinter.filedialog import askopenfilename
import pandas as pd

# Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)

pd_df = pd.read_excel(filename)

pd_df['new_col'] = [12, 32, 12, 18]
pd_df['double_col'] = pd_df['col_1']*2

pd_df.to_excel('grey2.xlsx')
