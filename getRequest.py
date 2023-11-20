import requests
import json

def get_information(customerID):
    apiKey = "a9282381ed7bd328f1629800e1706070"
    url = "https://eu-api.jotform.com/user/submission/{customerID}?apiKey={myApiKey}".format(myApiKey=apiKey,customerID=customerID)
    response = requests.get(url)
    if(response.status_code==200):
        data = response.json()
        IDNumber=(data['content']['answers']['8']['answer'])
        anotherFamilyMember=(data['content']['answers']['9']['answer'])
        NumberOfPersons =(data['content']['answers']['10']['answer'])
        Name = (data['content']['answers']['11']['answer'])
        LastName = (data['content']['answers']['12']['answer'])
        Email = (data['content']['answers']['13']['answer'])
        birthday = (data['content']['answers']['14']['answer']['day']) + "." + (data['content']['answers']['14']['answer']['month']) +"."+(data['content']['answers']['14']['answer']['year'])
        request = (data['content']['answers']['20']['answer'])
        Country = (data['content']['answers']['27']['answer'])
        try:
            FamilyMemberCountry = (data['content']['answers']['28']['answer'])
        except:
            FamilyMemberCountry = ""
        service = (data['content']['answers']['29']['answer'])
        return Name,LastName,birthday,Email,IDNumber,Country,NumberOfPersons,anotherFamilyMember,FamilyMemberCountry,request,service


def get_submissionID(device_ID):
    firebase_url = 'https://pythonrobocorp-default-rtdb.europe-west1.firebasedatabase.app/{device_ID}/submissionID.json'.format(device_ID=device_ID)
    # Adjust the path to your specific data
    response = requests.get(firebase_url)

    # Check the response status code
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        return data
    
    # Construct the URL

def is_machine_allowed(device_ID):
    firebase_url = 'https://pythonrobocorp-default-rtdb.europe-west1.firebasedatabase.app/%7B{device_ID}%7D.json'.format(device_ID=device_ID)
    # Adjust the path to your specific data
    response = requests.get(firebase_url)

    # Check the response status code
    if response.status_code == 200:
        # Parse the JSON response
        return True
    else:
        return False


def send_request(device_ID):
    url = 'https://pythonrobocorp-default-rtdb.europe-west1.firebasedatabase.app/request.json'
    data = {
    'registration request from device_ID': device_ID
    }

# Convert the data to JSON format
    json_data = json.dumps(data)
    response = requests.post(url,json_data)
    if response.status_code == 200:
        print('request sent successfully to Server!')
    else:
        print('Error:', response.status_code, response.text)



def send_report(device_ID,name,family):
    url = 'https://pythonrobocorp-default-rtdb.europe-west1.firebasedatabase.app/appointments.json'
    data = {
    'appointment got from device_ID': device_ID + " for " + name + " " + family
    }

# Convert the data to JSON format
    json_data = json.dumps(data)
    response = requests.post(url,json_data)
    if response.status_code == 200:
        print('appointment registiration done successfully!')
    else:
        print('Error:', response.status_code, response.text)
#send_request("293A6EE2-CB53-4420-8C5D-529C9EC990AC")
#get_information(5729338367975564387)
#get_submissionID("293A6EE2-CB53-4420-8C5D-529C9EC990AC")
#send_report("293A6EE2-CB53-4420-8C5D-529C9EC990AC","Milad","khaghanirad")
#is_machine_allowed("293A6EE2-CB53-4420-8C5D-529C9EC990AC")
