name = request.POST.get("name", None)
surname = request.POST.get("surname",None)
gmail = request.POST.get("gmail", None)
phone_number = request.POST.get("phone_number", None)
message = request.POST.get("message", None)

contacts = Contact()

contacts.name = name
contacts.surname = surname
contacts.gmail = gmail
contacts.phone_number = phone_number
contacts.message = message
contacts.save()
print("saqladi")


return redirect(reverse("bosh-sahifa"))
