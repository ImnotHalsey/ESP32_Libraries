import urequests, uos

def upload_photo(path):
    url = "https://farmrobo.chaithanyasaipo.repl.co/upload_image"
    with open(path, 'rb') as file:
        image_content = file.read()

    content_type = "image/jpeg"
    headers = {'Content-Type': 'multipart/form-data; boundary=my_boundary'}
    data = (b'--my_boundary\r\n' +
            b'Content-Disposition: form-data; name="file"; filename="' + path.encode('utf-8') + b'"\r\n' +
            b'Content-Type: ' + content_type.encode('utf-8') + b'\r\n\r\n' +
            image_content + b'\r\n' + b'--my_boundary--\r\n')

    response = urequests.post(url, data=data, headers=headers)

    if response.status_code == 200:
        print("Image uploaded successfully and Deleted")
        uos.remove(path)
        return True
    else:
        print("Error uploading image. Status code:", response.status_code)