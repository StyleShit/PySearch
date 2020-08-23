# -*- coding: utf-8 -*-

from PySearch import PySearch

# main code
def main():
    ps = PySearch()
    links = ps.get( "Hello World", 22 )

    for i, l in enumerate( links ):
        print "[" + str( i + 1 ) + "] " + l

    print "---------------\n"


# main code execution
if __name__ == "__main__":
    main()

