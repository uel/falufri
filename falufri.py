from PIL import Image, ImageFont, ImageDraw
import datetime

week = ["MÅNDAG", "TISDAG", "ONSDAG", "TORSDAG", "FREDAG", "LÖRDAG", "SÖNDAG"]


def DagensGastro():
    return ["", "", "", ""]

today = datetime.datetime(1988,1,1)
gastro = []
dag = ""

def UpdateImage(temp, hum, raining):
    global today
    if today.date() != datetime.datetime.today().date():
        today = datetime.datetime.today()
        gastro = DagensGastro()
        dag = week[today.weekday()]+" VECKA "+str(today.isocalendar()[1])

    im = Image.open("bas.png")
    draw = ImageDraw.Draw(im)
    font22 = ImageFont.truetype("Lato-Regular.ttf", 40)
    font20 = ImageFont.truetype("Lato-Regular.ttf", 20)
    font18 = ImageFont.truetype("Lato-Regular.ttf", 18)
    font17 = ImageFont.truetype("Lato-Regular.ttf", 17)

    icon = "temp.png"
    if temp < 0:
        icon = "temp0.png"
    elif temp > 20:
        icon = "temp2.png"
    if raining:
        icon = "rain.png"
        if temp < 0:
            icon = "snow.png"
            
    icon = Image.open(icon)

    draw.text((250, 170), str(hum)+"%", font=font22)
    draw.text((250, 250), str(temp)+"", font=font22)


    im.paste(icon, (135, 250), icon)
    im.show()

UpdateImage(20,68, False)