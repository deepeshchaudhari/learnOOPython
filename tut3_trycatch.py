try:
    file = open("textfile.txt",'r')
    print('I will try this code and throw exception if error occurs')
    file.close()
except Exception as e:
    print('It will run when try block fail')
else:
    print('It will run when try block fail')
finally:
    print("This will be printed irrespective of exception occuranne")

print("program chal raha hai")