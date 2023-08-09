from bs4 import BeautifulSoup
import requests
import library.exlib as lib


lib.Monogram()
print('\n\033[31mDISCLAIMER\nThis script is intended only for testing or evaluation purposes and should not be used in a production environment and may contain uncensored language or other potentially offensive content that is not suitable for all audiences. Script is not yet fully developed or validated, and may contain errors, bugs, or other issues that could impact the functionality or usability of the system. It is important to ensure that the script is not accidentally shared or used in a public environment, where it could cause harm or offense. Users should exercise caution and discretion when using the script, and should not rely on it for any critical or sensitive operations.\033[0m')

url = input("enter ig link: ")
request = requests.get(url)

s = BeautifulSoup(request.text, "html.parser")

meta = s.find("meta", property="og:description")
s = meta.attrs['content'].split(" ")

if len(s)>16:
    name = s[13]+" "+s[14]+" "+s[15]
else:
    name = s[13]+" "+s[14]

print("\nNote:- Data is fetched from meta which may be different from details on profile.\n")
print("Name: ",name)
print("Username: ",s[-1])
print("Followers: ", s[0])
print("Following: ", s[2])
print("Posts: ", s[4])
