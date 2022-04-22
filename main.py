import os
from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen
import requests
import pytesseract
from PIL import Image

import easyocr



reader = easyocr.Reader(['en','ar'])

folder = "hyper 1 "
fw=open(folder+".txt","w")
os.makedirs(folder)
f= open(folder+".csv","w")
header="image_name,image_url\n"
f.write(header)
for p in range(1, 7):
    url = "https://3orod.net/%d8%b9%d8%b1%d9%88%d8%b6-%d9%87%d8%a7%d9%8a%d8%a8%d8%b1-%d9%88%d8%a7%d9%86/%d8%b9%d8%b1%d9%88%d8%b6-%d9%87%d8%a7%d9%8a%d8%a8%d8%b1-%d9%88%d8%a7%d9%86-%d8%ad%d8%aa%d9%89-25-%d8%a5%d8%a8%d8%b1%d9%8a%d9%84-2022/" + str(p) + "/"
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    client = urlopen(req)
    html = client.read()
    client.close()
    soup = bs(html, "html.parser")
    div_of_img = soup.findAll("div", {"class": "entry-contentxyz"})
    par_of_img = div_of_img[0].findAll("p", {"style": "text-align: center;"})
    imgaes = []
    for i in par_of_img:
        name = i.img['alt']
        link = i.img['src']
        image_data= name+","+"https://3orod.net" + link+"\n"
        f.write(image_data)
        imgaes.append(i.img['src'])
        with open(folder+"/" + name.replace(" ", "_").replace("/", " ") + ".jpg", 'wb') as fs:
            im = requests.get("https://3orod.net" + link)
            fs.write(im.content)
        output = reader.readtext(folder + "/" + name.replace(" ", "_").replace("/", " ") + ".jpg")
        for w in output:
            fw.write(w[1] + "\n")






