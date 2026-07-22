try:
    with open("output.txt",'w') as file_obj:
        n = int(input())
        lst = [str(i) + '\n' for i in range(1,n + 1)]
        file_obj.writelines(lst)
except Exception as e:
    print(f"Something wrong : {e}")