import csv

# try:
#     with open("users.csv",'w',newline = "") as file:
#         writer = csv.writer(file)
#         writer.writerows([['id','Name','Age'],['1','Ravi',20],['2','Abi',21],['3','Raji',20]])
# except Exception as e:
#     print(f"Something wen wrong : {e}")


## Reading csv file content

try:
    with open("users.csv",'r',newline = "") as file:
        reader = csv.reader(file)
        [print(row) for row in reader]
except Exception as e:
    print(f"Something wen wrong : {e}")

