import requests
import json

url = "http://localhost:3000/"

class TestCreateUser:
    def test_basic_1(self):
        payload = {
            "uuid": "e3c5e629-5cf5-434d-a7db-a2a69c7cac13",
            "name": "Jeff Bezos",
            "birthdate": -188420400.0,
            "sex": "male",
            "email": "mynamejeff@amazon.com"            
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url + "createUser", data=json.dumps(payload), headers=headers)
        print(response.text)
        assert response.status_code == 200
        assert response.ok

    def test_basic_2(self):
        payload = {
            "uuid": "2e9348d2-91a5-4eac-8419-b03f09772af2",
            "name": "Alice in Wonderland",
            "birthdate": 367821801.5,
            "sex": "female",
            "email": "rabbit@wonderland.co.uk"            
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url + "createUser", data=json.dumps(payload), headers=headers)
        print(response.text)
        assert response.status_code == 200
        assert response.ok

    def test_invalid_uuid_1(self):
        payload = {
            "uuid": "7fd26b27-af88-455a-a28c-00c3e29bc87",
            "name": "Bill Gates",
            "birthdate": 7892164720.5,
            "sex": "male",
            "email": "bill.gates@microsoft.com"            
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url + "createUser", data=json.dumps(payload), headers=headers)
        print(response.content.decode())
        assert response.status_code == 400
        assert response.content.decode() == "Invalid UUID"
    
    def test_invalid_uuid_2(self):
        payload = {
            "uuid": "b6d6cd07--8e4d-4327-b1fb-81eb74113ecf",
            "name": "Harry Potter",
            "birthdate": 12479181.0,
            "sex": "male",
            "email": "Harry_Potter@HogwardsSchoolofWitchcraftAndWizardry.co.uk"            
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url + "createUser", data=json.dumps(payload), headers=headers)
        print(response.content.decode())
        assert response.status_code == 400
        assert response.content.decode() == "Invalid UUID"

    def test_invalid_name_1(self):
        payload = {
            "uuid": "4a907f28-251c-4c5d-899c-65cd78970e36",
            "name": "",
            "birthdate": 32456789170.75,
            "sex": "female",
            "email": "TheSpanishInquisition@gmail.com"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url + "createUser", data=json.dumps(payload), headers=headers)
        print(response.content.decode())
        assert response.status_code == 400
        assert response.content.decode() == "Invalid Name"

    def test_invalid_name_2(self):
        payload = {
            "uuid": "d6c7a91d-a48d-4d0c-8d5a-5119898f9de3",
            "name": 3,
            "birthdate": 127649852.0,
            "sex": "female",
            "email": "TheSpanishInquisition@gmail.com"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url + "createUser", data=json.dumps(payload), headers=headers)
        print(response.content.decode())
        assert response.status_code == 400
        assert response.content.decode() == "Invalid Name"
    
    def test_invalid_birthdate_1(self):
        payload = {
            "uuid": "c03fe061-fd29-4519-a57f-d9bd24f1c44c",
            "name": "Nick Huang",
            "birthdate": "This is a string",
            "sex": "male",
            "email": "xX__Nick__Huang__Xx@gmail.com"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url + "createUser", data=json.dumps(payload), headers=headers)
        print(response.content.decode())
        assert response.status_code == 400
        assert response.content.decode() == "Invalid Birthdate"
    
    def test_invalid_birthdate_2(self):
        payload = {
            "uuid": "35d2ae60-8f62-4f39-8b35-085f619720e2",
            "name": "Adeet Parikh",
            "birthdate": "",
            "sex": "male",
            "email": "cool_email@gmail.com"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url + "createUser", data=json.dumps(payload), headers=headers)
        print(response.content.decode())
        assert response.status_code == 400
        assert response.content.decode() == "Invalid Birthdate"

    def test_invalid_sex_1(self):
        payload = {
            "uuid": "310c2671-c1ef-4b4a-8412-0dfab51d539a",
            "name": "Ron Weasley",
            "birthdate": 12196871.0,
            "sex": "apache attack helicopter",
            "email": "petrat@gmail.com"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url + "createUser", data=json.dumps(payload), headers=headers)
        print(response.content.decode())
        assert response.status_code == 400
        assert response.content.decode() == "Invalid Sex"

    def test_invalid_sex_2(self):
        payload = {
            "uuid": "3a2d3956-8d04-4991-94a4-dc6db605dc48",
            "name": "Hermione Granger",
            "birthdate": 10984739268.5,
            "sex": "",
            "email": "petcat@gmail.com"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url + "createUser", data=json.dumps(payload), headers=headers)
        print(response.content.decode())
        assert response.status_code == 400
        assert response.content.decode() == "Invalid Sex"

    def test_invalid_sex_3(self):
        payload = {
            "uuid": "83c96c34-e30c-4c6d-b944-e9d3e5aef416",
            "name": "Arthur Weasley",
            "birthdate": -1928473.1,
            "sex": 15.2,
            "email": "muggle@gmail.com"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url + "createUser", data=json.dumps(payload), headers=headers)
        print(response.content.decode())
        assert response.status_code == 400
        assert response.content.decode() == "Invalid Sex"