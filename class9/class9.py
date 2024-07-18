from typing import Tuple,Dict
def my_func(a:int,b:int,*args:int,**kwargs:int) -> None:
    print(a,b,args,kwargs)

my_func(2,5,12,12,13,13,1,4,15,x=1,y=2)