import machine,time
class ledrgb():

    def __init__(self,rouge,vert,bleu):

        pin_rouge = machine.Pin(rouge, machine.Pin.OUT)
        pin_vert = machine.Pin(vert, machine.Pin.OUT)
        pin_bleu = machine.Pin(bleu, machine.Pin.OUT)

        self.led_rouge = machine.PWM(pin_rouge, freq=1000)
        self.led_vert = machine.PWM(pin_vert, freq=1000)
        self.led_bleu = machine.PWM(pin_bleu, freq=1000)

        self.led_rouge.duty(0)
        self.led_bleu.duty(0)
        self.led_vert.duty(0)

    def off(self):
        self.led_rouge.duty(0)
        self.led_bleu.duty(0)
        self.led_vert.duty(0)

    def rouge(self,value=None):

        if value is None:
            self.led_rouge.duty(1023)
            self.led_vert.duty(0)                    
            self.led_bleu.duty(0)
        else:
            self.led_rouge.duty(int(value))
            self.led_vert.duty(0)                    
            self.led_bleu.duty(0)

    def vert(self,value=None):

        if value is None:        
            self.led_vert.duty(1023)
            self.led_rouge.duty(0)
            self.led_bleu.duty(0)
        else:
            self.led_vert.duty(value)
            self.led_rouge.duty(0)
            self.led_bleu.duty(0)

    def bleu(self,value=None):

        if value is None:        
            self.led_bleu.duty(1023)
            self.led_rouge.duty(0)
            self.led_vert.duty(0) 
        else:
            self.led_bleu.duty(value)
            self.led_rouge.duty(0)
            self.led_vert.duty(0)   

    def orange(self,value=None):

        if value is None:
            self.led_rouge.duty(1023)
            self.led_vert.duty(512)                    
            self.led_bleu.duty(0)
        else:
            self.led_bleu.duty(value) 

    def blink_rouge(self,nbr):
        self.off()
        cpt = 0
        start = time.ticks_us()
        while cpt<nbr:
            if time.ticks_diff(time.ticks_us(), start) >500:
                self.led_rouge.duty(1023)
                cpt+=1
            else:
                self.led_rouge.duty(0)            

