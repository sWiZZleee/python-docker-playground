import os

if __name__ == '__main__':
    # Ask the user for the name of the image they would like to run
    tagName = input('Input the name/tag given to the image you would like to run: ')
    # This isn't the cleanest way to do this but its quick and works for me but I do want to improve on this
    while True:
        # Ask the user whether to run a shell instance or python interpreter
        choice = input(
            'Would you like to connect to a Python or Shell instance inside this image or just run it? [py/sh/run] ')

        if choice == 'py':
            # Run and connect to the image in interactive mode
            os.system('docker run -it --rm ' + tagName)
            break
        elif choice == 'sh':
            os.system('docker run -it --rm ' + tagName + ' /bin/sh')
            break
        elif choice == 'run':
            # Ask the user which ports on the container and local machine they want to use
            # Currently it's localhost:5000/ for a Flask instance but this can be dependent on each users config
            portFrom = input('Input the port you want to map from the container: ')
            portTo = input('Input the port which you want to map it to on your machine: ')
            os.system('docker run --rm -p ' + portTo + ':' + portFrom + ' ' + tagName)
            break
        else:
            print('Please specify whether you would like to connect to an instance inside the container or run it.')
