import pandas as pd
xl_file = pd.ExcelFile("Psi Wars For Adeev & Sander/Deck Analyzed Sept 13 2019 DRAFT .xlsx")

dfs = {sheet_name: xl_file.parse(sheet_name) 
          for sheet_name in xl_file.sheet_names}