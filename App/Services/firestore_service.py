import firebase_admin

from firebase_admin import credentials
from firebase_admin import firestore

class FirestoreService:
    def __init__(self):
        self.cred = credentials.Certificate('/Users/Luna/Documents/Rexmoon/Python/Moon-Service-/App/Keys/service_account_key.json')
        firebase_admin.initialize_app(self.cred)
        self.data_base = firestore.client()
        self.bikes_collection = 'bikes'

    def create_document(self,
                        document,
                        data):
        doc = self.data_base.collection(self.bikes_collection).document(document)
        doc.set(data)
        print('Sent: ', data)

    def deleteDocument(self, 
                       document):
        self.data_base.collection(self.bikes_collection).document(document).delete()
        print('Delete document: ', document)

    def readDocument(self, 
                     document):
        doc = self.data_base.collection(self.bikes_collection).document(document).get()
        print('Read data: ', doc._data)
        return doc