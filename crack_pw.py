import sys
import zipfile
import itertools
import string

filename = ""
try:
  filename = sys.argv[1];
except:
  print("The filename was not a valid string")
  exit(1)
  
#characters = string.ascii_letters
characters = string.ascii_lowercase
zipFile = zipfile.ZipFile(filename, "r")

#iterate all possible lengths of the password
for leng in range(1, len(characters)+1):
  print("Length of password: ", leng)

  #create an iterator over the cartesian product of all possible permuations
  opts = itertools.product(characters, repeat=leng)

  #iterate all created permutations
  for passw in opts:
      print("Trying with password {} ...".format(passw))
      try:
        #join the tupel to a string and set the password
        passwd = ''.join(passw)
        zipFile.setpassword(passwd)

        """ 
        try to extract the files from the file
        if the password is wrong, an exception is thrown,
        (RuntimeError), which is caught in the except part
        """
        zipFile.extractall()

        #if there was no error the password will be shown and the programm exits
        print("The password for file is: " + str(passwd))
        exit()
      except RuntimeError:
        print("Failed For {}\n".format(passw))
      except zipfile.BadZipfile:
        print("Error opening/operating zipfile\n")
      except:
        pass

print("No passwords were found...\n")
