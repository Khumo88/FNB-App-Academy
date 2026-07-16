contacts = {
    "Khumo": "0821112222",
    "Neo": "0833334444",
    "Ayanda": "0815556666"
}

name = input("Enter your friend's name: ")

if name in contacts:
    print("Found!", name + "'s number is", contacts[name])
else:
    print("Contact not found.")