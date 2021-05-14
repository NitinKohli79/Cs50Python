def announce(f):
    def wrapper1():
        print("Check user rigths")
        f()
        print("Executed as per rights")
    return wrapper1

    #def wrapper2():
    #    print("clean up mess")
    #return wrapper2()
	
	#added more comments

@announce
def hello():
    print("hello world")

hello()
