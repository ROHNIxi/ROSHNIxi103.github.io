# Comprehensive Python Practice Program with User Interface

def main():
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from sklearn.linear_model import LinearRegression
    import pickle

    while True:
        print("\nChoose an option:")
        print("1. Basic Operations")
        print("2. Data Types and Manipulations")
        print("3. Control Structures")
        print("4. Functions")
        print("5. File Handling")
        print("6. Exception Handling")
        print("7. Libraries (NumPy and Pandas)")
        print("8. Data Visualization")
        print("9. Machine Learning")
        print("10. Pickle Example")
        print("11. Exit")

        choice = input("Enter your choice (1-11): ")

        if choice == "1":
            x, y = 10, 5
            print(f"Sum: {x + y}, Difference: {x - y}, Product: {x * y}, Division: {x / y}")

        elif choice == "2":
            my_list = [1, 2, 3]
            my_dict = {'name': 'Alice', 'age': 25}
            my_tuple = (4, 5, 6)
            my_set = {7, 8, 9}
            print(f"List: {my_list}, Dictionary: {my_dict}, Tuple: {my_tuple}, Set: {my_set}")

        elif choice == "3":
            for i in range(1, 6):
                if i % 2 == 0:
                    print(f"{i} is even")
                else:
                    print(f"{i} is odd")

        elif choice == "4":
            def greet(name):
                return f"Hello, {name}!"

            name = input("Enter your name: ")
            print(greet(name))

        elif choice == "5":
            with open('example.txt', 'w') as f:
                f.write("Hello, File Handling!\n")

            with open('example.txt', 'r') as f:
                print(f"File Content: {f.read()}")

        elif choice == "6":
            try:
                result = 10 / 0
            except ZeroDivisionError:
                print("Cannot divide by zero!")

        elif choice == "7":
            arr = np.array([1, 2, 3])
            print(f"NumPy Array Sum: {arr.sum()}")

            df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
            print("Pandas DataFrame:")
            print(df)

        elif choice == "8":
            x_vals = [1, 2, 3]
            y_vals = [4, 5, 6]
            plt.plot(x_vals, y_vals, marker='o', color='r')
            plt.title("Sample Plot")
            plt.xlabel("X-axis")
            plt.ylabel("Y-axis")
            plt.grid()
            plt.show()

        elif choice == "9":
            X = [[1], [2], [3]]
            y = [1, 2, 3]
            model = LinearRegression()
            model.fit(X, y)
            print(f"Model Coefficients: {model.coef_}, Intercept: {model.intercept_}")

        elif choice == "10":
            X = [[1], [2], [3]]
            y = [1, 2, 3]
            model = LinearRegression()
            model.fit(X, y)

            with open('model.pkl', 'wb') as f:
                pickle.dump(model, f)

            with open('model.pkl', 'rb') as f:
                loaded_model = pickle.load(f)
                print(f"Loaded Model Coefficients: {loaded_model.coef_}")

        elif choice == "11":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
