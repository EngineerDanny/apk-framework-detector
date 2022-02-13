from zipfile import ZipFile


input_path = 'input/'
output_path = 'output'


def main():
    app_name = "beetv.apk"
    with ZipFile(input_path + app_name, 'r') as zipObject:
        file_names = zipObject.namelist()
        zipObject.extractall('output')

        for file_name in file_names:
            # FLUTTER
            if file_name.find('libflutter.so') != -1:
                zipObject.close()
                return "Flutter"

            # REACT NATIVE
            # check for a .bundle file in the assets folder
            # check for a libreactnativejni.so file in the libs folder
            rn_test_1 = file_name.find('libreactnativejni.so') != -1
            rn_test_2 = file_name.find('assets/index.android.bundle') != -1
            if rn_test_1 or rn_test_2:
                zipObject.close()
                return "React Native"

            # CORDOVA
            # check for a cordova.js, cordova_plugins or index.html file
            # in the assets/www folder
            cordova_test_1 = file_name.find('assets/www/cordova.js') != -1
            cordova_test_2 = file_name.find(
                'assets/www/cordova_plugins.js') != -1
            cordova_test_3 = file_name.find('assets/www/index.html') != -1

            if cordova_test_1 or cordova_test_2 or cordova_test_3:
                zipObject.close()
                return "Cordova"

            # XAMARIN
            # /assemblies/Sikur.Monodroid.dll
            # /assemblies/Sikur.dll
            # /assemblies/Xamarin.Android.Support.v13.dll
            # /assemblies/Xamarin.Android.Support.v4.dll
            # /assemblies/Xamarin.Android.Support.v7.AppCompat.dll
            # /assemblies/Xamarin.Android.Support.v7.CardView.dll
            # /assemblies/Xamarin.Android.Support.v7.RecyclerView.dll
            # /assemblies/Xamarin.Mobile.dll
            # /assemblies/mscorlib.dll
           
            # libmonodroid.so
            # libmonosgen-2.0.so
            xamarin_test_1 = file_name.find(
                'assets/App_Resources/Android/') != -1

        zipObject.close()
        return "Native"


find_framework = main()
print(find_framework)
