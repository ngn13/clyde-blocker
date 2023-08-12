#!/bin/python3
import requests
import platform

def main():
    tok = input("[>] Enter your discord token: ")
    url = "https://discord.com/api/v9/users/@me/relationships/1081004946872352958" # the api endpoint
    res = requests.put(url, json={"type": 2}, headers={"Authorization": tok})

    # if the response text contains "401: Unauthorized" then the provided
    # token is invalid
    if "401: Unauthorized" in res.text:
        print("[-] Token is not valid")
        return

    if res.text != "":
        print(f"[-] Unexpected response: {res.text}")
        return 

    print("[+] Clyde has been blocked!")

if __name__ == "__main__":
    # epic banner 
    print("""
░█▀▀░█░░░█░█░█▀▄░█▀▀░░░█▀▄░█░░░█▀█░█▀▀░█░█░█▀▀░█▀▄
░█░░░█░░░░█░░█░█░█▀▀░░░█▀▄░█░░░█░█░█░░░█▀▄░█▀▀░█▀▄
░▀▀▀░▀▀▀░░▀░░▀▀░░▀▀▀░░░▀▀░░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀░▀
         github.com/ngn13/clyde-blocker
    """)

    # handle keyboard interrupt (ctrl+c)
    try:
        main()
    except KeyboardInterrupt:
        print("\n[-] Cancelled")

    if platform.system() != "Linux":
        input("[*] Hit enter to close the program\n")
