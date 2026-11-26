import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class SalesDataAnalyzer:

    def __init__(self):
        self.data = None
        self.last_fig = None

    def load_data(self):
        path = input("Enter CSV file path: ")
        try:
            self.data = pd.read_csv(path)
            print("\nDataset loaded successfully!")
            print(self.data.head())
        except FileNotFoundError:
            print("File not found. Check the path.")
        except Exception as e:
            print("Error:", e)

    def explore_data(self):
        if self.data is None:
            print("Please load dataset first.")
            return

        while True:
            print("\n===== Explore Dataset =====")
            print("1. First 5 rows")
            print("2. Last 5 rows")
            print("3. Column names")
            print("4. Data types")
            print("5. Basic information")
            print("6. Back")
            choice = input("Enter option: ")

            if choice == "1":
                print(self.data.head())
            elif choice == "2":
                print(self.data.tail())
            elif choice == "3":
                print(list(self.data.columns))
            elif choice == "4":
                print(self.data.dtypes)
            elif choice == "5":
                print(self.data.info())
            elif choice == "6":
                break
            else:
                print("Invalid option.")

    def clean_data(self):
        if self.data is None:
            print("Please load dataset first.")
            return

        while True:
            print("\n===== Data Cleaning =====")
            print("1. Show missing values")
            print("2. Fill numeric missing values with mean")
            print("3. Remove rows with missing values")
            print("4. Replace missing values")
            print("5. Back")
            choice = input("Enter option: ")

            if choice == "1":
                print(self.data.isnull().sum())
            elif choice == "2":
                cols = self.data.select_dtypes(include="number").columns
                self.data[cols] = self.data[cols].fillna(self.data[cols].mean())
                print("Numeric missing values filled.")
            elif choice == "3":
                self.data = self.data.dropna()
                print("Rows with missing values removed.")
            elif choice == "4":
                value = input("Enter replacement value: ")
                self.data = self.data.fillna(value)
                print("Missing values replaced.")
            elif choice == "5":
                break
            else:
                print("Invalid option.")

    def numpy_operations(self):
        if self.data is None:
            print("Please load dataset first.")
            return

        cols = self.data.select_dtypes(include="number").columns.tolist()
        if len(cols) == 0:
            print("No numeric columns found.")
            return

        print("Numeric columns:", cols)
        col = input("Enter column name: ")
        if col not in cols:
            print("Invalid column.")
            return

        values = self.data[col].dropna().to_numpy()
        if len(values) == 0:
            print("This column has no values.")
            return

        print("Sum:", np.sum(values))
        print("Mean:", np.mean(values))
        print("Maximum:", np.max(values))
        print("Minimum:", np.min(values))
        print("Standard Deviation:", np.std(values))

    def search_filter(self):
        if self.data is None:
            print("Please load dataset first.")
            return

        col = input("Enter column name: ")
        if col not in self.data.columns:
            print("Column not found.")
            return

        print("1. Sort ascending")
        print("2. Sort descending")
        print("3. Filter by value")
        choice = input("Enter option: ")

        if choice == "1":
            print(self.data.sort_values(col).head(10))
        elif choice == "2":
            print(self.data.sort_values(col, ascending=False).head(10))
        elif choice == "3":
            value = input("Enter value to search: ")
            print(self.data[self.data[col].astype(str).str.lower() == value.lower()])
        else:
            print("Invalid option.")

    def split_data(self):
        if self.data is None:
            print("Please load dataset first.")
            return

        col = input("Enter categorical column: ")
        if col not in self.data.columns:
            print("Column not found.")
            return

        for value in self.data[col].dropna().unique():
            print("\n---", value, "---")
            print(self.data[self.data[col] == value].head())

    def statistics(self):
        if self.data is None:
            print("Please load dataset first.")
            return

        print("\n===== Descriptive Statistics =====")
        print(self.data.describe())
        numeric = self.data.select_dtypes(include="number")
        print("\nVariance:\n", numeric.var())
        print("\nStandard Deviation:\n", numeric.std())
        print("\nMedian:\n", numeric.median())

    def create_pivot_table(self):
        if self.data is None:
            print("Please load dataset first.")
            return

        index_col = input("Enter index column (e.g. Product): ")
        value_col = input("Enter values column (e.g. Sales): ")
        if index_col not in self.data.columns or value_col not in self.data.columns:
            print("Column not found.")
            return

        print("1. Sum")
        print("2. Mean")
        print("3. Count")
        choice = input("Enter option: ")
        functions = {"1": "sum", "2": "mean", "3": "count"}

        if choice in functions:
            result = self.data.pivot_table(
                index=index_col, values=value_col, aggfunc=functions[choice]
            )
            print("\n===== Pivot Table =====")
            print(result)
        else:
            print("Invalid option.")

    def visualize(self):
        if self.data is None:
            print("Please load dataset first.")
            return

        print("\n===== Visualization =====")
        print("1. Bar Plot")
        print("2. Line Plot")
        print("3. Scatter Plot")
        print("4. Pie Chart")
        print("5. Histogram")
        print("6. Stack Plot")
        print("7. Heatmap")
        print("8. Box Plot")
        choice = input("Enter option: ")

        try:
            fig, ax = plt.subplots(figsize=(8, 5))

            if choice in ["1", "2", "3"]:
                x = input("Enter X column: ")
                y = input("Enter Y column: ")
                if x not in self.data.columns or y not in self.data.columns:
                    print("Column not found.")
                    plt.close(fig)
                    return

                if choice == "1":
                    ax.bar(self.data[x].astype(str), self.data[y])
                    ax.set_title("Bar Plot")
                elif choice == "2":
                    ax.plot(self.data[x].astype(str), self.data[y], marker="o")
                    ax.set_title("Line Plot")
                else:
                    ax.scatter(self.data[x], self.data[y])
                    ax.set_title("Scatter Plot")
                ax.set_xlabel(x)
                ax.set_ylabel(y)

            elif choice == "4":
                col = input("Enter categorical column: ")
                if col not in self.data.columns:
                    print("Column not found.")
                    plt.close(fig)
                    return
                counts = self.data[col].value_counts()
                ax.pie(counts, labels=counts.index, autopct="%1.1f%%")
                ax.set_title("Pie Chart")

            elif choice == "5":
                col = input("Enter numeric column: ")
                if col not in self.data.columns:
                    print("Column not found.")
                    plt.close(fig)
                    return
                ax.hist(self.data[col].dropna(), bins=10, edgecolor="black")
                ax.set_title("Histogram")
                ax.set_xlabel(col)
                ax.set_ylabel("Frequency")

            elif choice == "6":
                col1 = input("Enter first numeric column: ")
                col2 = input("Enter second numeric column: ")
                if col1 not in self.data.columns or col2 not in self.data.columns:
                    print("Column not found.")
                    plt.close(fig)
                    return
                if not (pd.api.types.is_numeric_dtype(self.data[col1]) and
                        pd.api.types.is_numeric_dtype(self.data[col2])):
                    print("Please choose numeric columns.")
                    plt.close(fig)
                    return
                ax.stackplot(range(len(self.data)),
                             self.data[col1].fillna(0),
                             self.data[col2].fillna(0),
                             labels=[col1, col2])
                ax.legend()
                ax.set_title("Stack Plot")

            elif choice == "7":
                numeric = self.data.select_dtypes(include="number")
                if numeric.shape[1] < 2:
                    print("At least two numeric columns are needed.")
                    plt.close(fig)
                    return
                sns.heatmap(numeric.corr(), annot=True, ax=ax)
                ax.set_title("Correlation Heatmap")

            elif choice == "8":
                x = input("Enter categorical column: ")
                y = input("Enter numeric column: ")
                if x not in self.data.columns or y not in self.data.columns:
                    print("Column not found.")
                    plt.close(fig)
                    return
                sns.boxplot(data=self.data, x=x, y=y, ax=ax)
                ax.set_title("Box Plot")

            else:
                print("Invalid option.")
                plt.close(fig)
                return

            plt.xticks(rotation=45)
            plt.tight_layout()
            self.last_fig = fig
            plt.show()

        except Exception as e:
            print("Visualization error:", e)
            plt.close("all")

    def save_visualization(self):
        if self.last_fig is None:
            print("Please create a visualization first.")
            return

        name = input("Enter file name (e.g. chart.png): ")
        if not name:
            name = "chart.png"
        self.last_fig.savefig(name, dpi=300)
        print("Visualization saved successfully.")


analyzer = SalesDataAnalyzer()

while True:
    print("\n===== DATA ANALYSIS & VISUALIZATION PROJECT =====")
    print("1. Load Dataset")
    print("2. Explore Dataset")
    print("3. Data Cleaning")
    print("4. NumPy Operations")
    print("5. Search / Sort / Filter")
    print("6. Split Data")
    print("7. Statistical Analysis")
    print("8. Pivot Table")
    print("9. Visualization")
    print("10. Save Visualization")
    print("11. Exit")

    option = input("Enter your option: ")

    if option == "1":
        analyzer.load_data()
    elif option == "2":
        analyzer.explore_data()
    elif option == "3":
        analyzer.clean_data()
    elif option == "4":
        analyzer.numpy_operations()
    elif option == "5":
        analyzer.search_filter()
    elif option == "6":
        analyzer.split_data()
    elif option == "7":
        analyzer.statistics()
    elif option == "8":
        analyzer.create_pivot_table()
    elif option == "9":
        analyzer.visualize()
    elif option == "10":
        analyzer.save_visualization()
    elif option == "11":
        print("Thank you! Program closed.")
        break
    else:
        print("Invalid option. Please try again.")
