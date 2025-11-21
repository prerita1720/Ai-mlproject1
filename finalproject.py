import numpy as np


class DataAnalytics:




    def _init_(self):
        self.arr = None

    # Array Creation

    def create_array(self):
        print("\nSelect the type of array to create:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            n = int(input("Enter number of elements: "))
            elements = list(map(int, input("Enter elements separated by space: ").split()))
            self.arr = np.array(elements[:n])

        elif choice == 2:
            r = int(input("Enter number of rows: "))
            c = int(input("Enter number of columns: "))
            total = r * c
            elements = list(map(int, input(f"Enter {total} elements separated by space: ").split()))
            self.arr = np.array(elements).reshape(r, c)

        elif choice == 3:
            x = int(input("Enter number of blocks: "))
            r = int(input("Enter number of rows: "))
            c = int(input("Enter number of columns: "))
            total = x * r * c
            elements = list(map(int, input(f"Enter {total} elements separated by space: ").split()))
            self.arr = np.array(elements).reshape(x, r, c)

        else:
            print("Invalid choice")

        print("\nArray created successfully:")
        print(self.arr)

    # Indexing and Slicing 

    def indexing_slicing(self):
        if self.arr is None:
            print("No array found. Create an array first.")
            return

        print("\nChoose an operation:")
        print("1. Indexing")
        print("2. Slicing")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            if self.arr.ndim == 1:
                idx = int(input("Enter index: "))
                print("Result:", self.arr[idx])

            elif self.arr.ndim == 2:
                r = int(input("Enter row index: "))
                c = int(input("Enter column index: "))
                print("Result:", self.arr[r, c])

        elif choice == 2:
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print("Sliced Array:\n", self.arr[start:end])

    # ---------- COMBINE OR SPLIT ----------

    def combine_split(self):
        print("\n1. Combine Arrays")
        print("2. Split Array")
        choice = int(input("Enter choice: "))

        if choice == 1:
            second = list(map(int, input("Enter second array elements separated by space: ").split()))
            new_arr = np.array(second)
            result = np.concatenate((self.arr, new_arr))
            print("Combined Array:", result)

        elif choice == 2:
            parts = int(input("Enter number of parts: "))
            result = np.array_split(self.arr, parts)
            print("Split result:", result)

    # Math Operations 

    def math_operations(self):
        if self.arr is None:
            print("Create an array first.")
            return

        print("\nChoose a math operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        choice = int(input("Enter choice: "))

        elements = list(map(int, input("Enter second array elements separated by space: ").split()))
        second = np.array(elements).reshape(self.arr.shape)

        if choice == 1:
            result = self.arr + second
        elif choice == 2:
            result = self.arr - second
        elif choice == 3:
            result = self.arr * second
        elif choice == 4:
            result = self.arr / second

        print("\nResult:")
        print(result)

    # Search / Slot / Filtered 

    def search_sort_filter(self):
        if self.arr is None:
            print("Create an array first.")
            return

        print("\n1. Search element")
        print("2. Sort array")
        print("3. Filter array (greater than a value)")
        choice = int(input("Enter choice: "))

        if choice == 1:
            value = int(input("Enter element to search: "))
            result = np.where(self.arr == value)
            print("Found at index:", result)

        elif choice == 2:
            print("Sorted array:")
            print(np.sort(self.arr))

        elif choice == 3:
            value = int(input("Enter minimum value: "))
            print("Filtered array:")
            print(self.arr[self.arr > value])

    # ---------- AGGREGATE & STATISTICS ----------

    def aggregates_statistics(self):
        if self.arr is None:
            print("Create an array first.")
            return

        print("\nSum:", np.sum(self.arr))
        print("Mean:", np.mean(self.arr))
        print("Median:", np.median(self.arr))
        print("Min:", np.min(self.arr))
        print("Max:", np.max(self.arr))
        print("Std Dev:", np.std(self.arr))
        print("Variance:", np.var(self.arr))

    # Percentile and Correlation

    def advanced_stats(self):
        if self.arr is None:
            print("Create arrays first.")
            return

        print("\n1. Percentile")
        print("2. Correlation of two arrays")

        choice = int(input("Enter choice: "))

        if choice == 1:
            p = int(input("Enter percentile value: "))
            print("Percentile:", np.percentile(self.arr, p))

        elif choice == 2:
            arr2 = np.array(list(map(int, input("Enter second array: ").split())))
            corr = np.corrcoef(self.arr.flatten(), arr2.flatten())
            print("Correlation coefficient:\n", corr)


# Main Menu

def main_menu():
    obj = DataAnalytics()

    while True:
        print("\n=================================")
        print("   Welcome to the NumPy Analyzer")
        print("=================================")
        print("1. Create a Numpy Array")
        print("2. Indexing and Slicing")
        print("3. Combine or Split Arrays")
        print("4. Perform Mathematical Operations")
        print("5. Search, Sort, or Filter")
        print("6. Compute Aggregates and Statistics")
        print("7. Advanced Statistics")
        print("8. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            obj.create_array()

        elif choice == 2:
            obj.indexing_slicing()

        elif choice == 3:
            obj.combine_split()

        elif choice == 4:
            obj.math_operations()

        elif choice == 5:
            obj.search_sort_filter()

        elif choice == 6:
            obj.aggregates_statistics()

        elif choice == 7:
            obj.advanced_stats()

        elif choice == 8:
            print("Thank you for using NumPy Analyzer!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()