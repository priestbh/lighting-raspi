import tkinter as tk
import tkinter.font as TkFont
import threading
import time
import board
import neopixel

pixel_pin = board.D18
num_pixels = 230
ORDER = neopixel.GRB

liveRed = 128
liveGreen = 128
liveBlue = 128

winHeight = 450
myrepeat = 25

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.9, auto_write=False, pixel_order=ORDER
)

window = tk.Tk()
myFont = TkFont.Font(family = 'Helvetica', size = 28, weight = 'bold')



def ledON():
	global liveRed, liveGreen, liveBlue
	print("LED ON button pressed")
	pixels.fill((liveRed, liveGreen, liveBlue))
	pixels.show()

def ledOFF():
	global liveRed, liveGreen, liveBlue
	print("LED OFF button pressed")
	pixels.fill((0, 0, 0))
	pixels.show()

def ledRedUp():
	global liveRed, liveGreen, liveBlue
	if liveRed < 255 :
		liveRed = liveRed + 1
	print("LED red up button pressed, red:{red} green:{green} blue:{blue}".format(red=liveRed,green=liveGreen,blue=liveBlue))
	ledRedLabelButton["text"] = "Red: {red}".format(red=liveRed)
	pixels.fill((liveRed, liveGreen, liveBlue))
	pixels.show()

def ledRedDown():
	global liveRed, liveGreen, liveBlue
	if liveRed > 0 :
		liveRed = liveRed - 1
	print("LED red down button pressed, red:{red} green:{green} blue:{blue}".format(red=liveRed,green=liveGreen,blue=liveBlue))
	ledRedLabelButton["text"] = "Red: {red}".format(red=liveRed)
	pixels.fill((liveRed, liveGreen, liveBlue))
	pixels.show()

def ledGreenUp():
        global liveRed, liveGreen, liveBlue
        if liveGreen < 255 :
                liveGreen = liveGreen + 1
        print("LED green up button pressed, red:{red} green:{green} blue:{blue}".format(red=liveRed,green=liveGreen,blue=liveBlue))
        ledGreenLabelButton["text"] = "Green: {green}".format(green=liveGreen)
        pixels.fill((liveRed, liveGreen, liveBlue))
        pixels.show()

def ledGreenDown():
        global liveRed, liveGreen, liveBlue
        if liveGreen > 0 :
                liveGreen = liveGreen - 1
        print("LED green down button pressed, red:{red} green:{green} blue:{blue}".format(red=liveRed,green=liveGreen,blue=liveBlue))
        ledGreenLabelButton["text"] = "Green: {green}".format(green=liveGreen)
        pixels.fill((liveRed, liveGreen, liveBlue))
        pixels.show()

def ledBlueUp():
        global liveRed, liveGreen, liveBlue
        if liveBlue < 255 :
                liveBlue = liveBlue + 1
        print("LED Blue up button pressed, red:{red} green:{green} blue:{blue}".format(red=liveRed,green=liveGreen,blue=liveBlue))
        ledBlueLabelButton["text"] = "Blue: {blue}".format(blue=liveBlue)
        pixels.fill((liveRed, liveGreen, liveBlue))
        pixels.show()

def ledBlueDown():
        global liveRed, liveGreen, liveBlue
        if liveBlue > 0 :
                liveBlue = liveBlue - 1
        print("LED Blue down button pressed, red:{red} green:{green} blue:{blue}".format(red=liveRed,green=liveGreen,blue=liveBlue))
        ledBlueLabelButton["text"] = "Blue: {blue}".format(blue=liveBlue)
        pixels.fill((liveRed, liveGreen, liveBlue))
        pixels.show()


def exitProgram():
	print("Exit Button pressed")
	pixels.fill((0, 0, 0))
	pixels.show()    
	window.quit()	

def myPixel(x):
        # first strand starts at top and goes down
        # this allows linear address from end to end
        if x <= 43:
                x = 43 - x
        return x
         

def loadPreset():
        #0-43 top to bottom Right
        #44-185 right to left 
        #186-229 top to bottom Left
        print("preset 1 pressed")
        t1=threading.Thread(target=northernLights)
        t1.start()

        #for x in range(0, 43):
        #        pixels[x] = (0,0,255)
        #for x in range(44, 185):
        #        pixels[x]= (0,255,255)
        #for x in range(186,229):
        #        pixels[x] = (0,0,255)
        #pixels.show()  

def fade(pixel, fadeTime = 0.2,fadeStart = 0,fadeEnd = 255):
        if fadeEnd > fadeStart:
                dist = fadeEnd - fadeStart
        else:
                dist = fadeStart - fadeEnd        
        fadeLength = 1/(dist/fadeTime)
        for x in range(fadeStart, fadeEnd):
                pixels[pixel] = (0,x,255)
                pixels.show()
                print("pixel: {pixel}, time: {fadeLength}".format(pixel=pixel,fadeLength=fadeLength ))
                time.sleep(fadeLength)


def northernLights():
        #0-43 top to bottom Right
        #44-185 right to left 
        #186-229 top to bottom Left
        print("preset 1 pressed")
        for x in range(0, 228):
                pixels[x] = (0,0,255)
        pixels.show()  
        for x in range(0,228):
                print (x)
                fade(myPixel(x)) 
                if x < 43:
                        fade(myPixel(x) + 1, fadeStart = 255, fadeEnd = 0)
                elif x == 44:
                        fade(myPixel(x - 1), fadeStart = 255, fadeEnd = 0)
                else:        
                        fade(myPixel(x) - 1, fadeStart = 255, fadeEnd = 0)


frameONOFF = tk.Frame(master=window, width=200, height=winHeight, bg="gray")

exitButton  = tk.Button(frameONOFF, text = "Exit", font = myFont, command = exitProgram, height =2 , width = 6) 
exitButton.pack(side = tk.BOTTOM)

ledONButton = tk.Button(frameONOFF, text = "LED ON", font = myFont, command = ledON, height = 2, width =8 )
ledONButton.pack(side = tk.TOP)
ledONButton = tk.Button(frameONOFF, text = "LED OFF", font = myFont, command = ledOFF, height = 2, width =8 )
ledONButton.pack(side = tk.TOP)

frameONOFF.pack(fill=tk.Y, side=tk.LEFT)

frameRED = tk.Frame(master=window, width=200, bg="red")
ledRedUpButton = tk.Button(frameRED, text = "Red +", repeatdelay=500, repeatinterval=myrepeat, font = myFont, command = ledRedUp, height = 2, width =8 )
ledRedUpButton.pack(side = tk.TOP)
ledRedLabelButton = tk.Button(frameRED, text = "Red: {red}".format(red=liveRed), font = myFont, height = 2, width =8 )
ledRedLabelButton.pack(side = tk.TOP)
ledRedDownButton = tk.Button(frameRED, text = "Red -", repeatdelay=500, repeatinterval=myrepeat, font = myFont, command = ledRedDown, height = 2, width =8 )
ledRedDownButton.pack(side = tk.TOP)
frameRED.pack(fill=tk.Y, side=tk.LEFT)

frameGREEN = tk.Frame(master=window, width=200, bg="green")
ledGreenUpButton = tk.Button(frameGREEN, text = "Green +", repeatdelay=500, repeatinterval=myrepeat, font = myFont, command = ledGreenUp, height = 2, width =8 )
ledGreenUpButton.pack(side = tk.TOP)
ledGreenLabelButton = tk.Button(frameGREEN, text = "Green: {green}".format(green=liveGreen), font = myFont, height = 2, width =8 )
ledGreenLabelButton.pack(side = tk.TOP)
ledGreenDownButton = tk.Button(frameGREEN, text = "Green -", repeatdelay=500, repeatinterval=myrepeat, font = myFont, command = ledGreenDown, height = 2, width =8 )
ledGreenDownButton.pack(side = tk.TOP)
frameGREEN.pack(fill=tk.Y, side=tk.LEFT)

frameBLUE = tk.Frame(master=window, width=200, bg="blue")
ledBlueUpButton = tk.Button(frameBLUE, text = "Blue +", repeatdelay=500, repeatinterval=myrepeat, font = myFont, command = ledBlueUp, height = 2, width =8 )
ledBlueUpButton.pack(side = tk.TOP)
ledBlueLabelButton = tk.Button(frameBLUE, text = "Blue: {blue}".format(blue=liveBlue), font = myFont, height = 2, width =8 )
ledBlueLabelButton.pack(side = tk.TOP)
ledBlueDownButton = tk.Button(frameBLUE, text = "Blue -", repeatdelay=500, repeatinterval=myrepeat, font = myFont, command = ledBlueDown, height = 2, width =8 )
ledBlueDownButton.pack(side = tk.TOP)
ledPreset1Button = tk.Button(frameBLUE, text = "preset 1", font = myFont, command = loadPreset, height = 2, width =8 )
ledPreset1Button.pack(side = tk.BOTTOM)
frameBLUE.pack(fill=tk.Y, side=tk.LEFT)

window.attributes('-fullscreen', True)
window.mainloop()
