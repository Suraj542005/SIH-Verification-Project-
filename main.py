import time
from verification import start_verify
from flask import Flask, render_template, request
import database

app = Flask(__name__)

# Define the upload folder
app.config['UPLOAD_FOLDER'] = 'Uploaded_folder/'


@app.route('/')
def home():
    return render_template("homepage.html")


@app.route('/signup.html')
def signup():
    return render_template("signup.html")


@app.route('/Aadharcard.html', methods=["GET", "POST"])
def verification():
    if request.method == "POST":
        """Add Data to DataBase"""
        user_name = request.form.get("aadhaarName")
        mobile_num = request.form.get("aadhaarMobile")
        aadhar_num = request.form.get("aadhaarNumber")
        pdf_file = request.files.get("aadhaarCardPhoto")

        # email = request.form.get("email")
        # doc_type = request.form.get("docType")
        # add_num = "7164 4778 7575"
        # pan_number = ""

        if pdf_file:
            # Save the PDF file to the server
            pdf_filename = pdf_file.filename
            pdf_path = app.config['UPLOAD_FOLDER'] + pdf_filename
            pdf_file.save(pdf_path)

            print(f"Full Name: {user_name}")
            print(f"Mobile Number: {mobile_num}")
            print(f"Aadhar Number: {aadhar_num}")
            # print(f"Email: {email}")
            # print(f"Document Type: {doc_type}")
            # print(f"PDF File saved at: {pdf_path}")

            # Storing Data in Database
            # database.store_data(
            #     user_name,
            #     email,
            #     doc_type,
            #     pdf_path
            # )
            # pdf = "C:\\Users\\Suraj\\PycharmProjects\\SIH_Final\\Uploaded_folder\\Suraj_AdharCard( Voter ID).pdf"
            return_data = start_verify(pdf_path)

            # if add_num == return_data:
            #     print("Verified")
            # if pan_number == return_data:
            #     print("Pan card Verified.....")

            if aadhar_num == return_data:
                print("Verified")
            # To add Delay.....

            time.sleep(2)

            return render_template("verified.html")

    return render_template("Aadharcard.html")


@app.route('/Aadharcard.html')
def aadhar():
    return render_template("Aadharcard.html")


@app.route('/pan.html')
def pan():
    return render_template("pan.html")


@app.route('/Marksheet.html')
def marksheet():
    return render_template("Marksheet.html")


app.run(debug=True)
