# @author HGDIV
from bs4 import BeautifulSoup
import urllib.request
import PySimpleGUI as sg


def handleScrape(url, e1, e2):
    targetUrl = urllib.request.urlopen(url)
    soup = BeautifulSoup(targetUrl, 'html.parser')
    e1.update('Pull Data From Selected Tags')
    e2.update(soup.prettify())


sg.theme('Material2')
layout = [
    [sg.Text('Input the URL that you want to scrape')],
    [sg.InputText(key='input')],
    [sg.Button('Scrape'), sg.Exit('Exit')],
    [sg.Output(size=(80, 20), key='output')]
]

window = sg.Window('Web-Scraper-Python', layout)


while True:  # Event Loops
    event, values = window.read()
    if event == 'Exit':
        break
    if event == 'Scrape':
        url = values['input']
        e1 = window['Scrape']
        e2 = window['output']
        handleScrape(url, e1, e2)

window.close()
