"""
APK FRAMEWORK DETECTOR
Author  :   Daniel Agyapong
Contributor:   Swarup Saha
Date    :   2024-12-19
"""

import sys
import zipfile
import os


class FrameWork:
    FLUTTER = "Flutter"
    REACT_NATIVE = "React Native"
    CORDOVA = "Cordova"
    XAMARIN = "Xamarin"
    NATIVE = "Native (Java/Kotlin)"
    UNITY = "Unity"
    UNREAL = "Unreal Engine"
    LIBGDX = "LibGDX"
    EXPO = "Expo"
    KONY = "Kony Visualizer"


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
            "assemblies/Sikur.Monodroid.dll",
            "assemblies/Sikur.dll",
            "assemblies/Xamarin.Mobile.dll",
            "assemblies/mscorlib.dll",
            "libmonodroid.so",
            "libmonosgen-2.0.so",
        ]
    ),
    Technology(
        framework=FrameWork.UNITY,
        directories=[
            "libunity.so",
            "assets/bin/Data/Managed/UnityEngine.dll",
            "assets/bin/Data/Managed/UnityEditor.dll"
        ]
    ),
    Technology(
        framework=FrameWork.UNREAL,
        directories=[
            "libUE4.so",
            "assets/Unreal/UE4Game/Manifest.xml"
        ]
    ),
    Technology(
        framework=FrameWork.LIBGDX,
        directories=[
            "libgdx.so",
            "assets/libgdx/lwjgl.so",
            "assets/libgdx.jar"
        ]
    ),
    Technology(
        framework=FrameWork.EXPO,
        directories=[
            "assets/shell-app.bundle",
            "assets/expo-manifest.json"
        ]
    ),
    Technology(
        framework=FrameWork.KONY,
        directories=[
            "assets/kony.js",
            "assets/konyframework.js",
            "assets/KonyApps/config.json"
        ]
    ),
]

input_path = 'input/'


def main():
    app_name = get_app_name()
    detected_frameworks = []
    
    try:
        with zipfile.ZipFile(app_name, 'r') as zipObject:
            file_names = zipObject.namelist()
            
            for tech in tech_list:
                if any(directory in file_name for directory in tech.directories for file_name in file_names):
                    detected_frameworks.append(tech.framework)
            
            if not detected_frameworks:
                detected_frameworks.append(FrameWork.NATIVE)
    except FileNotFoundError:
        print(f"Error: File {app_name} not found. Ensure the path is correct.")
        sys.exit(1)
    except zipfile.BadZipFile:
        print(f"Error: {app_name} is not a valid APK file.")
        sys.exit(1)
    
    print_detection_results(detected_frameworks)


def get_app_name():
    args = sys.argv
    if len(args) > 1:
        return os.path.join(input_path, args[1])
    else:
        print("Please provide an app name as an argument.\nEg: python main.py app_name.apk")
        sys.exit(1)


def print_detection_results(detected_frameworks):
    if len(detected_frameworks) == 1:
        print(f"App was written in {detected_frameworks[0]}")
    else:
        print("App uses multiple frameworks:")
        for framework in detected_frameworks:
            print(f"- {framework}")


if __name__ == "__main__":
    main()
