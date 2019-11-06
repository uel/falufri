from PIL import Image, ImageFont, ImageDraw
import datetime
import Matsedel

week = ["MÅNDAG", "TISDAG", "ONSDAG", "TORSDAG", "FREDAG", "LÖRDAG", "SÖNDAG"]


def DagensGastro():
    mat = []
    for x in Matsedel.GetMenu(datetime.datetime.today()).meals:
        mat.append(x.name)
    return mat

today = datetime.datetime(1988,1,1)
gastro = []
dag = ""

def CenteredText(draw, y, text, font):
    w, h = draw.textsize(text, font=font)
    draw.text(((1920-w)/2,y), text, font=font)


def UpdateImage(temp, hum, raining):
    global today
    if today.date() != datetime.datetime.today().date():
        today = datetime.datetime.today()
        gastro = DagensGastro()
        dag = week[today.weekday()]+" VECKA "+str(today.isocalendar()[1])

    im = Image.open("bas.png")
    draw = ImageDraw.Draw(im)
    font22 = ImageFont.truetype("Lato-Regular.ttf", 60)
    font20 = ImageFont.truetype("Lato-Regular.ttf", 75)
    font18 = ImageFont.truetype("Lato-Regular.ttf", 55)


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

    x,y = icon.size

    draw.text((250, 140), str(hum)+"%", font=font22)
    draw.text((int(150+x/2)+65, 260), str(temp)+"°C", font=font22)
    CenteredText(draw, 400, dag, font20)

    for y, m in zip([700,775,850,925], gastro):
        CenteredText(draw, y, m, font18)

    im.paste(icon, (int(198-x/2), 240), icon)
    im.show()
    im.save("image.png")

UpdateImage(-10, 68, True)