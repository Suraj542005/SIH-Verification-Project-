import pymongo


def store_data(name, email, doc_type, pdf):
    """ This function Stores the Data in Database """
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client['SIH']
    collection = db['Verification_data']

    with open(pdf, "rb") as file:
        pdf_data = file.read()

    data = {
        'name': name,
        'email': email,
        'doc_type': doc_type,
        'pdf': pdf_data
    }

    collection.insert_one(data)


def find_data(email):
    """ This function use Email to find the Data """
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client['SIH']
    collection = db['Verification_data']

    # Code to Retrieve PDF files.....
    query = {'email': email}
    stored_data = collection.find_one(query)

    if stored_data:
        pdf_data = stored_data["pdf"]
        path = "Retrieved_folder/"+email+"_retrieved_pdf.pdf"
        with open(path, "wb") as file:
            file.write(pdf_data)
        print(f"PDF file has been retrieved and saved as '{path}'")
        print(f"User Name: {stored_data['name']}")
        print(f"Email: {stored_data['email']}")
        print(f"Document Type: {stored_data['doc_type']}")
        # print(f"PDF File saved at: {stored_data['pdf']}")
    else:
        print("PDF file not found in the database.")
    # End.....


# find_data("suraj@gmail.com")

# if __name__ == "__main__":
#     # Code to Connect Mongodb with Python
#     print("Connected to PyMongo")
#     client = pymongo.MongoClient("mongodb://localhost:27017")
#     print(client)
#     db = client['SIH']
#     collection = db['Verification_data']
#     # End.....
#
#     # Insert Data into Mongodb.....
#     # To insert one Data
#     data = {'name': "Suraj", 'marks': 50}
#     collection.insert_one(data)
#
#     # To insert multiple data
#     insertThese = [
#         {'name': "Ankit", 'marks': 95},
#         {'name': "Prinkesh", 'marks': 100}
#     ]
#     collection.insert_many(insertThese)
#
#     # To find the data
#     one = collection.find_one()  # It will give one random data
#     one = collection.find_one({'name': "Suraj"})  # It will give particular data
#     print(one)
#     # End.....
#
#     # Code to Store PDF files.....
#     # Read the PDF file
#     pdf_path = "PDFs/AI-ML Healthcare Hackathon[1].pdf"
#     with open(pdf_path, "rb") as file:
#         pdf_data = file.read()
#
#     # Store the PDF in MongoDB
#     pdf_document = {
#         "filename": "AI/ML Pdf",
#         "data": pdf_data
#     }
#     collection.insert_one(pdf_document)
#     # End.....
#
#     # Code to Retrieve PDF files.....
#     query = {"filename": "AI/ML Pdf"}
#     stored_pdf = collection.find_one(query)
#
#     if stored_pdf:
#         pdf_data = stored_pdf["data"]
#         with open("retrieved_pdf_file.pdf", "wb") as file:
#             file.write(pdf_data)
#         print("PDF file has been retrieved and saved as 'retrieved_pdf_file.pdf'")
#     else:
#         print("PDF file not found in the database.")
#     # End.....
#
