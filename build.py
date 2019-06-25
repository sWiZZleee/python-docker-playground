import os

if __name__ == '__main__':
    # Ask for the name the user would like to give the image
    tagName = input('Input the tag you would like to give the image:')
    # Build the image
    os.system('docker build -t ' + tagName + ' .')