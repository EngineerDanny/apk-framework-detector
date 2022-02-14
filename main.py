from zipfile import ZipFile


input_path = 'input/'
output_path = 'output'


class FrameWork:
    FLUTTER = "Flutter"
    REACT_NATIVE = "React Native"
    CORDOVA = "Cordova"
    XAMARIN = "Xamarin"
    NATIVE = "Native (Java/Kotlin) "


class Technology:
    def __init__(self, framework, directories):
        self.framework = framework
        self.directories = directories
    pass


tech_list = [
    Technology(
        framework=FrameWork.FLUTTER,
        directories=[
            "libflutter.so"
        ]
    ),
    Technology(
        framework=FrameWork.REACT_NATIVE,
        directories=[
            "libreactnativejni.so",
            "assets/index.android.bundle",
        ]
    ),
    Technology(
        framework=FrameWork.CORDOVA,
        directories=[
            "assets/www/index.html",
            "assets/www/cordova.js",
            "assets/www/cordova_plugins.js"
        ]
    ),
    Technology(
        framework=FrameWork.XAMARIN,
        directories=[
            "/assemblies/Sikur.Monodroid.dll",
            "/assemblies/Sikur.dll",
            "/assemblies/Xamarin.Mobile.dll",
            "/assemblies/mscorlib.dll",
            "libmonodroid.so",
            "libmonosgen-2.0.so",
        ]
    ),
]


def main():
    app_name = "fh.apk"
    with ZipFile(input_path + app_name, 'r') as zipObject:
        file_names = zipObject.namelist()
        # Uncomment the line below to extract the list of files in the apk
        # zipObject.extractall('output')

        for file_name in file_names:
            # loop through tech_list and check if file_name is in any of the directories
            for tech in tech_list:
                for directory in tech.directories:
                    if file_name.find(directory) != -1:
                        zipObject.close()
                        print(f"App was written in {tech.framework}")
                        return
                else:
                    continue

        # if no framework is found, return Native
        zipObject.close()
        print(f"App was written in {FrameWork.NATIVE}")


# Run the main function
main()
