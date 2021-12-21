from vpython import *
var_dy = y

function_graph = gcurve( color=color.black, label="y vs. x" )

x = 0
y = 1
delta_x = 0.01 

while ( x<4 ): 
    rate(200) 
    y = y + var_dy*delta_x 
    x = x + delta_x
    function_graph.plot( pos=(x,y) )
    
print( "Done." )