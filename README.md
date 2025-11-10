# Programming Lab: Cities Data Processing (OOP Lab)

## 🔹 Overview
This project processes city data from a CSV file (`Cities.csv`) in three stages:

1. **Commit 1 – Procedural**  
   - Read CSV, calculate average temperature, filter cities, count unique countries  
   - Code is repetitive and not reusable

2. **Commit 2 – Procedural + Lambda**  
   - Introduced helper functions: `filter()` and `aggregate()`  
   - Used `lambda` for filtering and aggregation  
   - Code is cleaner, readable, and reusable

3. **Commit 3 – OOP**  
   - Organized into `DataLoader` and `Table` classes  
   - `filter()` and `aggregate()` are methods in `Table`  
   - Output is identical to Commit 2, code is modular and maintainable

---

##  Key Features
- Display first 5 cities  
- Average temperature of all cities  
- Cities in Germany  
- Cities in Spain with temperature > 12°C  
- Number of unique countries  
- Average temperature of cities in Germany  
- Maximum temperature of cities in Italy  

**Note:** The outputs are the same for all commits

---

##  Lambda Functions
- Anonymous functions used for short, inline operations  
- Useful for filtering or aggregating data  
- Example:
```python
filter(lambda x: x['country']=='Germany', cities)
aggregate('temperature', lambda x: sum(x)/len(x), cities)