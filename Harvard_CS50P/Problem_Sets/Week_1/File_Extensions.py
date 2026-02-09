def main():
    file = input("File name: ").lower().strip()

    if file.endswith(".gif"):
        print("image/gif")
    elif file.endswith(".jpg") or file.endswith(".jpeg"):
        print("image/jpeg")
    elif file.endswith(".png"):
        print("image/png")
    elif file.endswith(".pdf"):
        print("application/pdf")
    elif file.endswith(".txt"):
        print("text/plain")
    elif file.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")

main()

print("*" * 50)

# PRO way of doing it with a DICTIONARY!


def second():
    file = input("File name: ").lower().strip()

    # Create a map of extensions to their official types
    types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
    }

    # Check if the file ends with any of our keys
    for extension in types:
        if file.endswith(extension):
            print(types[extension])
            return  # Stop the function once we find a match

    # If the loop finishes without finding anything
    print("application/octet-stream")


second()