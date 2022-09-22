import httpx
import threading
import time,os
import sys
import requests,json
import utils,random
from colorama import Fore
email_domains = ['@outlook.fr','@outlook.com','@gmail.com','@protonmail.com','@yahoo.com','@hotmail.com']
gender = ['1','2']


with open('config.json') as cf:
    config = json.load(cf)

os.system('title SpotifyUwU [Generator] Support : @terminaluwu - Terminal#2074')
print(Fore.CYAN+"""                                                                                                  
 @@@@@@   @@@@@@@    @@@@@@   @@@@@@@  @@@  @@@@@@@@  @@@ @@@  @@@  @@@  @@@  @@@  @@@  @@@  @@@  
@@@@@@@   @@@@@@@@  @@@@@@@@  @@@@@@@  @@@  @@@@@@@@  @@@ @@@  @@@  @@@  @@@  @@@  @@@  @@@  @@@  
!@@       @@!  @@@  @@!  @@@    @@!    @@!  @@!       @@! !@@  @@!  @@@  @@!  @@!  @@!  @@!  @@@  
!@!       !@!  @!@  !@!  @!@    !@!    !@!  !@!       !@! @!!  !@!  @!@  !@!  !@!  !@!  !@!  @!@  
!!@@!!    @!@@!@!   @!@  !@!    @!!    !!@  @!!!:!     !@!@!   @!@  !@!  @!!  !!@  @!@  @!@  !@!  
 !!@!!!   !!@!!!    !@!  !!!    !!!    !!!  !!!!!:      @!!!   !@!  !!!  !@!  !!!  !@!  !@!  !!!  
     !:!  !!:       !!:  !!!    !!:    !!:  !!:         !!:    !!:  !!!  !!:  !!:  !!:  !!:  !!!  
    !:!   :!:       :!:  !:!    :!:    :!:  :!:         :!:    :!:  !:!  :!:  :!:  :!:  :!:  !:!  
:::: ::    ::       ::::: ::     ::     ::   ::          ::    ::::: ::   :::: :: :::   ::::: ::  
:: : :     :         : :  :      :     :     :           :      : :  :     :: :  : :     : :  :   
                                                                                                  """+Fore.RESET)

print(Fore.LIGHTRED_EX+"                                    https://t.me/terminaluwuu-Terminal#1337  "+Fore.RESET)
# proxy_method = input(Fore.LIGHTMAGENTA_EX+"Proxy Method[>] "+Fore.RESET)
threadCount = int(input(Fore.LIGHTMAGENTA_EX+"Number of Threads[>] "+Fore.RESET))

with open("proxies.txt") as fp:
    proxy_list = fp.read().splitlines()

success_count = 0
error_count = 0
def Gen():

    
    global success_count
    global error_count
    global gender_val
    global birth_date
    birth_date = str(utils.getyear())+"-11-02"
    global email_val
    global user_name
    email_val = utils.email() + random.choice(email_domains)
    user_name = utils.user()
    gender_val = random.choice(gender)
    if config['proxied'] == 'True':
        proxy_val = "http://"+str(random.choice(proxy_list))
    elif config['proxied'] == 'False':
        proxy_val = None



    payload = {
   "account_details" : {
      "birthdate" : birth_date,
      "consent_flags" : {
         "eula_agreed" : 'true',
         "send_email" : 'true',
         "third_party_email" : 'false'
      },
      "display_name" : user_name,
      "email_and_password_identifier" : {
         "email" : email_val,
         "password" : config['password']
      },
      "gender" : gender_val
   },
   "callback_uri" : "https://www.spotify.com/signup/challenge?locale=in-en",
   "client_info" : {
      "api_key" : "a1e486e2729f46d6bb368d6b2bcda326",
      "app_version" : "v2",
      "capabilities" : [ 1 ],
      "installation_id" : "fc1e5e8c-1482-450e-b6f3-bd880944c1f3",
      "platform" : "www"
   },
   "tracking" : {
      "creation_flow" : "",
      "creation_point" : "https://www.spotify.com/in-en/free/?utm_source=in-en_brand_contextual_text&utm_medium=paidsearch&utm_campaign=alwayson_asia_in_premiumbusiness_core_brand_neev+contextual+in-en+google",
      "referrer" : ""
   }
}


    
    header = {
    'Accept' : '*/*',
    'Accept-Encoding' : 'gzip, deflate',
    'Accept-Language' : 'en-GB,en-US;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    # 'Content-Length': '764',
    'Content-Type' : 'application/json',
    'Host' : 'spclient.wg.spotify.com',
    'Origin' : 'https://www.spotify.com',
    'Referer' : 'https://www.spotify.com/',
    'sec-ch-ua' : '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile' : '?0',
    'sec-ch-ua-platform' : '"Windows"',
    'Sec-Fetch-Dest' : 'empty',
    'Sec-Fetch-Mode' : 'same-site',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'

}
    if gender_val == '1':
        gender_info = "Male"
    elif gender_val == '2':
        gender_info = "Female"
    try:
        r = httpx.post('https://spclient.wg.spotify.com/signup/public/v2/account/create',headers=header,json=payload,proxies=proxy_val,timeout=None).json()
        #print(r)
        print(Fore.GREEN+"Account Created - Email: "+email_val+'| Password: '+config['password']+'| Gender: '+gender_info+'| DOB: '+birth_date+Fore.RESET)
        file = open('accounts.txt','a')
        file.write(email_val+':'+config['password']+':'+gender_info+':'+birth_date+'\n')
        file.close()
        success_count += 1
        os.system('title SpotifyUwU [Now Generating] Support : Terminal#1337 - Success: '+str(success_count)+'Error: '+str(error_count))
        Gen()
    except Exception as e:
        os.system('title SpotifyUwU [Now Generating] Support : @terminaluwu - Terminal#1337 - Success: '+success_count+' Error: '+error_count)
        Gen()
    


threads = []
for i in range(threadCount):
     t = threading.Thread(target=Gen)
     t.start()
     threads.append(t)
for i in range(threadCount):
    threads[i].join()
