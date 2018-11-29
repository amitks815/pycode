str2 = "Line1-abcdef \nLine2-abc \nLine4-abcd";
print (str2.split( ))
print( str2.split(' @', 1 ))  # num is number of line minus 1

'splitlines'
str = "Line1-a b c d e f\nLine2- a b c\n\nLine4- a b c d";
print (str.splitlines( ))
print (str.splitlines(0 ))
print (str.splitlines( 3 ))
print (str.splitlines( 4 ))
print (str.splitlines( 5 ))