def read_bytes(name: str) -> bytes:
    try:
        with open(name, 'rb') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        print("The file was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {str(e)}.")


def write_bytes(name: str, text: bytes) -> None:
    try:
        with open(name, "wb") as file:
            file.write(text)
        print(f"Congratulations! The data is written to a file : {name}.")
    except FileNotFoundError:
         print("The file was not found.")
    except Exception as e:
         print(f"An error occurred while reading the file: {str(e)}.")
