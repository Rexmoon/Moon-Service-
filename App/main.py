from Services.firestore_service import FirestoreService

FirestoreService().readDocument('list')
FirestoreService().create_document(document='R3 Yamaha', data={'id':1, 'name':'My bike'})
FirestoreService().deleteDocument('R3 Yamaha')
