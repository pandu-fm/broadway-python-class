# Python Dictionaries — Practice Questions
### Beginner Level — Real Life Examples

---

**1. Contact Book**
Make dict `contacts` with 3 names as keys, phone numbers as values. Print one contact by name.

**2. Add Entry**
Add new contact to `contacts` dict. Print updated dict.

**3. Update Value**
Priya changed her phone number. Update existing key's value (don't add new key).

**4. Remove Entry**
Remove one contact using `.pop()`. Print removed value too.

**5. Safe Remove**
Try remove contact not in dict using `.pop()` with default value (no crash).

**6. Check Existence**
Ask user for name, check `in` contacts dict before printing number. Print "not found" if missing.

**7. Loop All**
Print all contacts as "Name: Number" using `.items()`.

**8. Just Names**
Print only names using `.keys()`.

**9. Just Numbers**
Print only numbers using `.values()`.

**10. Student Grades**
Dict `grades` = subject : marks. Find subject with highest mark.

**11. Grocery Inventory**
Dict `stock` = item : quantity. User buys item, reduce quantity by 1 using `.get()` for safe lookup.

**12. Merge Dicts**
Two dicts `morning_shift`, `evening_shift` (employee : hours). Merge into one using `.update()`.

**13. Nested Dict**
Student record: `{"Amit": {"math": 90, "sci": 85}}`. Access Amit's math marks.

**14. Count Words**
Given a sentence, count each word's frequency into a dict using `.get(word, 0) + 1` pattern.

**15. Menu Price Lookup**
Restaurant menu dict item : price. Ask user for item name, use `.get()` with default "item not available".

---

*Covers: creating dicts, add/update, `.pop()`, `in` check, `.items()`, `.keys()`, `.values()`, `.get()`, `.update()`, nested dicts.*
