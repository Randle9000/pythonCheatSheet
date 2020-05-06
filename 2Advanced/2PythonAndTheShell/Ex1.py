# Shell is a term, which is often used and often misunderstood. Like the shell of an egg, either hen or Python snake, or a mussel, the shell in computer science is generally seen as a piece of software that provides an interface for a user to some other software or the operating system. So the shell can be an interface between the operating system and the services of the kernel of this operating system. But a web browser or a program functioning as an email client can be seen as shell as well.
#
# Understanding this, it's obvious that a shell can be either
#
#     a command-line interface (CLI)
#     or
#     a graphical user interface (GUI)
#
# But in most cases the term shell is used as a synonym for a command line interface (CLI). The best known and most often used shells under Linux and Unix are the Bourne-Shell, C-Shell or Bash shell. The Bourne shell (sh) was modelled after the Multics shell, and is the first Unix shell.
# Most operating system shells can be used in both interactive and batch mode.

# System programming
# System programming (also known as systems programming) stands for the activity of programming system components or system software. System programming provides software or services to the computer hardware, while application programming produces software which provides tools or services for the user.
#
# "System focused programming" as it is made possible with the aid of the sys and the os module, serves as an abstraction layer between the application, i.e. the Python script or program, and the operating system, e.g. Linux or Microsoft Windows. By means of the abstraction layer it is possible to implement platform independent applications in Python, even if they access operating specific functionalities.
#
# Therefore Python is well suited for system programming, or even platform independent system programming. The general advantages of Python are valid in system focused programming as well:
#
#     simple and clear
#     Well structured
#     highly flexible
#
# The os Module
# The os module is the most important module for interacting with the operating system. The os module allows platform independent programming by providing abstract methods. Nevertheless it is also possible by using the system() and the exec*() function families to include system independent program parts. (Remark: The exec*()-Functions are introduced in detail in our chapter "Forks and Forking in Python")
# The os module provides various methods, e.g. the access to the file system.

