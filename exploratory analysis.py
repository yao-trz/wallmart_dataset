import pandas as pd
import joblib

df = pd.read_csv("Walmart_Sales.csv")

print("\nNombre de lignes et de colonnes :\n")
print(df.shape[0], "lignes et", df.shape[1], "colonnes")

print("\n Début du DataFrame :\n")
print(df.head(10))

print("\n Fin du DataFrame :\n")
print(df.tail(10))

print("\n Statistiques descriptives :\n")
print(df.describe())

df.set_index('Date', inplace=True, drop=True)
df.index = pd.to_datetime(df.index, dayfirst=True)

print("\n Nombre de valeurs manquantes par colonne :\n")
print(df.isnull().sum())

print("\n Nombre de valeurs uniques par colonne :\n")
print(df.nunique())

print("columns :\n")
print(", ".join(df.columns))

print("\n Types de données par colonne :\n")
print(df.dtypes)

print("\n Vente hebdomadaire moyenne par magasin :\n")
print(df.groupby("Store")["Weekly_Sales"].mean())

print(df["Holiday_Flag"].value_counts())
joblib.dump(df, "Walmart_Sales.pkl")