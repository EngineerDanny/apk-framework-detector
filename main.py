"""
APK FRAMEWORK DETECTOR
Author  :   Daniel Agyapong
Website :   https://engineerdanny.me
Date    :   February, 2022
"""

import sys
import zipfile


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

input_path = 'input/'
output_path = 'output'


def main():
    app_name = get_app_name()
    detected_frameworks = []

    try:
        with zipfile.ZipFile(app_name, 'r') as zipObject:
            file_names = zipObject.namelist()
            # Uncomment the line below to extract the list of files in the apk to the output directory
            # zipObject.extractall('output')

            for tech in tech_list:
                if any(any(file_name.find(directory) != -1 for file_name in file_names)
                       for directory in tech.directories):
                    detected_frameworks.append(tech.framework)

            if not detected_frameworks:
                detected_frameworks.append(FrameWork.NATIVE)
    except FileNotFoundError:
        print(f"File {app_name} not found.")
        return
    except zipfile.BadZipFile:
        print(f"{app_name} is not a valid APK or zip file.")
        return
        
    if len(detected_frameworks) == 1:
        print(f"App was written in {detected_frameworks[0]}")
    else:
        print("App uses multiple frameworks:")
        for framework in detected_frameworks:
            print(f"- {framework}")


def get_app_name():
    args = sys.argv
    if len(args) > 1:
        return input_path + args[1]
    else:
        print("Please provide an app name as an argument." +
              "\nEg: python main.py app_name.apk")
        # exit the program
        exit()


# Run the main function
main()
