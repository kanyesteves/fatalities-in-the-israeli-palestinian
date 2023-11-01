import pandas as pd

file_csv = "../datasets/fatalities_isr_pse_conflict_2000_to_2023.csv"
treated_file_csv = "../datasets/treated_fatalities_isr_pse_conflict_2000_to_2023.csv"

df = pd.read_csv(file_csv)
print("DataFrame carregado")

new_df = df[['name', 'age', 'citizenship', 'gender', 'date_of_death', 'event_location', 'event_location_district', 'event_location_region', 'killed_by']].copy()


# Tratando valores nulos
gender_mode = new_df.gender.mode()
new_df["gender"].fillna(gender_mode[0], inplace=True)

male_mean = round(new_df.loc[new_df["gender"] == "M"]["age"].median())
female_mean = round(new_df.loc[new_df["gender"] == "F"]["age"].median())

new_df.loc[new_df["gender"] == 'M', 'age'] = new_df.loc[new_df["gender"] == 'M',]["age"].fillna(male_mean)
new_df.loc[new_df["gender"] == 'F', 'age'] = new_df.loc[new_df["gender"] == 'F',]["age"].fillna(female_mean)


# Tratando valores duplicados
new_df[new_df.duplicated() == True].copy()
new_df.drop_duplicates(keep = 'first', inplace = True)


# Exportando DataFrame
print("CSV exportado na pasta ../datasets")
new_df.to_csv(treated_file_csv)