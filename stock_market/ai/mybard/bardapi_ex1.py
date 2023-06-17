## https://github.com/dsdanielpark/Bard-API
# #pip install bardapi
#Visit https://bard.google.com/
#F12 for console
#Session: Application → Cookies → Copy the value of  __Secure-1PSID cookie.
#Secure-1PSID=XQhZhhB-gnDDlA_Zskt4wxVOFxfUS0pKtNeNFI5UMdOhCLsfDuLuAnvgC8iJSj2i8ZIegw.
from bardapi import Bard

token = 'XQhZhhB-gnDDlA_Zskt4wxVOFxfUS0pKtNeNFI5UMdOhCLsfDuLuAnvgC8iJSj2i8ZIegw.'
bard = Bard(token=token)
ans = bard.get_answer("What's are applications with an api that can be added to the apple devices share butoon to and have an api to retrieve from using python")['content']
print(ans)