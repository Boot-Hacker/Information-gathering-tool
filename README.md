# Information-gathering-tool
This is a basic information gathering tool using python-3.9. 
We can use this tool to caputer possible information about corrosponding IP ,Domain ,website. 

DETAILS OF USES LIBARIES : 

  1. WHOIS : Extract the capable data about given domain.
     Offical link : https://pypi.org/project/python-whois/
     Here you also get the process od installation.
  
  2. DnsPython : dnspython is a DNS toolkit for Python. It supports almost all record types. It can be used for queries, zone transfers, and dynamic updates. 
     Offical link : https://pypi.org/project/dnspython/
  
  3. Shodan : Shodan is a search engine for Internet-connected devices. Google lets you search for websites, Shodan lets you search for devices.
     Offical link : https://pypi.org/project/shodan/
  
  
  **
Steps To Follow **
---------------------------------------------------------------------

-> Install all necessary libary file into your system. [like shodan,Whois]

-> Download info_gathering.py

-> chmod +x info_gathering.py{Linux}

-> Go to the path where download ".py" file.

-> command : "python3 info_gathering.py -h"


**Example :**
---------------------------------------------------------------------
-> Get help for arguments to exxecute command.

      command : python3 info_gathering.py -h
      
   ![Screenshot (138)](https://user-images.githubusercontent.com/87462515/175241974-8557fe36-3b28-4095-9a52-58bbd8167d2b.png)
  

-> Get details of 'google.com' through 192.168.228.1

    command : python3 info_gathering.py -d google.com -s 192.168.228.1
   
   ![Screenshot (140)](https://user-images.githubusercontent.com/87462515/175242423-d8976526-0c54-4bb3-ad7c-a8a42292a474.png)
