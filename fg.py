import json

print(f"""

\033[31moooo   o8o   .o88o.     .                                     \033[0mVersion:           
\033[31m `888   `"'   888 `"\   .o8                                   \033[0mAPI Server: api.icey.fr
\033[32m 888  oooo  o888oo  .o888oo      oo.ooooo.  oooo    ooo       \033[0mCurrent date:
\033[32m 888  `888   888      888        888' `88b  `88.  .8'         \033[0mCurrent time: 
\033[33m 888   888   888      888        888   888   `88..8'          \033[0mFile path: 
\033[33m 888   888   888      888 . .o.  888   888    `888'           
\033[34mo888o o888o o888o     `888" Y8P  888bod8P'     .8'     
\033[34m                                 888       .o..P'      
\033[35m                                o888o      `Y8P'   
\033[0m                              
                                """)

from urllib.request import urlopen
import os
import time
from datetime import datetime

now = datetime.now()
ctzo = now.strftime("%Y-%m-%d")
cto = now.strftime("%H:%M:%S")
cvf = os.getcwd()
ghda = ctzo + " " + cto

url = "http://api.icey.fr/gateway/connect.json"
response = urlopen(url)
data_json = json.loads(response.read())
connectwss = data_json['active']
connectcode = data_json['public_code']

if connectwss == "true":
    print(f"\033[31mI \033[33m{ghda} \033[32mliftcord.gateway \033[0m\033[1mCollecting data from \033[1mapi.icey.fr/gateway/connect.json\033[0m")
    time.sleep(.5)
    print(f"\033[31mI \033[33m{ghda} \033[32mliftcord.api \033[0m\033[1mConnected to \033[1mapi.icey.fr/gateway/connect.json\033[0m")
    print(f"\033[31mI \033[33m{ghda} \033[32mliftcord.api \033[0m\033[1mUsing public code {connectcode}")
elif connectwss == "false":
    print(f"\033[31mI \033[33m{ghda} \033[32mliftcord.gateway \033[0m\033[1mCollecting data from \033[1mapi.icey.fr/gateway/connect.json\033[0m")
    time.sleep(.5)
    print(f"\033[31mI \033[33m{ghda} \033[32mliftcord.gateway \033[0m\033[1mConnection refused \033[1mapi.icey.fr/gateway/connect.json\033[0m")
else:
    print(f"\033[31mI \033[33m{ghda} \033[32mliftcord.gateway \033[0m\033[1mUnexpected error while connecting \033[1mapi.icey.fr/gateway/connect.json\033[0m")

print(data_json)