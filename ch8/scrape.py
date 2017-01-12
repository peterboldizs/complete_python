import argparse
import base64
import json
import os
from bs4 import BeautifulSoup
import requests


def scrape(url, format_, type_):
    try:
        page = requests.get(url)
    except requests.RequestException as rex:
        print(str(rex))
    else:
        soup = BeautifulSoup(page.content, 'html.parser')
        images = _fetch_images(soup, url)
        images = _filter_images(images, type_)
        _save(images, format_)


def _fetch_images(soup, base_url):
    images = []
    for img in soup.find_all('img'):
        src = img.get('src')
        img_url = (
            '{base_url}/{src}'.format(base_url=base_url, src=src)
        )
        name = img_url.split('/')[-1]
        images.append(dict(name=name, url=img_url))
    return images


def _filter_images(images, type_):
    if type_ == 'all':
        return images
    ext_map = {
        'png': ['.png'],
        'jpg': ['.jpg'],
    }
    return [
        img for img in images
        if _matches_extension(img['name'], ext_map[type_])
    ]


def _matches_extension(filename, extension_list):
    name, extension = os.path.split(filename.lower())
    return extension in extension_list


def _save(images, format_):
    if images:
        if format_ == 'img':
            _save_images(images)
        else:
            _save_json(images)


def _save_images(images):
    for img in images:
        img_data = requests.get(img['url']).content
        with open(img['name'], 'wb') as f:
            f.write(img_data)


def _save_json(images):
    data = {}
    for img in images:
        img_data = requests.get(img['url']).content
        b64_img_data = base64.b64encode(img_data)
        str_img_data = b64_img_data.decode('utf-8')
        data[img['name']] = str_img_data
    with open('images.json', 'w') as ijson:
        ijson.write(json.dumps(data))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='scrape a webpage'
    )
    parser.add_argument(
        '-t',
        '--type',
        choices = ['all', 'jpg', 'png'],
        default= 'all',
        help = 'the image type'
    )
    parser.add_argument(
        '-f',
        '--format',
        choices = ['img', 'json'],
        default= 'img',
        help = 'the image format'
    )
    parser.add_argument(
        'url',
        help = 'the image webpage url'
    )
args = parser.parse_args()
scrape(args.url, args.format, args.type)