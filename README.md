Variable Declaration:

1. Variables starts with the symbol '$', and you can use variables in the expression of other variables.
2. Expressions can use previously assigned variables, allowing for recursive operations.
3. Variables can be declared with values of any type, including objects and lists. To include expression values within an object, the '@"{expression}"' function should be used. For example: `$list = [@"(1+2)",'1+2']`. result = `$list = [3 , '1+2']`
4. Previously assigned variables can be used within lists or objects.
5. Table data can be inserted into a variable using JSON format.
6. Table data can be used to create ne table with this syntax .
``` 
$table= [{"radius" : 10},{"radius" : 100}];
$table2 = $<table>(x)=>(x.radius>10){ {'area' : x.radius*x.radius*3.1416 , 'radius' : x.radius , 'increasing_number' : x.radius+$<table2><[$index-1].radius|0> } };```
here $<table> is the representation of $table '(x)' is each element of $table  (x.radius>10) is an optional condition {...} this is the funciton that returns the value of $table2 array

10. Comments can be added using '#' for single-line comments and '/* ... */' for multiple lines.

Report Engine:

1. Use '{{$variable}}' to print the value of an integer or float variable.
2. Use '{{$variable : format_rule }}' to print a formatted value of a variable. format_rule should be in python syntax
3. use '{{$variable ::{...}}}' you can pass a json object of format rule 
example :
'{{$variable ::{"align" : 'center', 'fill' : '#' , "width" : 30}}}'
4. use '{{$variable:c1,c2,c3}}' there 'c1', c2, c3 are classes that are declared in the template with <format>c1 = {'align': 'center'}\nc2={'fill' : '#'} </format>
5. you can use condition in class and or class to format if the condition is false
example :
 '{{$variable:((x)=>x>1),c1,c2,c3|c4,c5}}'

5. Use '{{$variable.value()}}' to print the value of an object or string variable.
7. Use '<> ... </>' to include Python code. Declare variables within the code using '{{$variable}}'.
8. Operations such as 'avg()', 'min()', 'max()', 'sum()', 'count()' ,'len()', 'reverse()' ,'index()', 'map()', 'set()', 'distinct()' can be performed. Filter operations can be done using arrow functions. For example: 'sum((x)=>x>1)'.

Report Engine Examples:

