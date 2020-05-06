# Redirections
#
# There is hardly a user of a Linux or a Unix Shell, e.g.
# the Bourne or the Bash Shell, who hasn't used input or output redirections.
# It's not exaggerated to say that a useful work is not possible without
# redirections.

#
#
# The standard output (stdout) can be redirected e.g. into a file,
#  so that we can process this file later with another program.
#  The same is possible with the standard error stream,
#  we can redirect it into a file as well.
#  We can redirect both stderr and stdout into the same file or into
# separate files
# .
#
# The following script should be self-explanatory.
# But nevertheless here are some explanations:
# The first statement uses the regular standard output (stdout),
# i.e. the text "Coming through stdout"
# will be printed into the terminal from which the script has been called.
# In the next line we are storing the standard output channel
# in the variable save_stdout, so that we will be capable of restoring
# the original state at a later point in the script. After this we open
# a file "test.txt" for writing. After the statement sys.stdout
# = fh all print statements will directly print into this file.
# The original condition is restored with sys.stdout = save_stdout.

import sys

print("Coming through stdout")

# stdout is saved
save_stdout = sys.stdout

fh = open("test.txt","w")

sys.stdout = fh
print("This line goes to test.txt")

# return to normal:
sys.stdout = save_stdout

fh.close()


###

# The following example shows how to redirect the standard error stream into a file:

import sys

save_stderr = sys.stderr
fh = open("errors.txt","w")
sys.stderr = fh

x = 10 / 0

# return to normal:
sys.stderr = save_stderr

fh.close()

#
# It's possible to write into the error stream directly, i.e. without changing the general output behaviour. This can be achieved by appending >> sys.stderr to a print statement.

import sys

save_stderr = sys.stderr
fh = open("errors2.txt","w")
sys.stderr = fh

print >> sys.stderr, "printing to error2.txt"

# return to normal:
sys.stderr = save_stderr

fh.close()