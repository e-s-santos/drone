from mpu6050 import mpu6050
import time
#mpu = mpu6050(0x68)


def getGiroACelTemp():
    return_data = "{"
    mpu = mpu6050(0x68)
    try:
        print("Temp : "+str(round(mpu.get_temp(),3)))		
		return_data += "\"temperatura: \" " + str(round(mpu.get_temp(),3))
    except:
        print ("Não foi possível pegar os detalhes")
    
    accel_data = mpu.get_accel_data()
    try:
        print(" Acc X: "+str(round(accel_data['x'],2)) + " \t Y: "+str(round(accel_data['y'],2))+ " \t Z: "+str(round(accel_data['z'],2)) )
    except OSError:
        print ("Não foi possivel pegar os detalhes")
    except:
        print ('geral')
    print()

    gyro_data = mpu.get_gyro_data()
    try:
        print(" Gyro X: "+str(round(gyro_data['x'],2)) + " \t Y: "+str(round(gyro_data['y'],2))+ " \t Z: "+str(round(gyro_data['z'],2)) )
    except OSError:
        print ("Não foi possível pegar os detalhes")
    except:
        print ("verifique os circuitos")
    print("------------------------------\n\n\n\n")
    