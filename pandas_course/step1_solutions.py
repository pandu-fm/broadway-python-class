# Peek only AFTER you tried. Copy lines into the EXERCISE block.
q1 = df.shape
q2 = df.columns.tolist()
q3 = df.head(5)
q4 = df["category"]
q5 = df["price"].mean()
q6 = df["quantity"].max()
df["total"] = df["price"] * df["quantity"]
q7 = df["total"].sum()
q8 = df["status"].value_counts()
q9 = df["order_date"].dtype
