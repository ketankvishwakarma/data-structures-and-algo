
def countdown(num):
    print("current value : {}".format(num))
    if num==0:   
        print("All Done")
        return
    countdown(num-1)


if __name__ == "__main__":
    countdown(10)