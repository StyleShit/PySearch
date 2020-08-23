# PySearch

A small Python class for basic Google Search automation.

## Usage:
```python
ps = PySearch()
links = ps.get( "Hello World", 22 )
```

The first parameter is the search term, and the second one represents the amount of the results that you want to return.

This code will return a list of links that can be used later, i.e. like this:

```python
for i, l in enumerate( links ):
	print "[" + str( i + 1 ) + "] " + l

```

An example of a working code can be found in the `main.py` file.
	
## Requirements:
	- Urllib
	- Requests
	- Re
