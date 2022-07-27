
import csv
from email import header

# doing with open as csv... automatically closes the file for you without you manually closes it
def read_csv():
    with open('SampleSalesData.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                line_count += 1
        print(f'Processed {line_count} lines.')
# read_csv()

# Writing to csv files


def write_csv():
    with open('writeto.csv', mode='w+') as employee_file:
        #  need to specifcy so it doesn't auto skip rows
        employee_writer = csv.writer(employee_file, delimiter=',',lineterminator='\n')
        headers = ['Name', 'Dept', 'Month']
        employee_writer.writerow(headers)
        employee_writer.writerow(['John Smith', 'Accounting', 'November'])
        employee_writer.writerow(['Erica Meyers', 'ITtt', 'March'])

# write_csv()

# add read and add additionally to csv


def read_factbook_csv():
    with open('factbook.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                line_count += 1
        print(f'Processed {line_count} lines.')

# read from file and write to separate file:
# def read_csv_write_csv():
#     with open('film.csv') as input_file:
#         csv_reader = csv.reader(input_file, delimiter=';')
#         with open('film_output.csv', 'w+') as output_file:
#             # rows = []
#             for line in input_file:
#                 output_file.write(line)
     

# read from file , transform, and write to separate file:
# attempt #1: found out what kind of data we have 
# def read_csv_write_csv():
#     with open('film.csv') as input_file:
#         csv_reader = csv.reader(input_file, delimiter=';')
#         with open('film_output.csv', 'w+') as output_file:
#             rows = []
#             for row in csv_reader:
#                 print(row)
  

# attempt #2: found 2nd row is not where data starts
# def read_csv_write_csv():
#     with open('film.csv') as input_file:
#         csv_reader = csv.reader(input_file, delimiter=';')
#         with open('film_output.csv', 'w+') as output_file:
#             rows = []
#             headers = next(csv_reader)
#             second = next(csv_reader)
#             print('headers', headers)
#             for row in csv_reader:
#                 print(row)
#                 break
     

# attempt #3: found 3rd row is where data starts
# def read_csv_write_csv():
    # with open('film.csv') as input_file:
    #     csv_reader = csv.reader(input_file, delimiter=';')
    #     with open('film_output.csv', 'w+') as output_file:
    #         rows = []
    #         headers = next(csv_reader)
    #         second = next(csv_reader)
    #         for row in csv_reader:
    #             print(row)
                
# now we can write to csv
def read_csv_write_csv():
    with open('film.csv') as input_file:
        csv_reader = csv.reader(input_file, delimiter=';')
        file_output_name = 'film_output'
        with open('{}.csv'.format(file_output_name), 'w+') as output_file:
            writer = csv.writer(output_file, delimiter=',',lineterminator='\n')

            row_count = 0
            headers = next(csv_reader)
            second = next(csv_reader)
            writer.writerow(headers)
            for row in csv_reader:
                row_count += 1
                writer.writerow(row)
            print('{} rows written to {}'.format(row_count, file_output_name))

# read_csv_write_csv()

# alternatives to read and write a file:
# def alt_read_and_write():
#     file1=open("inventory.txt","r")
#     file2=open("purchasing.txt","w")

#     # Iterate over each line in the file
#     for line in file1.readlines():

#         # Separate each item in the line
#         items=line.split()

#         # Retrieve important bits
#         qty=int(items[3])
#         reorder=int(items[4])

#         # Write to the file if conditions are met
#         if qty<=reorder:
#             file2.write(items[0]+"\t"+items[1]+"\n")

#     # Release used resources
#     file1.close()
#     file2.close()


# add to txt
# beginner - manipulate data
def read_csv_sum():
    with open('SampleSalesData.csv') as input_file:
        csv_reader = csv.reader(input_file, delimiter=',')
        file_output_name = 'sales_ouput'
        with open('{}.csv'.format(file_output_name), 'w+') as output_file:
            writer = csv.writer(output_file, delimiter=',',lineterminator='\n')

            row_count = 0
            headers = next(csv_reader)
            # search for column index
            column_index = 0
            sum = 0
            print(type(headers))
            for index, column_name in enumerate(headers):
                print(column_name, index)
                if 'Sales' in column_name:
                    column_index = index
                    print('index: {}'.format(index))
                    break
            
            for row in csv_reader:
                sales_data = row[column_index]
                print(sales_data)
                sum += float(sales_data)
                # writer.writerow(row)
            print('{} total sales'.format(round(sum, 2)))
read_csv_sum()

# filter data

#  

# intermediate


# advance