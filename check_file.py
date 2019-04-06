# Check for file existence and file_age
# Delete if file is older than ## seconds
import os, time

def file_age(filepath):
    return time.time() - os.path.getmtime(filepath)



file_path = '/Users/SBMaru/Downloads/index.html'
exists = os.path.isfile(file_path)
if exists:
    # Store configuration file values
    print("Found file: ",file_path)
    st = os.stat(file_path)
    print(st.st_mtime)
    ctime = file_age(file_path)
    print("file age: ", ctime)
    if ctime > 40:
        print("delete file")
        os.remove(file_path)
else:
    # Keep presets
    print("No file found")
