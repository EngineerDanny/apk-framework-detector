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
    with zipfile.ZipFile(app_name, 'r') as zipObject:
        file_names = zipObject.namelist()
        # Uncomment the line below to extract the list of files in the apk to the output directory
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
