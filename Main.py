# @author HGDIV
from bs4 import BeautifulSoup
import urllib.request
import PySimpleGUI as sg


def handleScrape(url):
        window['output'].update()
        targetUrl = urllib.request.urlopen(url, [None])
        soup = BeautifulSoup(targetUrl, 'html.parser')
        window['output'].update(soup.prettify())
        layout.append(sg.Button('Submit Filter'))





sg.theme('Material2')
layout = [
    [sg.Text('Input the URL that you want to scrape')],
    [sg.InputText(key='input')],
    [sg.Button('Scrape'), sg.Exit('Exit')],
    [sg.Output(size =(80,20), key='output')]
]

window = sg.Window('Web-Scraper-Python', layout)


while True:  # Event Loops
    event, values = window.read(timeout=10)
    print(event, values)
    if event in (None, 'Exit'):
        break
    if event == 'Scrape':
        url = values['input']
        handleScrape(url)




