from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?cm_sp=Tab_Components_3-_-visnav-_-Video-Graphic-Devices_2'

#this code opens up the connection and grabs the page from the URL above
uClient = uReq(my_url)
page_html = uClient.read() #offloads the content into a variable<<=page>>
uClient.close() #closes the client server

#parsing the html
page_soup = soup(page_html, "html.parser")

#grabs each product into a variable<<containers>>
containers = page_soup.findAll("div",{"class":"item-container"})

filename = "products.csv" #name of the output file 
with open(filename, "w") as f: #'with' used when opening file to ensure closure
    headers = "BRAND, PRODUCT NAME, SHIPPING\n" #title heads in csv file to be written

    f.write(headers) 

    # loops over each product and grabs attributes (which are 3) about each product 
    for container in containers:
        #attribute 1
        brand = container.div.div.a.img["title"]  #selects the brand name from all div about to the title attribute inside image class

        #attribute 2
        title_container = container.findAll("a",{"class":"item-title"})
        product_name = title_container[0].text

        #attribute 3
        shipping_container = container.findAll("li",{"class":"price-ship"}) #Grabs the product shipping information by searching all lists with the class "price-ship".
        shipping = shipping_container[0].text.strip()  #it then cleans the text of white space with strip()

        #code prints the output file
        print("brand: " + brand)
        print("product_name: " + product_name)
        print("shipping: " + shipping)

        f.write(brand + "," + product_name.replace(",", "|") + "," + shipping + "\n") #replaces the commas in the attribute "product name" with "|"