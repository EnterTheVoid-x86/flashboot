# Flashboot, a utility suite to flash images to a Pixel device.
try:
    import wget
    import os
except ImportError:
    print("Installing wget...")
    sys.stdout.flush()
    os.system("py -m pip install wget")
    import wget
print("Notice: Before you run this program, make sure you have drivers installed, along with internet!")
print("Pixel is copyright Google Inc. and is licensed under the terms of the GNU General Public License v3.")
print("Select a device:")
print("0. Pixel 5")
print("1. Pixel 4")
print("2. Pixel 4 XL")
print("3. Pixel 3")
print("4. Pixel 3 XL")
print("5. Pixel 3a XL")
print("6. Pixel 3a")
print("7. Pixel 2")
print("8. Pixel 2 XL")
print("9. Pixel")
print("10. Pixel XL")
line = input("Enter the number of the device you want to flash: ")
if line == "0":
    device = "pixel5"
elif line == "1":
    device = "pixel4"
elif line == "2":
    device = "pixel4xl"
elif line == "3":
    device = "pixel3"
elif line == "4":
    device = "pixel3xl"
elif line == "5":
    device = "pixel3axl"
elif line == "6":
    device = "pixel3a"
elif line == "7":
    device = "pixel2"
elif line == "8":
    device = "pixel2xl"
elif line == "9":
    device = "pixel"
elif line == "10":
    phone = "pixelxl"
else:
    print("Invalid input.")
def main2():
    print("Select a choice:")
    print("1. Install TWRP")
    print("2. Install a zip file")
    print("3. Exit")
    line = input("Enter the number of the choice you want to make: ")
    if line == "1":
        print("Installing TWRP...")
        if device == "pixel5":
            wget.download("https://dl.twrp.me/redfin/twrp-3.6.2_11-0-redfin.img", "twrp.img")
        elif device == "pixel4":
            wget.download("https://dl.twrp.me/flame/twrp-3.6.2_11-0-flame.img", "twrp.img")
        elif device == "pixel4xl":
            wget.download("https://dl.twrp.me/coral/twrp-3.6.2_11-0-coral.img", "twrp.img")
        elif device == "pixel3":
            wget.download("https://dl.twrp.me/blueline/twrp-3.6.2_11-0-blueline.img", "twrp.img")
        elif device == "pixel3xl":
            wget.download("https://dl.twrp.me/crosshatch/twrp-3.6.2_11-0-crosshatch.img", "twrp.img")
        elif device == "pixel3axl":
            wget.download("https://dl.twrp.me/bonito/twrp-3.6.2_11-0-bonito.img", "twrp.img")
        elif device == "pixel3a":
            wget.download("https://dl.twrp.me/sargo/twrp-3.6.2_11-0-sargo.img", "twrp.img")
        elif device == "pixel2":
            wget.download("https://dl.twrp.me/walleye/twrp-3.3.0-0-walleye.img", "twrp.img")
        elif device == "pixel2xl":
            wget.download("https://dl.twrp.me/taimen/twrp-3.6.2_9-0-taimen.img", "twrp.img")
        elif device == "pixel":
            wget.download("https://dl.twrp.me/sailfish/twrp-3.6.2_9-0-sailfish.img", "twrp.img")
        elif device == "pixelxl":
            wget.download("https://dl.twrp.me/marlin/twrp-3.6.2_9-0-marlin.img", "twrp.img")
        os.system("adb reboot bootloader")
        os.system("fastboot flash recovery twrp.img")
        os.system("fastboot reboot")
        print("TWRP installed!")
        main2()
    elif line == "2":
        print("Installing zip file...")
        zipfile = input("Enter the name of the zip file: ")
        os.system("adb reboot recovery")
        print("In recovery, select the 'Apply Update > Install from ADB' option.")
        line2 = input("Enter 'y' to continue: ")
        os.system("adb sideload " + zipfile)
        print("Zip file installed!")
        main2()
    elif line == "3":
        print("Exiting...")
        exit()
main2()
