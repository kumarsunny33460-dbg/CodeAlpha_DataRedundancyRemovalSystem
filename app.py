from flask import Flask, render_template, request, redirect, flash, send_file
from datetime import datetime
import csv

from database import *
from redundancy import classify_record

app = Flask(__name__)

app.secret_key = "codealpha"

duplicate_counter = 0


@app.route("/")
def home():

    global duplicate_counter

    search = request.args.get("search", "")

    records = get_all_records()

    if search:

        records = [
            r for r in records
            if search.lower() in r.get("name", "").lower()
            or search.lower() in r.get("email", "").lower()
            or search.lower() in r.get("phone", "").lower()
        ]

    total = total_records()

    verified = total

    if total == 0:
        success = "0%"
    else:
        success = "100%"

    return render_template(
        "index.html",
        records=records,
        total=total,
        verified=verified,
        duplicates=duplicate_counter,
        success_rate=success,
        search=search
    )


@app.route("/add", methods=["POST"])
def add():

    global duplicate_counter

    name = request.form["name"]

    email = request.form["email"]

    phone = request.form["phone"]

    duplicate = find_duplicate(email, phone)

    status = classify_record(duplicate)

    if status == "Duplicate":

        duplicate_counter += 1

        flash("Duplicate Record Detected!", "danger")

        return redirect("/")


    record = {

        "name": name,

        "email": email,

        "phone": phone,

        "verified": True,

        "created_at": datetime.now().strftime("%d-%m-%Y %H:%M")

    }


    insert_record(record)

    flash("Record Stored Successfully!", "success")

    return redirect("/")


@app.route("/delete/<id>")
def delete(id):

    delete_record(id)

    flash("Record Deleted Successfully!", "warning")

    return redirect("/")


@app.route("/edit/<id>")
def edit(id):

    record = get_record(id)

    return render_template(
        "edit.html",
        record=record
    )


@app.route("/update/<id>", methods=["POST"])
def update(id):

    data = {

        "name": request.form["name"],

        "email": request.form["email"],

        "phone": request.form["phone"]

    }

    update_record(id, data)

    flash("Record Updated Successfully!", "info")

    return redirect("/")


@app.route("/export")
def export():

    records = get_all_records()

    file_path = "records.csv"


    with open(file_path, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)


        writer.writerow(
            [
                "Name",
                "Email",
                "Phone",
                "Created"
            ]
        )


        for r in records:

            writer.writerow(
                [
                    r.get("name", ""),
                    r.get("email", ""),
                    r.get("phone", ""),
                    r.get("created_at", "")
                ]
            )


    return send_file(
        file_path,
        mimetype="text/csv",
        as_attachment=True,
        download_name="records.csv"
    )


if __name__ == "__main__":

    app.run(debug=True)