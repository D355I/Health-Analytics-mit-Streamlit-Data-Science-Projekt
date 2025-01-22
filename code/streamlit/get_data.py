import pandas as pd

def load_data():
    d_krankenhaus = pd.read_excel("../../data/cleaned_data/Krankenhäuser.xlsx")
    d_personal = pd.read_excel("../../data/cleaned_data/Personal.xlsx")
    diagnose_2018 = pd.read_excel("../../data/cleaned_data/final_cleaned/Data_Final_Diagnose_2018.xlsx")
    diagnose_2019 = pd.read_excel("../../data/cleaned_data/final_cleaned/Data_Final_Diagnose_2019.xlsx")
    diagnose_2020 = pd.read_excel("../../data/cleaned_data/final_cleaned/Data_Final_Diagnose_2020.xlsx")
    diagnose_2021 = pd.read_excel("../../data/cleaned_data/final_cleaned/Data_Final_Diagnose_2021.xlsx")
    diagnose_2022 = pd.read_excel("../../data/cleaned_data/final_cleaned/Data_Final_Diagnose_2022.xlsx")
    diagnose_2023 = pd.read_excel("../../data/cleaned_data/final_cleaned/Data_Final_Diagnose_2023.xlsx")

    return d_krankenhaus, d_personal, diagnose_2018, diagnose_2019, diagnose_2020, diagnose_2021, diagnose_2022, diagnose_2023