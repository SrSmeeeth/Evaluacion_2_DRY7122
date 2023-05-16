import requests
import urllib.parse

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "Sc5dcy9YJjRw6kM0xWCrccHi8qkCSePl"

while True:
    orig=input("Ciudad de origen: ")
    if orig == "quit" or orig =="q":
        break
    dest=input("Ciudad de Destino: ")
    if dest == "quit" or dest =="q":
        break
    url=main_api + urllib.parse.urlencode({"key":key,"from":orig,"to":dest})
    json_data=requests.get(url).json()
    json_status=json_data["info"]["statuscode"]
    if json_status== 0:
        print("=============================")
        print("Direccion Desde: " + (orig) + " a " + (dest))
        print("Duración del viaje: " + (json_data["route"]["formattedTime"]))
        print("Distancia en Kilometros: " + str("{:.2f}".format((json_data["route"]["distance"])*1.61))+ " Kms.")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61)+ "Km"))
    elif json_status == 402:
        print("**************************************************")
        print("Status Code: "+ str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**************************************************\n")
    elif json_status == 611:
        print("**************************************************")
        print("Status Code: "+ str(json_status) + "; Missing and entry for one or both locations.")
        print("*************************************************\n")
    else:
        print("**************************************************")
        print(" For Status code: " + str(json_status) + "; Refer to:")
        print(" https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("*************************************************\n")