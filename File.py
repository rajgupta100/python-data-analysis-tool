import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (directly without asking for input)
df = pd.read_csv("titanic_sample.csv")

def menu():
    print("\n===== Advanced Data Analysis Tool =====")
    print("1. Show first 5 rows")
    print("2. Show dataset shape (rows, columns)")
    print("3. Show summary statistics")
    print("4. Show column names")
    print("5. Check missing values")
    print("6. Group by a column")
    print("7. Plot scatter (two numeric columns)")
    print("8. Correlation heatmap")
    print("9. Export summary statistics to CSV")
    print("10. Clean data (fill missing, drop duplicates)")
    print("11. Compare columns with plots (matplotlib)")
    print("12. Exit")

while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        print(df.head())

    elif choice == "2":
        print("Shape:", df.shape)

    elif choice == "3":
        print(df.describe())

    elif choice == "4":
        print("Columns:", df.columns.tolist())

    elif choice == "5":
        print("Missing Values:\n", df.isnull().sum())

    elif choice == "6":
        col = input("Enter column name to group by: ")
        if col in df.columns:
            print(df.groupby(col).size())
        else:
            print("Invalid column name!")

    elif choice == "7":
        col1 = input("Enter first numeric column: ")
        col2 = input("Enter second numeric column: ")
        if col1 in df.columns and col2 in df.columns:
            plt.scatter(df[col1], df[col2])
            plt.xlabel(col1)
            plt.ylabel(col2)
            plt.title(f"{col1} vs {col2}")
            plt.show()
        else:
            print("Invalid column names!")

    elif choice == "8":
        plt.figure(figsize=(8, 6))
        corr = df.corr(numeric_only=True)  # only numeric columns
        sns.heatmap(corr, annot=True, cmap="coolwarm")
        plt.title("Correlation Heatmap")
        plt.show()

    elif choice == "9":
        df.describe().to_csv("summary_export.csv")
        print("Summary exported to summary_export.csv")

    elif choice == "10":
        # Fill numeric missing values with mean
        for col in df.select_dtypes(include="number").columns:
            df[col].fillna(df[col].mean(), inplace=True)

        # Fill categorical missing values with mode
        for col in df.select_dtypes(include="object").columns:
            if df[col].isnull().sum() > 0:
                df[col].fillna(df[col].mode()[0], inplace=True)

        # Drop duplicates
        df.drop_duplicates(inplace=True)
        print("Data cleaned: Missing values filled, duplicates removed.")

    elif choice == "11":
        print("\nChoose Plot Type:")
        print("1. Scatter Plot (numerical vs numerical)")
        print("2. Bar Plot (categorical vs numerical)")
        print("3. Line Plot (numerical trend)")
        plot_choice = input("Enter your plot choice: ")

        if plot_choice == "1":
            col1 = input("Enter first numeric column: ")
            col2 = input("Enter second numeric column: ")
            if col1 in df.columns and col2 in df.columns:
                plt.scatter(df[col1], df[col2], color="blue", alpha=0.6)
                plt.xlabel(col1)
                plt.ylabel(col2)
                plt.title(f"Scatter Plot: {col1} vs {col2}")
                plt.show()
            else:
                print("Invalid column names!")

        elif plot_choice == "2":
            col1 = input("Enter categorical column: ")
            col2 = input("Enter numeric column: ")
            if col1 in df.columns and col2 in df.columns:
                df.groupby(col1)[col2].mean().plot(kind="bar", color="green")
                plt.xlabel(col1)
                plt.ylabel(f"Average {col2}")
                plt.title(f"Bar Plot: {col1} vs {col2}")
                plt.xticks(rotation=45)
                plt.show()
            else:
                print("Invalid column names!")

        elif plot_choice == "3":
            col1 = input("Enter X-axis column (numeric): ")
            col2 = input("Enter Y-axis column (numeric): ")
            if col1 in df.columns and col2 in df.columns:
                plt.plot(df[col1], df[col2], marker="o", color="red")
                plt.xlabel(col1)
                plt.ylabel(col2)
                plt.title(f"Line Plot: {col1} vs {col2}")
                plt.show()
            else:
                print("Invalid column names!")

        else:
            print("Invalid choice!")

    elif choice == "12":
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice, try again!")
