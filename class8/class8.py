# tup: tuple[int,int,int,int,int,int,int] = (1,2,4,5,6,7,8)
# for i in tup:
    # print(i)
# 

# name:str = input("Whats your name ? : \t")
# print(name)
# print(type(name))

# import sys
# print("line1")
# print("line2")
# print(sys.argv)
# print(type(sys.argv))

# import sys
# print("line1")
# print("line2")
# print(type(sys.argv))

# if sys.argv[1] == "-g":
#     print("Package will be installed globally on the system")
# print(sys.argv)

# / back slash is used everywhere for line continuation
prompt: str = """if you share your name, we can personalize the message you see.\
What is your name ? """

name:str = input(prompt)
print(f"Hello {name}")

prompt1: str = """if you share your name, we can personalize the message you see.
What is your name ? """

name1:str = input(prompt1)
print(f"Hello {name1}")

prompt2: str = """if you share your name, we can personalize the message you see.\n
What is your name ? """

name2:str = input(prompt2)
print(f"Hello {name2}")

print(1 +\
      2 +\
        3+\
            4+\
                5)