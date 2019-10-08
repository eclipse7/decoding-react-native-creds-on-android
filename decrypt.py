from Crypto.Cipher import AES
from base64 import b64decode
key = b64decode('f8WwucPW1fxcJ/sb65X2Dz9qkd4xrOZmKdmyIgOTtRM=')

crypted_list = [b64decode('AQIvZ0rae6csEKp09v5UvJfWyehtBM3rtPHsRJIPVxHyyaZGy/v9xFnGv18='),
                b64decode('AQIn08cVW4SAPsqT4VdX24WeRh+WO/4lrMbh436HMSYRv0q09P0='),
                b64decode('''AQI5CFY7+Sq8DGq7XYD7X8EyXZcUOjWka2WETTgK1zOu6oAOwE1cParQ4KvMyV60FoH2AcJOErQ6
r+0ZqeHuoMo2igaug7cKEhOj0iFMrwE6Ad4yjoq582P0OQy5upMBia86SIRLqDNZlniFNWJUUJdk
+a+FaV7jrtXzgtuLU838YkUCXV+NihesneXXlrPEJCb74SmfxUh2VROdip/uy9k+k6qXWFB6+Cnn
uY11sZhlCiWb4ofccD7Iz7JdnT+cFOOIbAh0UjBVYwqijae3WfenUSgFzwX/V20E3vYAo+T+aF2I
YtPVluKxLdSpfb6SvHAs3EK5bvA0S2487mVUFyt1Ov7ULRlGXiQ0we4A3ieHEAu1agilgyDq+bxI
Kb9/C8veYvtSFvG6KHyxrx9kG1msw5gOQYRG431N8Ns4eIfTaRcBCqqyiq2/0hWRato3nNWSk/1s
U6GoRrFzE6Pi9TcxoK9zQ8vOqikpEoU5OjHU6F/3dyA51+F7K0CFGhGNAywd+5bbkloTK9Cu0mZe
HLzPMTnAY8J8rR3kSO3980k8Y22Xi85c7noOXdR4iYIbrwsEnmn1oGYc+8eDrTTPu2OTpo+zeMz9
XbOsY+L6JinQaP47AgUuc+H111cXWdBV4Sw4rIT2pXA7mj5a8gUyECAHGxKutYUFiwmk6Y9IGm8S
72MSEDLh+CUDXIP4t/DmrVMg9r1YXI3cyY2MqfoUImzc65Ls4cVRyUeHm9fiehcxfJXdYmiYk437
IH3c3I2KGBqZe/yIOIPhfuKX1ObZPuC1hPfKEMQu4VdX7XMMvtWKvzYeP7X9VfPU0Evh/evMBFCK
UUqdeSUxGNq8eENAfjlzf2dxYFTg0659lmM/t/UW8dVbgu9ZkleAmyfktmC42aCKiczqtWx62lKF
nZcJHoQu1eqnDvCDZAP4amFFYiYGTdqDoTGqv9TSAcsVQEWYUiCfXQGzZq0+P/IGgeV+ACLscpF4
PyJe1KhBOHZRny9n3a6dprblFs65TKWVSnWiXui50A4NlUZyQKUpuDD3yXukwFQ5fGYxnuE0ZcDl
Pem/JvAFVYRussyDceEeLgCwEm/g+r2Riw/8RteFRNA3B7NngctP5wcu106AqVPP6PrnIbMLRlkQ
gQhr2zKXp2Mqx6mgREWIhfkpPEDoJuGEEHOR'''),
                b64decode('AQL+SIyCOQTbwB84By9oa1NNruzfEO3xQMx/Qj5IQBWbPQ+w83nDf3vI1qo6CVvG9+ikvN4L3CcdrKq5lPnT1bE=')]

for crypted_text in crypted_list:
    a = AES.new(key, AES.MODE_GCM, crypted_text[2:14])
    print(a.decrypt(crypted_text[14:]))
