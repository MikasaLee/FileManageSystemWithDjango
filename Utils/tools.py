import os
def save_file(content,save_path):
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    path = os.path.join(save_path)
    if not os.path.exists(path):
        os.mkdir(path)

    _, ext = os.path.splitext(str(content))
    filepath = os.path.join(path, _ + ext)

    destination = open(filepath, 'wb+')
    for chunk in content.chunks():
        destination.write(chunk)
    destination.close()
