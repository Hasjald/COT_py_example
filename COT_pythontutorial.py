""" 
    COT_pythontutorial.py
    python 3.9 64-bit  
    Created by Harald Sæther   
------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------
This python script serves as an example of how to communicate with circusofthings.com through the server
REST-api Goto https://circusofthings.com/api.jsp for more info on the Rest Json commands.
In this example we will feed a signal to the circusofthings Dashboard, and Read values on the same signal.
There are a few things you need to check and set yourself. The requests library and json libraries should
be included in the latest python else checkout pypi.org for both libraries. 3 things you need to set is the
signal key, value and circustoken. The signal key can be found in COT along with the circustoken, the value 
can be whatever.  
------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------
"""
""" 2xLibraries needed """
import requests  # Lib should be included in latest python versions else do: python -m pip install requests   
import json      # Lib should be included in latest python versions else do: python -m pip install json 

"""variable and constants"""
KEY_1   ="12345"                #put your signal key here  
VALUE_1 = 3.14                  #this is a variable
TOKEN_1  ="your_key_here"       #the token is found under account in circusofthings.com

"""defining our dict, this will be the payload and data to be put in the json body"""
data_1={'Key':'0','Value':0,'Token':'0'} 

"""to update the dict do something like this""" 
data_1['Key']=KEY_1 
data_1['Value']=VALUE_1
data_1['Token']=TOKEN_1
"""These are optional location parameters, currently set to Storskrymten, Norway """
data_1['Lat'] =62.3725  #denoted in decimaldegrees
data_1['Lon'] =9.061667
data_1['Alt'] =1985     

"""Then we do the PUT request"""
response=requests.put('https://circusofthings.com/WriteValue',
				data=json.dumps(data_1),headers={'Content-Type':'application/json'}) #There can be additional things 

"""example of error handling"""
if(response.status_code==200):
    print("succsess")
else:
    print("error %d" % (response.status_code))
#-----------------------------------------------------------------------------------------------------------------------#
"""The Get request is shown below"""
payload = data_1
response=requests.get('https://circusofthings.com/ReadValue',params=payload)

print(response.content) #prints the content

"""save our Get values"""
datahandling=json.loads(response.content)  
print(datahandling["Value"]) #here we parse and get the value of the signal


