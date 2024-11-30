class employee:
    #initialize
    def __init__(self):
        print("employee created")
    def __del__(self):
        print("employee deleted")

e=employee()
del e
        