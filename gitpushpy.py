import os
os.system("git add .")
commitPurpose = input("Input Commit Purpose : ")
os.system('git commit -m " '+ commitPurpose +' '"')
os.system("git push")
