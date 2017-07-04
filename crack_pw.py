import sys
import zipfile
import itertools
import string

filename = ""
try:
  filename = sys.argv[1];
except:
  print("The filename is not a valid string!")
  sys.exit(1)
  
#characters = string.ascii_letters 
characters = string.ascii_lowercase
try:
  zipFile = zipfile.ZipFile(filename, "r")
except IOError:
  # rather than raise() we'll simple print it to screen because we dont't want to scare the user
  print("IOError: \nFile you entered was not found!\nTry again!")     
  sys.exit(1)

found = False
#iterate all possible lengths of the password
for leng in range(1, len(characters)+1):
  print("Length of password: ", leng)

  #create an iterator over the cartesian product of all possible permuations
  opts = itertools.product(characters, repeat=leng)

  #iterate all created permutations
  for passw in opts:
    if found:
      sys.exit(0)
    else:
      tmp = ''.join(passw)
      print("Trying with password {} :".format(tmp))
      try:
        #join the tuple to a string and set the password
        passwd = ''.join(passw)
        zipFile.setpassword(passwd)

        """ 
          try to extract the files from the file
          if the password is wrong, an exception is thrown,
            (RuntimeError), which is caught in the except part
        """
        zipFile.extractall()

        print("Password Found\n  Password is ->" + str(passwd))
        found = True
      except RuntimeError:
        print("Failed for test {}\n".format(tmp))
      except Exception as e:
        print("Error opening/operating zipfile\n")

print("No passwords were found...\n")
