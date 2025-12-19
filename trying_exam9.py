
import pandas as pd
import matplotlib.pyplot as plt

df = None
last_plot = None

def main_menu():   
    print("\n---Data Analysis & Visualization program ----")
    print("1.load dataset")
    print("2.explore data")
    print("3.handle missing data")
    print("4.Data visulization")
    print("5.Descriptive statistics")
    print("6.Dataframe operation")
    print("7.Save visualization")
    print("8.Exist")

def load_dataset():
    global df
    X = input("Enter the name of dataset(csv file)")
    try:
        df = pd.read_csv(X)
        print("Dataset depicts successfully")
    except Exception as e:
        print("issuse showing in loading")
        
def explore_data():
    if df is None:
        print("Please load dataset first!")
        return

    print("\n== Explore Data ==")
    print("1. Display first 5 rows")
    print("2. Display last 5 rows")
    print("3. Display column names")
    print("4. Display data types")
    print("5. Display basic info")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        print(df.head())
    elif choice == 2:
        print(df.tail())
    elif choice == 3:
        print(df.columns)
    elif choice == 4:
        print(df.dtypes)
    elif choice == 5:
        print(df.info())
    else:
        print("Invalid choice")

def handle_missing_data():
    if df is None:
        print("Please load dataset firt")
        return
    print("Handle missing value")
    print("1.Display rows with missing values")
    print("2.Fill missing values with mean")
    print("3.Drop rows with missing values")
    print("4.Replace missing values with a specific value")
    
    choice = int(input("Enter your choice (1-4)"))
    
    if choice == 1:
        print("\n--Row with missing value--")
        print(df[df.isnull().any(axis = 1)])
        
    elif choice == 2:
        print("\n--Filling missing value with mean:")
        df_filled = df.fillna(df.mean(numeric_only =True))
        print(df_filled)
        
    elif choice == 3:
        print("\n--Drop rows with missing value--")
        df_dropped = df.dropna()
        print(df_dropped)
        
    elif choice == 4:
        replace_value = input("Enter the value to replace missing value with:")
        print("\n--Replace missing value with a specific value--")
        df_replaced = df.fillna(replace_value)
        
    else:
        print("\n--Invaild choice.Please enter the number again")
        
def data_visulization():
    global last_plot
    if df is None:
        print("load data first")
        return
    print("\n--Data visulization")
    print("1.Bar plot")
    print("2.line plot")
    print("3.scatter pot")
    print("4.Pie chart")
    print("5.Histogram")
    print("6.stack plot")
    
    choice = int(input("Enter your choice(1-6)"))
    
    if choice == 1:
        def bar_plot():
            plt.bar(df["product"] , df["Sale"])
            plt.xticks(rotation = 50)
            plt.title("sales by product")
            plt.xlabel("product")
            plt.ylabel("Sales")
            plt.legend()
            plt.show()
            
    elif choice == 2:
        def line_plot():
            plt.plot(df["year"], df["sale"], marker='o')
            plt.title("Sales Trend by Year")
            plt.xlabel("Year")
            plt.ylabel("Sales")
            plt.legend()
            plt.show()
            
    elif choice == 3:
        def scatter_plot():
            plt.scatter(df["Price"], df["Sale"])
            plt.title("Sale trend by year")
            plt.xlabel("Price")
            plt.ylabel("Sales")
            plt.legend()
            plt.show()
            
    elif choice == 4:
        def pie_chart():
            city_counts =df["city"].value_counts()
            plt.pie(city_counts,autocapt='%1.1f%')
            plt.title("Sale Distribution by city")
            plt.legend(city_counts.index,title="city",loc="best")
            plt.show()
            
    elif choice == 5:
        def Histogram():
            plt.hist(df["Sales"].dropna(),bins=5,label="Sales Distribution")
            plt.title("Sales Histrogram")
            plt.xlabel("Sales")
            plt.ylabel("Frequency")
            plt.legend()
            plt.show()
            
    elif choice == 6:
        def stack_plot():
            years = df["year"]
            sales = df["sale"].fillna(0)
            prices =df["price"]

            plt.stackplot(years, sales, prices, labels=["Sales", "Price"])
            plt.title("Sales & Price Stack Plot")
            plt.xlabel("Year")
            plt.ylabel("Values")
            plt.legend(loc="upper left")
            plt.show()
            
            
def descriptive_statistics():
    if df is None:
        print("Please load dataset first!")
        return
    print("\n== Descriptive Statistics ==")
    print(df.describe())
    
    
def dataframe_operation():
    if df is None:
        print("Please load dataset first")
        return
    
    print("\n--Dataframe Operation")
    print("1.select column")
    print("2.Filter rows")
    print("3.sort values")
    
    if choice == 1:
        col = input("Enter column name")
        print(df[col])
    elif choice == 2:
        col = input("Enter column name")
        val =input("Enter value to filter")
        print(df[df[col]==val])
    elif choice == 3:
        col = input("Enter column name to sort ")
        print(df.sort_values(by=col))
    else:
        print("invaild")
        
        
        
def save_visualization():
    global last_plot

    if last_plot is None:
        print("First create a graph using mobile data")
        return

    filename = input("Enter file name : ")
    last_plot.savefig(filename)
    print("Graph saved successfully!")
    
    
while True:
    main_menu()
    choice = int(input("Enter your choice(1-7)"))
    
    if choice == 1:
        load_dataset()
    elif choice == 2:
        explore_data()
    elif choice == 3:
        handle_missing_data()
    elif choice == 4:
        data_visulization()
    elif choice == 5:
        descriptive_statistics()
    elif choice == 6:
        dataframe_operation()
    elif choice == 7:
        save_visualization()
    elif choice == 8:
        print("program run successfully")
        break
    else:
        print("Invalid choice")
        


            

                       
    