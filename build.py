# making an alternative to the makefile.
# This is a simple script that will build the project using the command line.
# it will look for a file called builfile in the directory given in sys.argv[1] and execute the commands in that file.

import os

"""
a typical buildfile would look like this:
nasm boot.asm -o boot.bin
nasm boot2.asm -o boot2.bin
bootloader = append(boot.bin, boot2.bin) ; this is a custom command that will append the contents of boot2.bin to boot.bin
file bootloader, bootloader.bin ; this is a custom command that will write the contents of bootloader to a file called bootloader.bin
""" 
# this file will be run with a bat file so that it can be run like "build" and not build.py

import sys

def main():
    # get the buildfile
    os.chdir(sys.argv[1])
    buildfile = os.path.join(os.getcwd(), "buildfile")
    if not os.path.exists(buildfile):
        print("buildfile not found")
        return
    
    # read the buildfile
    with open(buildfile, "r") as f:
        lines = f.readlines()
    
    # execute the commands in the buildfile
    for line in lines:
        line = line.strip()
        if line.startswith(";") or line == "":
            continue
        elif line.startswith("file"):
            # this is a custom command that will write the contents of a variable to a file
            parts = line.split()
            var_name = parts[1].strip(",")
            file_name = parts[2]
            with open(file_name, "wb") as f:
                f.write(globals()[var_name])
        elif "=" in line:
            # this is a custom command that will assign the result of an expression to a variable
            var_name, expr = line.split("=")
            var_name = var_name.strip()
            expr = expr.strip()

            if expr.startswith("append"):
                inside = expr[len("append("):-1]  # remove append( and )
                file1, file2 = [x.strip() for x in inside.split(",")]

                with open(file1, "rb") as f:
                    data1 = f.read()
                with open(file2, "rb") as f:
                    data2 = f.read()

                globals()[var_name] = data1 + data2
        else:
            # this is a normal command that will be executed using os.system
            os.system(line)
if __name__ == "__main__":
    main()