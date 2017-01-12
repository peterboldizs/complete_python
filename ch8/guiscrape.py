from tkinter import *
from tkinter import ttk, filedialog, messagebox
import argparse
import base64
import json
import os
from bs4 import BeautifulSoup
import requests


def fetch_url():
    pass


def save():
    pass

if __name__ == "__main__":
    _root = Tk()
    _root.title('BP Scrape app')
    _mainframe = ttk.Frame(_root, padding='5 5 5 5')
    _mainframe.grid(row=0, column = 0, sticky = (E, W, N, S))

    _url_frame = ttk.LabelFrame(_mainframe, text = 'URL', padding='5 5 5 5')
    _url_frame.grid(row=0, column = 0, sticky = (E, W))
    _url_frame.columnconfigure(0, weight=1)
    _url_frame.rowconfigure(0, weight=1)

    _url = StringVar()
    _url.set('http://localhost:8000')

    _url_entry = ttk.Entry(_url_frame, width = 40, textvariable = _url)
    _url_entry.grid(row=0, column = 0, sticky = (E, W, S, N), padx = 5)

    _fetch_button = ttk.Button(_url_frame, text='Fetch info', command=fetch_url)
    _fetch_button.grid(row=0, column = 1, sticky = W, padx = 5)

    _img_frame = ttk.LabelFrame(_mainframe, text='Content', padding='9 0 0 0')
    _img_frame.grid(row = 1, column = 0, sticky = (N, S, E, W))

    _images = StringVar()
    _img_listbox = Listbox(_img_frame, listvariable=_images, height = 6, width = 25)
    _img_listbox.grid(row=0, column=0, sticky=(E, W), pady=5)

    _scrollbar = ttk.Scrollbar(_img_frame, orient = VERTICAL, command=_img_listbox.yview)
    _scrollbar.grid(row=0, column=1, sticky=(S,N), pady=6)
    _img_listbox.configure(yscrollcommand=_scrollbar.set)

    _radio_frame = ttk.Frame(_img_frame)
    _radio_frame.grid(row=0, column=2, sticky=(N, S, W, E))

    _choice_label = ttk.Label(_radio_frame, text='Choose how to save image')
    _choice_label.grid(row=0, column=0, padx=5, pady=5)

    _save_method =StringVar()
    _save_method.set('img')
    _img_only_radio = ttk.Radiobutton(_radio_frame, text='as images', variable=_save_method, value='img')
    _img_only_radio.grid(row=1, column=0, padx=5, pady=2, sticky = W)
    _img_only_radio.configure(state='normal')

    _json_radio = ttk.Radiobutton(_radio_frame, text='as json', variable=_save_method, value='json')
    _json_radio.grid(row=2, column=0, padx=5, pady=2, sticky=W)

    _scrape_button = ttk.Button(_mainframe, text='Scrape!', command=save)
    _scrape_button.grid(row=2, column=0, sticky=E, pady=5)

    _status_frame = ttk.Frame(_root, relief='sunken', padding='2 2 2 2')
    _status_frame.grid(row=1, column=0, sticky=(E, W, S))
    _status_msg = StringVar()
    _status_msg.set('Type a URL to start scraping...')
    _status = ttk.Label(_status_frame, textvariable=_status_msg, anchor=W)
    _status.grid(row=0, column=0, sticky=(E, W))

    _root.mainloop()


