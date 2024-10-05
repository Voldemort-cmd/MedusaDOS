#!/usr/bin/env python3

import os
import sys
import httpx
from colorama import Fore, init

init(autoreset=True)

fr = Fore.RED
fg = Fore.GREEN
fy = Fore.YELLOW
fw = Fore.WHITE
fre = Fore.RESET

url_list = [
    'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt',
    # Add other URLs as needed
]  

if __name__ == "__main__":
    file = "proxy.txt"
    
    try:
        if os.path.isfile(file):
            os.system('cls' if os.name == 'nt' else 'clear')
            os.remove(file)
            print(f"{fr}File {file} already exists!\n{fy}Starting to download a new {file}!\n")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')

        with open(file, 'a') as data:
            for proxy in url_list:
                try:
                    response = httpx.get(proxy)
                    response.raise_for_status()  # This will raise an exception for HTTP errors
                    data.write(response.text)
                    print(f" -| Fetching {fg}{proxy}")
                except httpx.HTTPStatusError as e:
                    print(f"{fr}HTTP error occurred: {e.response.status_code} for URL {proxy}")
                except httpx.RequestError as e:
                    print(f"{fr}Request error occurred: {e}")

        with open(file, 'r') as count:
            total = sum(1 for line in count)
        print(f"\n{fw}({fy}{total}{fw}) {fg}Proxies successfully downloaded.")

    except Exception as e:
        print(f"{fr}An unexpected error occurred: {str(e)}")
        sys.exit(1)
