import os, time, signal

def createChild():
		print("New child process is being created...")
		print("Child pid: ", os.getpid(), "\n")
   	
def killChild():
		os.kill(os.getpid(), signal.SIGKILL)

while "true":
	cpid = os.fork()
	if cpid != 0:
		print("Parent pid: ", os.getpid())
		time.sleep(5)
	else:
		createChild() 
		killChild() # Kills the current process which is the child.
		print("I'm dead inside!!!") # It will not be printed because child process has been killed.
