import os
import zipfile

def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file),
                       os.path.relpath(os.path.join(root, file),
                                       os.path.join(path, '..')))

if __name__ == '__main__':
    project_folder = 'D:/MS IT.M/Fall24 - Sem 4/MIS 6382 OOP Python/Python_IDEs/hail_damage_repair'  # Replace with your project folder name
    zipf = zipfile.ZipFile('hdr.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir(project_folder, zipf)
    zipf.close()
    print(f"{project_folder} has been zipped to your_project.zip")