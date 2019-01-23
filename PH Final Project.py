from visual import* #motion of an electron in a magnetic and electric field 
      
universe = display(title = "Electron motion in a Magnetic field and user defined Electric field",
                   center = vector(0,0,0.6), range = vector(0.5,0.5,0.5), x = 0, y = 0, width = 1000, height = 1000)   
         
#** VARIBLES *****************************************************************************************************************
xcoor = input('Enter the x-coor for the E-field: ')
ycoor = input('Enter the y-coor for the E-field: ')
zcoor = input('Enter the z-coor for the E-field: ')
  
E = vector(xcoor,ycoor,zcoor)               # initial strength of the "E-field"
B = vector(0.2*10**-1,0.4*10**-2,1*10**-3)  # meters/sec "strength of the B field"
Ve = vector(5*10**7,0,1*10**7)              # meters/sec "initial" velocity of the electron
q = -1.602*10**-19                          # charge of an electron in Coulombs
  
Me = 9.109*10**-31                          # kg mass of an electron
Se = vector(0,-0.2,0)                       # intial position of the electron 
Ae = vector(0,0,0)                          # gravity acting upon the electron
     
t = 0                                       # sec
dt = 10**-11                                # sec
        
#** OBJECTS ******************************************************************************************************************                    
electron = sphere(pos = Se, radius = 0.01, color = color.red, make_trail= True)                        
   
for x in arange(-0.5,0.5,0.1):           
    for y in arange(-0.5,0.5,0.15):      
        Bvector = arrow(pos = vector(x,y,0), axis = B, color = color.green)             
                                                               
for x in arange(-0.4,0.4,0.1):           
    for y in arange(-0.5,0.5,0.15):     
        Evector = arrow(pos=vector(x,y,0), axis = E, color = color.yellow)
         
#** EQUATIONS ***************************************************************************************************************** 
while True:                    
       
    rate(100)                               # meters/sec
    Fb = (q*cross(Ve,B))                    # Force equation for the B-field
    Fe = (q*cross(Ve,E))                    # Force equation for the E-field
    F = Fb + Fe                             # Combined Forces of B and E feild to be applied on the electron
 
    Ae = F / Me                             # Acceleration of the electron
    Ve = Ve + Ae * dt                       # Velocity of the electron
    Se = Se + Ve * dt                       # Position of the electron
  
    electron.pos = Se                       # position change of the object
    t = t + dt                              # sec
    
