
from bs4 import BeautifulSoup
import time
import requests as req

DEBUG=False   #temp

parms = ['slab_id','meltting_id','slab_length','slab_width','line_speed']

def get_plc_values():
    # Requesting for the website

    t1 =time.time()

    my_dict = {}
    flag = False
    try:
        if not DEBUG:
            Web = req.get('http://192.168.0.1/awp/dorsa/Dorsa_WSP_MSC01.html')
            content = BeautifulSoup(Web.text, 'lxml')
            flag = True
    #     # Creating a BeautifulSoup object and specifying the parser
    except:
        Web =  open("Web_Server.html", "r")
        content = BeautifulSoup(Web, 'lxml')
    # Printing the Code, name, and text of a tag
    if DEBUG:
        Web =  open("Web_Server.html", "r")
        content = BeautifulSoup(Web, 'lxml')

    for _,tag in enumerate(content.find_all('td')):
    
    # Printing the name, and text of p tag
        # print(parms[_],tag.text)
        try:
            my_dict.update({parms[_]:tag.text})
        except:
            my_dict.update({parms[_]:-2})


    return flag , my_dict


if __name__ == '__main__':

    _,a=get_plc_values()
    print(a)