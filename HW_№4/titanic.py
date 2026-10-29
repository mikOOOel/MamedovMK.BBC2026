import pandas as pd
import numpy as np
from pathlib import Path

df = pd.read_csv(r'C:\P\python\honer\tested.csv') 
#7
n = int(input())
print(df.head(n))
#8
print(df.tail(5))
#9
print(df.shape)
#===
shape_before = df.shape  
#10
print(df.columns)
#11
print(df.dtypes)
#12?
num_cols = df.select_dtypes(include="number").columns.tolist()
cat_cols = df.select_dtypes(exclude="number").columns.tolist()
#13?
print(df[num_cols].mean(), df[num_cols].median(), df[num_cols].min(), df[num_cols].max(), df[num_cols].std())
#14
print(df["Pclass"].value_counts())
#15
print(df["Embarked"].nunique())
#16
print(df.isna().sum())
#17
data = df.to_numpy()  
print(((df.isna().sum() / data.shape[0]) *100).round(1))
#18
missing = df.isna().sum()
print(missing.idxmax())
#19
age = df["Age"]
print(age.mean(), age.median(), age.min(), age.max(), age.std())
#===
ameanb = age.mean()
amedianb = age.median()
aminb = age.min()
amaxb = age.max()
astdb = age.std()
acountb = age.count()
df["Age"] = df["Age"].fillna(amedianb)
#20
median_age = df["Age"].median()
df["Age"] = df["Age"].fillna(median_age)
#21
age = df["Age"]
print(age.mean(), age.median(), age.min(), age.max(), age.std())
#===
ameana = age.mean()
amediana = age.median()
amina = age.min()
amaxa = age.max()
astda = age.std()
acounta = age.count()
#22
table = pd.DataFrame(
    {
        "Показатель": [
            "Среднее арифметическое",
            "Медиана",
            "Минимальный возраст",
            "Максимальный возраст",
            "Стандартное отклонение",
            "Количество известных значений",
        ],
        "До обработки": [ameanb, amedianb, aminb, amaxb, astdb, acountb],
        "После обработки": [ameana, amediana, amina, amaxa, astda, acounta],
    }
)

print(table)
#23
df = df.dropna(subset=["Embarked"])
#24
cabin_missing = df["Cabin"].isna().mean()
if cabin_missing > 0.5:
    df = df.drop(columns="Cabin")
    print("Столбец 'Cabin' удален")
#===
shape_after = df.shape    
#25
print(df.isna().sum())
#26
print("До обработки:   строк", shape_before[0], ", столбцов", shape_before[1])
print("После обработки: строк", shape_after[0], ", столбцов", shape_after[1])
print("Удалено строк:", shape_before[0] - shape_after[0])
print("Удалено столбцов:", shape_before[1] - shape_after[1])
#31
survived = df["Survived"].to_numpy()
survived_pct = np.mean(survived) * 100
print(survived_pct)
#32
sex = df["Sex"].to_numpy()
survived = df["Survived"].to_numpy()
male_pct = np.mean(survived[sex == "male"]) * 100
female_pct = np.mean(survived[sex == "female"]) * 100
print(male_pct, female_pct)
#33
age = df["Age"].to_numpy()
survived = df["Survived"].to_numpy()
male_mean_age_pct = np.mean(survived[sex=="male"])
female_mean_age_pct = np.mean(survived[sex=="female"])
print(male_mean_age_pct, female_mean_age_pct)
#34
male_mean_age_surv_pct = np.mean(age[(sex=="male") & (survived==1)]) * 100
female_mean_age_surv_pct = np.mean(age[(sex=="female") & (survived==1)]) * 100
print(male_mean_age_surv_pct, female_mean_age_surv_pct) 
#35
ticket_price = df["Fare"].to_numpy()
print(np.min(ticket_price), np.max(ticket_price), np.mean(ticket_price))
#36
print(np.std(age))
#5.1
sex = df["Sex"].to_numpy()
age = df["Age"].to_numpy()
pclass = df["Pclass"].to_numpy()
mask = (sex == "male") & (age > 30) & (pclass == 1)
print(np.sum(mask))
print(df[mask].head(10))
#5.2
survived = df["Survived"].to_numpy()
mask = ((age < 18) | (sex == "female")) & (survived == 1)
print(np.sum(mask))
#5.3
fare = df["Fare"].to_numpy()
ticket_price_3class = df[df["Pclass"] == 3]["Fare"].to_numpy()
ticket_mean_price_3class = np.mean(ticket_price_3class)
mask = (fare > ticket_mean_price_3class) & (pclass == 3)
print(np.sum(mask))
#5.4
port = df["Embarked"].to_numpy()
mask = (age >= 20) & (age <= 40) & (port == "S")
print(np.sum(mask))
#37
result = df.groupby(["Pclass", "Sex"]).agg(
    cnt=("PassengerId", "count"),
    mean_age=("Age", "mean"),
    survival_rate=("Survived", "mean"),
    mean_fare=("Fare", "mean"),
)
result["survival_rate"] *= 100
print(result.round(2))
#===(41)
result.round(2).to_csv(r"C:\P\python\honer\titanic_statistics.csv")
#38
result = df.groupby("Embarked").agg(
    cnt = ("PassengerId", "count"),
    procent = ("Survived", "mean")
)
result["procent"] *= 100
print(result.round(2))
#39
survival_by_class = df.groupby("Pclass")["Survived"].mean() * 100
print(survival_by_class.idxmax())
#40
out_path = Path(__file__).parent / "titanic_processed.csv"
df.to_csv(out_path, index=False)
check = pd.read_csv(out_path)
print(check.shape, df.shape)            
print(check.isna().sum().sum())         
print(check.head())
print(pd.read_csv(r"C:\P\python\honer\titanic_statistics.csv"))
