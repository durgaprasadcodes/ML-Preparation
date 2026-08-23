# 📊 Matplotlib Learning Roadmap (4 Days)

> A beginner-friendly roadmap to learn **Matplotlib** for **Data Analysis** and **Machine Learning**.

---

## 🎯 Goal

By the end of this roadmap, you will be able to:

- Create different types of charts
- Customize visualizations
- Work with Pandas DataFrames
- Build multiple plots in a single figure
- Save charts as images
- Prepare for Exploratory Data Analysis (EDA) in Machine Learning

---

# 📅 Day 1 - Introduction & Basic Plots

## 📚 Topics

- What is Matplotlib?
- Introduction to `pyplot`
- Creating a Figure
- Line Plot
- Multiple Line Plots
- Labels
- Title
- Legend
- Grid

## 💻 Example

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)

plt.title("Sales")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.grid(True)

plt.show()
```

### ✅ Practice

- Plot two different lines on the same graph.
- Add titles and labels.
- Experiment with legends and grids.

---

# 📅 Day 2 - Most Important Charts

## 📚 Topics

- Bar Chart
- Horizontal Bar Chart
- Scatter Plot
- Histogram
- Pie Chart

## 💻 Examples

### Bar Chart

```python
plt.bar(names, marks)
```

### Horizontal Bar Chart

```python
plt.barh(names, marks)
```

### Scatter Plot

```python
plt.scatter(age, salary)
```

### Histogram

```python
plt.hist(data)
```

### Pie Chart

```python
plt.pie(values, labels=labels)
```

### ✅ Practice

Create every chart using your own sample dataset.

---

# 📅 Day 3 - Customization

## 📚 Topics

### Figure Size

```python
plt.figure(figsize=(8,5))
```

### Customize

- Colors
- Line Styles
- Markers
- Marker Size
- Transparency (`alpha`)
- Rotate X-axis Labels
- Axis Limits

```python
plt.xlim()

plt.ylim()
```

### Color Formats

- `"red"`
- `"blue"`
- `"green"`
- Hex Colors (`#FF5733`)
- RGB Tuples

### ✅ Practice

Customize every chart created on Day 2.

---

# 📅 Day 4 - Subplots & Saving Figures

## 📚 Topics

### Subplots

```python
plt.subplot()
```

### Multiple Plots

```python
fig, ax = plt.subplots()
```

### Save Figure

```python
plt.savefig("graph.png")
```

### Tight Layout

```python
plt.tight_layout()
```

### Working with Pandas

```python
df.plot()

df["Salary"].plot(kind="hist")
```

### ✅ Practice

Create a dashboard with 4 different plots using subplots.

---

# 📌 Important Functions

```python
plt.plot()

plt.bar()

plt.barh()

plt.scatter()

plt.hist()

plt.pie()

plt.figure()

plt.subplot()

plt.subplots()

plt.xlabel()

plt.ylabel()

plt.title()

plt.legend()

plt.grid()

plt.xlim()

plt.ylim()

plt.savefig()

plt.tight_layout()

plt.show()
```

---

# 📊 Mini Projects

## 1. Student Performance Analysis

Visualize:

- Subject Marks
- Attendance
- Average Marks
- Grade Distribution

---

## 2. Sales Dashboard

Visualize:

- Monthly Sales
- Revenue
- Profit
- Regional Sales

---

## 3. Employee Dataset

Visualize:

- Salary Distribution
- Department Count
- Age Distribution
- Gender Ratio

---

## 4. IPL Dataset

Visualize:

- Team Wins
- Top Run Scorers
- Toss Decisions
- Most Wickets

---

# ✅ Learning Checklist

## Day 1

- [ ] What is Matplotlib?
- [ ] pyplot
- [ ] Figure
- [ ] Line Plot
- [ ] Multiple Lines
- [ ] Labels
- [ ] Title
- [ ] Legend
- [ ] Grid

---

## Day 2

- [ ] Bar Chart
- [ ] Horizontal Bar Chart
- [ ] Scatter Plot
- [ ] Histogram
- [ ] Pie Chart

---

## Day 3

- [ ] Figure Size
- [ ] Colors
- [ ] Line Styles
- [ ] Markers
- [ ] Marker Size
- [ ] Alpha
- [ ] X-axis Rotation
- [ ] Axis Limits

---

## Day 4

- [ ] Subplots
- [ ] Multiple Figures
- [ ] Save Figure
- [ ] Tight Layout
- [ ] Pandas Integration

---

# 🚀 After Completing This

Continue your Machine Learning roadmap:

```text
Python
    ↓
NumPy
    ↓
Pandas
    ↓
Matplotlib ✅
    ↓
Seaborn
    ↓
Scikit-learn
    ↓
Machine Learning
    ↓
Deep Learning
```

---

# 🎯 Outcome

After completing this roadmap, you will be able to:

- 📈 Create professional data visualizations.
- 📊 Perform Exploratory Data Analysis (EDA).
- 📉 Present insights using charts.
- 🤖 Build a strong visualization foundation for Machine Learning and Data Science.

---

## ⭐ Happy Learning!

> "A picture is worth a thousand rows of data."