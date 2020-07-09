from httprequest.unlock import Http

class Unlock:

    def __init__(self):
        return

    def send(self, url, clientCredentialFingerPrint, userID, data):
        http = Http()
        
        headers = {
            "Content-Type": "application/json",
            "finger_print": clientCredentialFingerPrint,
            "user_id": userID
        }

        print("headers:", headers)
        print("data:", data)

        response = http.post(url, headers, data)

        res = response.json()
        return