import os

# command = os.popen('ls -al')
# print(command.read())
# command.close()

command = os.popen('npm -v')
print("npm version: " + command.read())
command.close()

command = os.popen('node -v')
print("node version: " + command.read())
command.close()
