# Affichage OLED SSD1306 en MicroPython | MicroPython SSD1306  OLED display
# affiche les mesures d'un capteur BME280 i2c sur un écran OLED
# Display values from an i2c BME280 sensor on OLED screen
# https://projetsdiy.fr - https://diyprojects.io (dec. 2017)

import machine, time, ssd1306, bme280
import CCS811
import ledrgb
import framebuf
from writer import Writer
import icones
import ntptime
import network
import ubinascii

# Font
import FreeSans20
import font10
import font6

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
wlan_mac = sta_if.config('mac')
print("Mac adress "+ubinascii.hexlify(wlan_mac).decode())
sta_if.connect('phoebus_gaston','phoebus09')
#sta_if.connect("Borde Basse Personels",'')
print("connection au wifi")
time.sleep(2)

while sta_if.active() == False:
      print('.', end = " ")
      time.sleep_ms(50)

time.sleep(2)
start = time.ticks_us()
page = 0

eco2 = 0
tvoc= 0
temp=0.0
pa=0.0
hum=0.0
print (sta_if.ifconfig())
print("Local time before synchronization：%s" %str(time.localtime()))
ntptime.settime()
print("Local time after synchronization：%s" %str(time.localtime()))
ladate = list(time.localtime())
print (ladate[2],ladate[1],ladate[0])


led = ledrgb.ledrgb(12,13,14)

pinScl      = 22  #ESP8266 GPIO5 (D1)
pinSda      = 21  #ESP8266 GPIO4 (D2)
addrOled    = 60  #0x3c
addrBME280  = 118 #0x76
hSize       = 64  # Hauteur ecran en pixels | display heigh in pixels
wSize       = 128 # Largeur ecran en pixels | display width in pixels

oledIsConnected = False
bmeIsConnected  = False
temp = 0
pa = 0
hum = 0

# init ic2 object
i2c = machine.SoftI2C(scl=machine.Pin(22), sda=machine.Pin(21)) #ESP8266 5/4


s = CCS811.ccs811(i2c=i2c, addr=90)
time.sleep(1)
"""
for i in range(0,1024,10):
      print(i)
      led.rouge(i)
      time.sleep_ms(20)
"""
led.off()


# Scan le bus i2c et verifie si le BME280 et l'ecran OLED sont connectes
# Scan i2c bus and check if BME2 and OLDE display are connected
print('Scan i2c bus...')
devices = i2c.scan()
if len(devices) == 0:
  print("No i2c device !")
else:
  print('i2c devices found:',len(devices))
  for device in devices:
    if device == addrOled:
      print("connected oled")
      oledIsConnected = True
    if device == addrBME280:
      bmeIsConnected = True  
    print(device)
if oledIsConnected:
  oled = ssd1306.SSD1306_I2C(wSize, hSize, i2c, addrOled)

with open('icone_co2_36x36.pbm', 'rb') as f:
    f.readline() # Magic number
    #f.readline() # Creator comment
    f.readline() # Dimensions
    data = bytearray(f.read())
#fb = framebuf.FrameBuffer(data, 128, 64, framebuf.MONO_HLSB)
fb = framebuf.FrameBuffer(data, 36, 25,framebuf.MONO_HLSB)

with open('icone_temperature_36x79.pbm', 'rb') as f:
    f.readline() # Magic number
    #f.readline() # Creator comment
    f.readline() # Dimensions
    data = bytearray(f.read())
fb2 = framebuf.FrameBuffer(data, 16, 36,framebuf.MONO_HLSB)

with open('logo_humidite_36x36.pbm', 'rb') as f:
    f.readline() # Magic number
    #f.readline() # Creator comment
    f.readline() # Dimensions
    data = bytearray(f.read())
fb3 = framebuf.FrameBuffer(data, 36, 37,framebuf.MONO_HLSB)

led.off()

def affiche_heure():
  #ntptime.update()
  ladate = list(time.localtime())
  print (ladate[2],ladate[1],ladate[0])
  affdate = str(ladate[2])+"/"+str(ladate[1])+"/"+str(ladate[0])
  affheure = str(ladate[3])+":"+str(ladate[4])+":"+str(ladate[5])
  #oled.text(affdate, 10, 10)
  wri = Writer(oled, FreeSans20,False)
  Writer.set_textpos(oled, 10, 30)  # verbose = False to suppress console output
  wri.printstring(affheure)
  wri2 = Writer(oled, font6,False)
  Writer.set_textpos(oled, 40, 40)  # verbose = False to suppress console output
  wri2.printstring(affdate)
  oled.show()   

def affiche_co2():
    oled.blit(fb, 10, 10)
    #oled.text(str(eco2), 40, 40)
    wri = Writer(oled, FreeSans20,False)
    Writer.set_textpos(oled, 30, 50)  # verbose = False to suppress console output
    wri.printstring(str(eco2))
    oled.text("ppm", 95, 40)
    oled.show()  

def affiche_temp():
    oled.blit(fb2, 10, 10)
    #oled.text(str(eco2), 40, 40)
    wri = Writer(oled, FreeSans20,False)
    Writer.set_textpos(oled, 30, 50)  # verbose = False to suppress console output
    wri.printstring(str(round(temp,1))+" C")
    oled.show()

def affiche_hum():
    oled.blit(fb3, 10, 10)
    #oled.text(str(eco2), 40, 40)
    wri = Writer(oled, FreeSans20,False)
    Writer.set_textpos(oled, 30, 50)  # verbose = False to suppress console output
    wri.printstring(str(int(hum))+" %")
    oled.show()          

while True:
      
 if bmeIsConnected:
  bme = bme280.BME280(i2c=i2c,address=addrBME280)
  print("BME280 values:")
  print(bme.raw_values)
  temp,pa,hum = bme.raw_values 
  print(temp," C")
  print(pa," hpa") 
  print(hum," %")
  
  if oledIsConnected:
    oled = ssd1306.SSD1306_I2C(wSize, hSize, i2c, addrOled)
    oled.fill(0)
        
    if time.ticks_diff(time.ticks_us(), start) > 2000:
      #raise TimeoutError
      if page == 0:
        affiche_heure()
      elif page==1:
        if s.data_ready():
          eco2 = s.eCO2
          tvoc= s.tVOC
        affiche_co2()
      elif page==2:
        affiche_temp()
      elif page==3:
        affiche_hum()    
      """
      page +=1
      if page==4:
        page =0
      """
      page =(page+1)%4
      print ("Page",page)
      

  if eco2 <1000:
      led.vert()
  elif 1000<= eco2 and eco2<1500:
    led.orange()
  else:
    led.rouge()      
  print('eCO2: %d ppm, TVOC: %d ppb' % (eco2, tvoc))
  time.sleep(5)
