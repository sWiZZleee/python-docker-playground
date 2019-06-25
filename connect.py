import os

if __name__ == '__main__':
    # Ask the user for the name of the image they would like to connect to\
    tagName = input('Input the name/tag given to the image you would like to connect to: ')
    # This isn't the cleanest way to do this but its quick and works for me but I do want to improve on this
    while True:
        # Ask the user whether to run a shell instance or python interpreter
        choice = input('Would you like to connect to a Python or Shell instance inside this image? [py/sh] ')
        
        if choice =='py':
            # Run and connect to the image in interactive mode
            os.system('docker run -it --rm ' + tagName)
            break
        elif choice =='sh':
            os.system('docker run -it --rm '+ tagName + ' /bin/sh')
            break
        else:
            print('Please specify whether you would like a shell instance or python interpreter when connecting to this image.')