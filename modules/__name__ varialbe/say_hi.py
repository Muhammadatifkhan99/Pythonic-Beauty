from say_sup import say_sup

def say_hi():
    print(f"Hi! My __name__ is {__name__}")
##the name variable is set to main in the main file

#so name is a variable that refers to the name of module unless you are running the file itself so the
#name variable is set to main if that file is actually runned
say_hi()
say_sup()


#                       __name__
#when run, every python file has a __name__variable.
#if the is the main file being run, its value is "__main__".
#otherwise, its value is the file name.



