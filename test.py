import easygopigo3 as easy
import time
sensor_readings = None
gpg = easy.EasyGoPiGo3()
DistancePort = gpg.init_distance_sensor('RPI_1')
LoudnessSensor = gpg.init_loudness_sensor('AD2')
 

def eyecolor(Value):
    gpg.set_eye_color(Value)
    gpg.open_eyes()
def wait(value):
    time.sleep(value)


loudnesslimit = 65
def Distance():
    loudness = LoudnessSensor.percent_read()
    while True:
       
       
        wait(0.5)
        if (DistancePort.read_inches()<maxdistance):
            gpg.stop()
            eyecolor(closecolor)
            gpg.turn_degrees(90)
            
           
           
            
        elif (DistancePort.read_inches()>maxdistance):
            gpg.forward()
            eyecolor(farcolor)
            
            
            
        
            
                
                
            
    



Distance()
