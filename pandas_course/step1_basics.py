"""
PANDAS STEP 1: Load a CSV and look at it  (about 10 minutes)

Setup: pip install pandas
Run:   python step1_basics.py

How: read each LEARN line, run file, then fill the `None` in EXERCISE.
Goal: every CHECK line says PASS.
"""
import pandas as pd

# ---- SETUP: make a small clean CSV ----
with open("sales.csv", "w") as f:
    f.write("""order_id,order_date,customer,category,price,quantity,status
1001,2024-01-05,Anna,Electronics,1200.00,2,Completed
1002,2024-01-06,Ben,Apparel,45.50,1,Completed
1003,2024-01-06,Cara,Kitchen,80.00,3,Cancelled
1004,2024-01-07,Anna,Electronics,1200.00,1,Completed
1005,2024-01-08,Dev,Apparel,89.00,1,Pending
1006,2024-01-09,Eli,Beauty,24.99,4,Completed
1007,2024-01-10,Fay,Electronics,350.00,2,Refunded
1008,2024-01-11,Ben,Apparel,45.50,5,Completed
""")

# ---- LEARN (DataFrame = table, like an Excel sheet) ----
df = pd.read_csv("sales.csv")        # load CSV into a table
print(df.head(3))                    # first 3 rows (tail(n) = last n)
print(df.shape)                      # (rows, columns)
print(df.columns.tolist())           # column names as a list
df.info()                            # types + missing values
print(df["customer"])                # ONE column  -> Series
print(df[["customer", "price"]])     # MANY columns -> double [[ ]]
print(df["price"].mean(), df["price"].max(), df["price"].sum())
print(df["status"].value_counts())   # count of each value
df["total"] = df["price"] * df["quantity"]   # new column = math on columns
print(df.describe())                 # stats for all number columns


# ================= EXERCISE: replace each None =================
df = pd.read_csv("sales.csv")        # fresh copy

q1 = None   # Q1. (rows, columns) tuple
q2 = None   # Q2. column names as a list
q3 = None   # Q3. first 5 rows
q4 = None   # Q4. the "category" column
q5 = None   # Q5. average "price"
q6 = None   # Q6. biggest "quantity"
q7 = None   # Q7. add column "total" = price * quantity, then sum it
q8 = None   # Q8. count of orders per "status"
q9 = None   # Q9. BONUS: dtype of "order_date" (plain text for now)


# ================= CHECK =================
def check(name, ok):
    print(f"{name}: {'PASS' if ok else 'FAIL'}")

print("\n====== CHECK ======")
check("Q1", q1 == (8, 7))
check("Q2", q2 is not None and q2[:7] == ["order_id", "order_date", "customer", "category", "price", "quantity", "status"])
check("Q3", q3 is not None and len(q3) == 5)
check("Q4", q4 is not None and q4.tolist() == df["category"].tolist())
check("Q5", q5 is not None and round(q5, 2) == 379.37)
check("Q6", q6 == 5)
check("Q7", q7 is not None and round(q7, 2) == 5001.96)
check("Q8", q8 is not None and q8["Completed"] == 5)
check("Q9", str(q9) in ("object", "str", "string"))
