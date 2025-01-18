with open("file.txt","w")as f:
    f.write("hello my name is yogendra mishra\n i am from balrampur \n i am a student of M.C.A")
    f = open("file.txt","r")    
    data = f.read()
    print(data)
    word = "mishra"
    
    if word in f:
        print("found")
    else:
        print("not found")