You can choose script without any options, Defaults are 100km from given base location (53.3381985, -6.2592576) with file name with customers data 'customers.txt'

Optionally:
 '-l', 'Current location like (53.3381985, -6.2592576)'
 '-p', 'Current place like Dublin'
 '-d', 'Needed distance'
 '-f', 'Input file with customers list'
 '-t', 'Type of calc: vincenty(1) or great_circle(2)'
 Note: do not use -l and -p at te same time; if -p provided it will override -l option
 
 E.g. 
 python gbd.py -p "Moscow, Center" -d 50 -t 2
 will result the list of customers in circle of 50 km from center of Moscow using great_circle calc approach.
 
 See output in json format in res.json
 
 
 
