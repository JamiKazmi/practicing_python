commad = ''
started = False

while True:
    commad = input('> ').lower()

    if commad == 'start':
        if started:
            print('Car is already is started!')
        else:
            started = True
            print('Car is started... Ready to go!')

    elif commad == 'stop':
        if not started:
            print('Car is already stoped!')
        else:
            started = False
            print('Car is stoped.!')

    elif commad == 'help':
        print('''
start - to start
stop - to stop
quit - to quit
              ''')

    elif commad == 'quit':
        print('Bye..! See you')
        break

    else:
        print('I don\'t understand you.!')
