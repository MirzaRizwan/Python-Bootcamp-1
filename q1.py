name = input("\nName is : ")
space = ""
name = name[::-1]
def main(name,space):
    print("\n Reverse diagonal is :")
    for ch in name :
        space +="  "
        print(space,ch) 
    return name,space
main(name,space)
    
