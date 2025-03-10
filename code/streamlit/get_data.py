import pandas as pd

def load_data():
    d_krankenhaus = pd.read_excel("../../data/cleaned_data/Krankenhäuser.xlsx")
    d_personal = pd.read_excel("../../data/cleaned_data/Personal.xlsx")
    d_kosten = pd.read_excel("../../data/cleaned_data/bereinigte_kosten_deutscher_Krankenhäuser.xlsx")
    d_ausgaben = pd.read_excel("../../data/cleaned_data/jaehrliche-gesundheitsausgaben-in-deutschland-bis-2022.xlsx")
    diagnose_2018 = pd.read_excel("../../data/cleaned_data/final_cleaned/Data_Final_Diagnose_2018.xlsx")
    diagnose_2019 = pd.read_excel("../../data/cleaned_data/final_cleaned/Data_Final_Diagnose_2019.xlsx")
    diagnose_2020 = pd.read_excel("../../data/cleaned_data/final_cleaned/Data_Final_Diagnose_2020.xlsx")
    diagnose_2021 = pd.read_excel("../../data/cleaned_data/final_cleaned/Data_Final_Diagnose_2021.xlsx")
    diagnose_2022 = pd.read_excel("../../data/cleaned_data/final_cleaned/Data_Final_Diagnose_2022.xlsx")
    diagnose_2023 = pd.read_excel("../../data/cleaned_data/final_cleaned/Data_Final_Diagnose_2023.xlsx")
    tode_2010 = pd.read_excel("../../data/cleaned_data/final_cleaned/Data_Final_Tode_2010.xlsx")
    tode_2011 = pd.read_excel("../../data/cleaned_data/final_cleaned/Data_Final_Tode_2011.xlsx")
    tode_2012 = pd.read_excel("../../data/cleaned_data/final_cleaned/Data_Final_Tode_2012.xlsx")
    tode_2013 = pd.read_excel("../../data/cleaned_data/final_cleaned/Data_Final_Tode_2013.xlsx")
    tode_2014 = pd.read_excel("../../data/cleaned_data/final_cleaned/Data_Final_Tode_2014.xlsx")
    tode_2015 = pd.read_excel("../../data/cleaned_data/final_cleaned/Data_Final_Tode_2015.xlsx")
    tode_2016 = pd.read_excel("../../data/cleaned_data/final_cleaned/Data_Final_Tode_2016.xlsx")
    tode_2017 = pd.read_excel("../../data/cleaned_data/final_cleaned/Data_Final_Tode_2017.xlsx")
    tode_2018 = pd.read_excel("../../data/cleaned_data/final_cleaned/Data_Final_Tode_2018.xlsx")
    tode_2019 = pd.read_excel("../../data/cleaned_data/final_cleaned/Data_Final_Tode_2019.xlsx")
    tode_2020 = pd.read_excel("../../data/cleaned_data/final_cleaned/Data_Final_Tode_2020.xlsx")
    tode_2021 = pd.read_excel("../../data/cleaned_data/final_cleaned/data_tode_2021_final.xlsx")
    tode_2022 = pd.read_excel("../../data/cleaned_data/final_cleaned/data_tode_2022_final.xlsx")
    tode_2023 = pd.read_excel("../../data/cleaned_data/final_cleaned/data_tode_2023_final.xlsx")
    tode_insgesamt = pd.read_excel("../../data/cleaned_data/final_cleaned/final_cleaned_insgesamt/tode_insgesamt_nach_jahr.xlsx")
    tode_i_alles = pd.read_excel("../../data/cleaned_data/final_cleaned/final_cleaned_insgesamt/Data_Final_Tode_Insgesamt.xlsx")
    bettenauslastung = pd.read_excel("../../data/cleaned_data/bettenauslastung_2010_bis_2023.xlsx")
    verweildauer = pd.read_excel("../../data/cleaned_data/final_cleaned/Data_Verweildauer.xlsx")

    return d_krankenhaus, d_personal,d_kosten,d_ausgaben, diagnose_2018, diagnose_2019, diagnose_2020, diagnose_2021, diagnose_2022, diagnose_2023, tode_2010, tode_2011, tode_2012, tode_2013, tode_2014, tode_2015, tode_2016, tode_2017, tode_2018, tode_2019, tode_2020, tode_2021, tode_2022, tode_2023, tode_insgesamt, tode_i_alles, bettenauslastung, verweildauer