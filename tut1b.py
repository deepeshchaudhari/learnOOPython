import tut1a

def function(*args):
    if len(args)==3:
        print("The name of the student is",
        args[0],"and age is ",args[1],
        "and rool no is",args[2],".")
    else:
        print("The name of the student is",
              args[0], "and age is ", args[1])

def master(**kwargs):
    for key,value in kwargs.items():
        print(key,value)

def hybrid_args(str,*args,**kwargs):
    print("This function is made by ", str)
    print("The name of the student is",
          args[0], "and age is ", args[1],
          "and roll no is", args[2], ".")
    for key,value in kwargs.items():
        print(key,value)

function("Deepesh","22","19111028")
function("manoj","55")

list =["Ratan",90,1212121]
function(*list)
dict = {"Anil":89,"Mukesh":95,"Ratan":100,"Bill":88,"jack":92}
master(**dict)
hybrid_args("Deepesh",*list,**dict)