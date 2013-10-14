CleanHTML
=========

Quick Script to pretty print HTML from command line that uses BeautifulSoup to 
create a new cleanly formatted file.  Nothing fancy here, just something for 
shell noobs to work with... exactly the sort that might need this script 
written out for them.

Requirements
------------

* A compupter
* Python 

Examples
-------
    
    python /path/to/CleanHTML/cleanit.py -i /path/to/your/ugly.html

This will create a new file:
    
    /path/to/your/ugly.html.clean

which you can edit, diff, or use to overwrite the existing file.

You might also:

    python /path/to/CleanHTML/cleanit.py -i /path/to/your/old/ugly.html -o /path/to/your/new/pretty.html
