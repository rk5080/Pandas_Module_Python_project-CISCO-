import csv

class Series:
    def __init__(self, data, col_name):
        self.data = data
        self.col_name = col_name

    def sum(self):
        try:
            return sum(float(x) for x in self.data if str(x).replace('.', '', 1).isdigit())
        except Exception as e:
            print(f"Error in sum(): {e}")
            return None

    def max(self):
        try:
            numeric_data = [float(x) for x in self.data if str(x).replace('.', '', 1).isdigit()]
            return max(numeric_data)
        except Exception as e:
            print(f"Error in max(): {e}")
            return None

    def min(self):
        try:
            numeric_data = [float(x) for x in self.data if str(x).replace('.', '', 1).isdigit()]
            return min(numeric_data)
        except Exception as e:
            print(f"Error in min(): {e}")
            return None

    def __repr__(self):
        return f"Series({self.col_name}: {self.data})"


class DataFrame:
    def __init__(self, data, columns):
        self.data = data  # list of dicts (row-wise)
        self.columns = columns

    def __getitem__(self, key):
        try:
            # Column access
            if key in self.columns:
                return Series([row[key] for row in self.data], key)
            # Row access
            elif isinstance(key, int) and 0 <= key < len(self.data):
                return self.data[key]
            else:
                raise KeyError(f"Invalid key: {key}")
        except Exception as e:
            print(f"Error in __getitem__: {e}")

    def __setitem__(self, key, value):
        try:
            # Modify or add column
            if isinstance(value, list) and len(value) == len(self.data):
                for i, row in enumerate(self.data):
                    row[key] = value[i]
                if key not in self.columns:
                    self.columns.append(key)
            else:
                raise ValueError("Value must be a list of same length as rows")
        except Exception as e:
            print(f"Error in __setitem__: {e}")

    def save_to_file(self, filename):
        try:
            with open(filename, "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=self.columns)
                writer.writeheader()
                writer.writerows(self.data)
            print(f"Data saved to {filename}")
        except Exception as e:
            print(f"Error in save_to_file: {e}")

    def show(self, n=5):
        try:
            for i, row in enumerate(self.data[:n]):
                print(row)
        except Exception as e:
            print(f"Error in show: {e}")


def readfile(filename):
    try:
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            data = [row for row in reader]
            return DataFrame(data, reader.fieldnames)
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except Exception as e:
        print(f"Error in readfile: {e}")
