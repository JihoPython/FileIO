import pandas as pd

def main():
    row_data = {
        'col1': [1, 2, 3, 4],
        'col2': [10, 20, 30, 40],
        'col3': [100, 200, 300, 400]
    }
    row_data = pd.DataFrame(row_data)
    row_data.to_excel(excel_writer='sample.xlsx')

if __name__ == '__main__':
    main()