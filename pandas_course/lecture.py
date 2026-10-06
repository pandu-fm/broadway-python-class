"""
Run: python lecture.py
Each block prints: the QUESTION, then the ANSWER code's result.
Use it live: show the question, let students try, then reveal.
"""
import pandas as pd

# with open("employees.csv", "w") as f:
#     f.write("""emp_id,name,department,salary,years,city
# 1,Asha,Sales,52000,3,Austin
# 2,Bikram,IT,78000,6,Denver
# 3,Chitra,HR,48000,2,Austin
# 4,Deepak,IT,91000,9,Seattle
# 5,Esha,Sales,56000,4,Denver
# 6,Farid,IT,65000,3,Austin
# 7,Gita,HR,51000,5,Seattle
# 8,Hari,Sales,60000,7,Austin
# 9,Isha,IT,83000,8,Denver
# 10,Jay,Sales,45000,1,Seattle
# """)

df = pd.read_csv("employees.csv")


def ask(n, question, answer):
    print(f"\nQ{n}. {question}\n    ANSWER -> {answer}")


# ---------- LEVEL 1: look at data ----------
# ask(1, "How many rows and columns?", df.shape)                       # df.shape
# ask(2, "List the column names.", df.columns.tolist())                # df.columns.tolist()
# ask(3, "Show the first 3 rows.", "\n" + df.head(3).to_string())      # df.head(3)
# ask(4, "Show the last 2 rows.", "\n" + df.tail(2).to_string())       # df.tail(2)
# ask(5, "What type is the 'salary' column?", df["salary"].dtype)      # df["salary"].dtype

# # ---------- LEVEL 2: pick columns ----------
# ask(6, "Get only the 'name' column.", df["name"].tolist())           # df["name"]
# ask(7, "Get 'name' and 'salary' together.",
#     "\n" + df[["name", "salary"]].head(3).to_string())               # double [[ ]]
# ask(8, "Get the salary of the 4th row (index 3).", df["salary"][3])  # df["salary"][3]

# # ---------- LEVEL 3: quick stats ----------
# ask(9, "Average salary?", df["salary"].mean())                       # .mean()
# ask(10, "Highest salary?", df["salary"].max())                       # .max()
# ask(11, "Lowest years of experience?", df["years"].min())            # .min()
# ask(12, "Total salary paid?", df["salary"].sum())                    # .sum()
# ask(13, "How many employees per department?",
#     "\n" + df["department"].value_counts().to_string())              # value_counts()
# ask(14, "How many different cities?", df["city"].nunique())          # .nunique()
# ask(15, "List the unique departments.", df["department"].unique().tolist())  # .unique()

# # ---------- LEVEL 4: new columns ----------
df["monthly"] = df["salary"] / 12
# ask(16, "Add 'monthly' = salary / 12. Show Asha's monthly.",
#     round(df.loc[0, "monthly"], 2))
# print("\n" + df.head(3).to_string())
df["bonus"] = df["salary"] * 0.10
# print("\n" + df.head(3).to_string())

# df.to_csv("employees_with_bonus.csv", index=False)  # save to new file
# ask(17, "Add 'bonus' = 10% of salary. Total bonus for everyone?", df["bonus"].sum())
# df["senior"] = df["years"] >= 5
# ask(18, "Add 'senior' = True if years >= 5. How many seniors?", df["senior"].sum())

# # ---------- LEVEL 5: sort & filter (preview of step 2) ----------
# ask(19, "Sort by salary, highest first. Show top 3 names.",
    # df.sort_values("salary", ascending=False)["name"].head(3).tolist())
# ask(20, "Employees in IT only (names).",
#     df[df["department"] == "IT"]["name"].tolist())
# ask(21, "Employees earning more than 60000 (names).",
#     df[df["salary"] > 60000]["name"].tolist())
# ask(22, "IT employees in Austin or Denver (names).",
#     df[(df["department"] == "IT") & (df["city"].isin(["Austin", "Denver"]))]["name"].tolist())

# # ---------- CHALLENGE ----------
# ask(23, "CHALLENGE: average salary per department?",
#     "\n" + df.groupby("department")["salary"].mean().to_string())    # groupby (step 4)

# df["salary"] = df["salary"].fillna(0)  # Handle empty salary values (read as NaN)
# print(df.head(2).to_string())  # Show rows with salary = 0

import math
import pandas as pd # pip install pandas

"""
series and dataframe are the two main 
data structures in pandas.
"""

name = pd.Series(["Asha", "Bikram", "Chitra", "Deepak"])
age = pd.Series([25, 30, 28, 35])

user_data = pd.DataFrame(
    {"name": name, "age": age}
    )
print(user_data.head(10))  # Show first 2 rows

