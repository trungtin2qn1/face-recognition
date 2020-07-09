from httprequest.unlock import Http
from db.db import DbConnector

class ClientCredential:

    def __init__(self):
        return

    # def getFromServer(self, url, token):
    #     http = Http()
        
    #     headers = {
    #         "Authorization": "Tin " + token
    #     }
    #     response = http.get(url, headers)
        
    #     fingerPrint = response.json()['finger_print']
    #     self.insertToDB('client-credential', fingerPrint)
    #     self.getByKey('client-credential')
    #     return

    def save(self, fingerPrint):
        http = Http()
        
        headers = {
            "Authorization": "Tin " + token
        }
        response = http.get(url, headers)
        
        fp = response.json()['finger_print']
        self.insertToDB('client-credential', fp)
        self.getByKey('client-credential')
        return
    
    def insertToDB(slef, key, fingerPrint):
        dbConnector = DbConnector()
        dbConnector.getInstance().put(key, fingerPrint)
        return

    def getByKey(self, key):
        dbConnector = DbConnector()
        val = dbConnector.getInstance().get(key)
        # clientCredential = ClientCredential()
        # return user.decode(val)
        print(val)
        return