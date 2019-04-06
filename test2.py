#Sample script server files from outside of the project folder

import os

from flask import Flask
from flask import send_from_directory

#static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static')
static_file_dir = "/Users/SBMaru/Downloads"
app = Flask(__name__)


@app.route('/dir', methods=['GET'])
def serve_dir_directory_index():
    print(static_file_dir)
    return send_from_directory(static_file_dir, 'index.html')


@app.route('/dir/<path:path>', methods=['GET'])
def serve_file_in_dir(path):

    if not os.path.isfile(os.path.join(static_file_dir, path)):
        path = os.path.join(path, 'index.html')

    return send_from_directory(static_file_dir, path)

# Create files in the defined static dictory
@app.route('/create/<file>')
def create(file):
    print("check if file exist in")
    if os.path.isfile(os.path.join(static_file_dir, file)):
        print("Found file : " , file)
        return send_from_directory(static_file_dir, file)
    else:
        print("Not Found creatting file: ", file)
        filepath = os.path.join(static_file_dir, file)
        f = open(filepath,"w+")
        f.write("Creating this file via api")
        f.close()
        return send_from_directory(static_file_dir, file)


# Delete files in defined static directory
@app.route('/delete/<file>')
def delete(file):
    print("check if file exist in")
    if os.path.isfile(os.path.join(static_file_dir, file)):
        print("Found file : " , file , " deleting")
        os.remove( os.path.join(static_file_dir, file))
        return "File Removed "
    else:
        print("Not Found creatting file: ", file)
        return "File Not found"


app.run(host='0.0.0.0',port=8080,debug=True)
