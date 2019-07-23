import usingnameandmain1

print(usingnameandmain1.nameprinter('shadab', 'ansari'))


#__main__ used to avoid all unnecessary import of imported python file
#when we import oyher file import module also executes all the command of that file.
#to avoid unnecessary executes we use main
#it restricts the program and only the required command execute
#for that we have to put those command under if __name__ == '__main__':