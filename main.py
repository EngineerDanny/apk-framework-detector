from zipfile import ZipFile


input_path = 'input/'
output_path = 'output'


def main():
    app_name = "beetv.apk"
    with ZipFile(input_path + app_name, 'r') as zipObject:
        file_names = zipObject.namelist()
        zipObject.extractall('output')

        for file_name in file_names:
            if file_name.find('libflutter.so') != -1:
                zipObject.close()
                return "Flutter"
            
            if file_name.find('libreactnativejni.so') != -1:
                zipObject.close()
                return "React Native"
            
        zipObject.close()
        return "Native"


find_framework = main()
print(find_framework)

