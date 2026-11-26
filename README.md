# 📊 SALES DATA ANALYZER
### A Python Project for Data Analysis & Visualization

> Turn raw sales records into useful information with Python!

---

## 🚀 Quick Links

| Explore | Click to Open |
|---|---|
| 💻 **Source Code** | [![View Source Code](https://img.shields.io/badge/VIEW_SOURCE_CODE-green?style=for-the-badge)](sales_data_analyzer.py) |
| 📁 **Sample Dataset** | [![Download Dataset](https://img.shields.io/badge/DOWNLOAD_CSV-blue?style=for-the-badge)](sales_100_records.csv) |
| 🎥 **Watch a Tutorial** | [![Watch Video](https://img.shields.io/badge/WATCH_VIDEO-red?style=for-the-badge)](YOUR_VIDEO_LINK) |

---

## 📌 About the Project

**Sales Data Analyzer** is a simple, menu-driven Python application that helps users load, explore, clean, analyze, and visualize sales data stored in a CSV file.

It is designed as a beginner-friendly project to practise Python programming and popular data analysis libraries. A sample dataset containing **100 records** is included.

## 🧰 Tools & Technologies

- 🐍 **Python 3** – Core programming language
- 🔢 **NumPy** – Numerical calculations
- 🐼 **Pandas** – Data handling and analysis
- 📊 **Matplotlib** – Charts and graphs
- 🎨 **Seaborn** – Statistical data visualization

## 📂 Project Structure

Keep all three files in the same folder:

```text
Sales-Data-Analyzer/
│
├── Data_Visualization.py   # Main Python source code
├── sales_records.csv    # Sample dataset (100 records)
└── README.md                # Project information
```

## ⚙️ Installation & Setup

**Step 1 – Install Python**

Install Python 3 on your computer.

**Step 2 – Install the required libraries**

Open Command Prompt or Terminal and run:

```bash
pip install numpy pandas matplotlib seaborn
```

**Step 3 – Download the project files**

Download the Python file and CSV dataset using the Quick Links above. Keep them in the same folder.

**Step 4 – Run the project**

Open the project folder in VS Code, IDLE, or Terminal and run:

```bash
python Data_Visualization.py
```

**Step 5 – Load the dataset**

From the main menu, select `1. Load Dataset`. When asked for the file path, enter:

```text
sales_records.csv
```

Now the project is ready to use!

---

## 🧭 Main Menu

| No. | Option | Description |
|---:|---|---|
| 1 | Load Dataset | Load a CSV file into the program |
| 2 | Explore Dataset | View rows, columns, data types, and information |
| 3 | Data Cleaning | Find and handle missing values |
| 4 | NumPy Operations | Calculate sum, mean, maximum, minimum, and standard deviation |
| 5 | Search / Sort / Filter | Search for values and sort records |
| 6 | Split Data | Display records grouped by a selected column |
| 7 | Statistical Analysis | View descriptive statistics, variance, standard deviation, and median |
| 8 | Pivot Table | Summarize data using sum, mean, or count |
| 9 | Visualization | Create different types of charts |
| 10 | Save Visualization | Save the latest chart as an image |
| 11 | Exit | Close the application |

## 📈 Visualization Options

The project can create **8 types of visualizations**:

1. **Bar Plot** – Compare sales between products or categories.
2. **Line Plot** – Show values across an ordered sequence.
3. **Scatter Plot** – Explore the relationship between two numeric columns.
4. **Pie Chart** – Display category-wise proportions.
5. **Histogram** – Understand the distribution of numeric values.
6. **Stack Plot** – Compare cumulative values from two numeric columns.
7. **Heatmap** – Display correlations between numeric columns.
8. **Box Plot** – Explore the spread of numeric values across categories.

## 🗃️ About the Sample Dataset

The file `sales_records.csv` contains **100 sample sales records**.

| Column | Details |
|---|---|
| `Order_ID` | Unique order number |
| `Date` | Date of the order |
| `Product` | Product name |
| `Category` | Product category |
| `City` | City where the sale was recorded |
| `Quantity` | Number of units sold |
| `Unit_Price` | Price of one unit |
| `Sales` | Total sales amount |

Sample products include laptops, phones, tablets, headphones, and monitors. The sample cities are in Gujarat.

## 🧪 Things You Can Try

- Calculate the total and average of the `Sales` column using NumPy.
- Filter the `City` column to view records from `Ahmedabad`.
- Create a pivot table with `Product` as the index and `Sales` as the values.
- Create a bar plot using `Product` and `Sales`.
- Generate a heatmap to explore relationships between numeric columns.

## 🎯 Learning Objectives

- Learn how to read CSV files using Pandas.
- Understand basic data cleaning techniques.
- Perform calculations with NumPy.
- Explore and summarize data with Pandas.
- Create charts using Matplotlib and Seaborn.
- Practise Python classes, functions, loops, and conditional statements.

## 💡 Future Improvements

Some ideas to extend this project:

- Add a graphical user interface (GUI).
- Add more chart types and chart customization.
- Export filtered data and analysis results.
- Add date-wise and city-wise sales reports.
- Connect the application to a database.

## ⚠️ Important Notes

- Enter the correct CSV file path when loading a dataset.
- Use numeric columns for calculations and numeric chart axes.
- Create a chart before choosing **Save Visualization**.
- The chart is saved in the program's current working folder unless another path is provided.
- The included CSV contains sample data for educational and demonstration purposes.

## 👨‍💻 Project Information

- **Project Name:** Sales Data Analyzer & Visualization
- **Developed By:** Dharmi Sonani
- **Subject:** Python / Data Analysis

---

### ⭐ Thank You!

Thanks for checking out the Sales Data Analyzer project.

**Quick access:** [Source Code](Data_Visualization.py) · [Sample CSV](sales_records.csv) · [Watch Tutorials](https://www.youtube.com/results?search_query=python+sales+data+analysis+project+beginner)

