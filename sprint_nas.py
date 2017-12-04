#Superintendent
    #Functions:
        #Asks users whether they are experienced programmers (Lambda) or average users (else) and adjusts interface accordingly
        #Automatically passes files from computer to NAS server and v.v.
        #Lets users browse/retrieve files by name, filetype, and tags
        #Notifies users by email when specific files are downloaded or uploaded
    #Question: user-friendly text interface, or integrate arguments into commands e.g. store(name,type,tagpri,tagsec,tagter)

import sys
import time
import random
        
estand = '[o o]'
echeer = '[^ ^]'
efault = '[> <]'
ewarn = '[O O]'
equery = '[< <]'
emisc = ['[< >]','[U U]','[X X]','[+ +]','[~ ~]','[` `]','[C C]']

prompt = '      >>> '
filename = ''
filetype = ''
foldername = ''
tagpri = ''
tagsec = ''
tagter = ''
placeholder = '[PLACEHOLDER]'
initcommand = ''

def userstore():
    while True:
        print('\n' + equery + ' Is this your first time storing a file using Superintendent? ')
        firstquery = input(prompt)
        if firstquery == 'yes':
                cont = ''
                i = 0
                instrset = ['Please enter any input to proceed to each new instruction; please enter "end" instead if at any point you wish to leave the instruction phase','Superintendent will ask you to choose a location to store your files; this can be done one-at-a-time, in a batch, or across a range of files and locations','Superintendent will also ask you to name each file for future retrieval','To ensure that you are retrieving the right file and not a duplicate, Superintendent will then ask you to confirm the filetype','These steps are mandatory to ensure that Superintendent will correctly store, retrieve, and transfer files as needed','Lastly, you can choose to add three keyword tags to your file','Tagging is not required but can help you narrow down the Library quickly if you forget the name of a specific file','It is also handy if you want to browse similar files with the same tag']
                while cont != 'end' and i < 8:
                    print(estand + ' ' + instrset[i])
                    i = i + 1
                    time.sleep(2)
                    print(equery + '      Continue? ')
                    cont = input('      ' + prompt)
                print(echeer + ' Instruction Phase COMPLETE')
        else:
            print(echeer + ' Welcome back!')
        time.sleep(1)
        print('\n' + ewarn + ' Proceeding to file storage...')
        #foldername = input(estand + ' Please specify a location for this file: ')
        while True:
            print(estand + ' Please specify a filename:')
            filename = input(prompt)
            print(ewarn + ' Please confirm the filename:')
            nameconf = input(prompt)
            if filename != nameconf:
                print(efault + ' The filenames do not match!')
                time.sleep(1)
                print(equery + ' Proceed anyway? ')
                proceed = input(prompt)
                if proceed == 'yes':
                    break
                else:
                    continue
            else:
                break
            
        while True:
            print(estand + ' Please specify a filetype (.txt, .py, .gif ...):')
            filetype = input(prompt + '.')
            print(ewarn + ' Please confirm the filetype:')
            typeconf = input(prompt + '.')
            if filetype != typeconf:
                print(efault + ' The filetypes do not match!')
                time.sleep(1)
                print(equery + ' Proceed anyway? ')
                proceed = input(prompt)
                if proceed == 'yes':
                    break
                else:
                    continue
            else:
                break

        while True:
            print(equery + ' Would you like to add keyword tags to this file? ')
            tagquery = input(prompt)
            if tagquery == 'yes':
                time.sleep(1)
                print(ewarn + ' Please specify tags for this file (funny, wallpaper, chill...):')
                tagpri = input('     ' + emisc[random.randint(0, 6)] + ' First tag: ')
                tagsec = input('     ' + emisc[random.randint(0, 6)] + ' Second tag: ')
                tagter = input('     ' + emisc[random.randint(0, 6)] + ' Final tag: ')
                print(ewarn + ' This file is now tagged as ' + tagpri + ', ' + tagsec + ', ' + tagter)
                time.sleep(2)
                print(equery + ' Are you satisfied with these tags? ')
                tagconf = input(prompt)
                if tagconf == 'yes':
                    break
                else:
                    continue
            else:
                break

        print(ewarn + ' ' + nameconf + '.' + typeconf + ' is ready for storage')
        time.sleep(2)
        print(equery + 'Proceed with storage? ')
        finalconf = input(prompt)
        if finalconf == 'yes':
            print(echeer + ' ' + nameconf + '.' + typeconf + ' is now stored in ' + placeholder + '. Thank you for using Superintendent!')
            break
        else:
            continue

def userinit():
    print('Superintendent SPRINT File Assistant v0.1.2 "Virgil"')
    print('     Credit: R3Ddude 2017')
    print('\n' + echeer + ' Connected to device "' + placeholder + '"\n')
    while True:
        print('Enter any input to continue')
        usertype = input(prompt)
        if usertype == 'Lambda' or usertype == 'lambda':
            usertype = 'Lambda'
            print('Welcome, ' + usertype + '!\n')
            lambdamenu()
        else:
            print('Welcome, user!\n')
            usermenu()

def lambdamenu()
	while True:
		print(estand + ' Awaiting instruction')
		initcommand = input(prompt)
		if initcommand == 'exit':
			print(echeer + ' Goodbye')
			sys.exit()
		elif initcommand == 'help'
			print(estand + ' command(arg)')
			print(emisc[random.randint(0, 6)] + '     
			print(emisc[random.randint(0, 6)] + '     
			print(emisc[random.randint(0, 6)] + '     

def usermenu()
	while True:
        print(estand + ' Awaiting instruction')
        initcommand = input(prompt)
        if initcommand == 'exit':
            print(echeer + ' Goodbye')
            sys.exit()
		elif initcommand == 'help':
        elif initcommand == 'store':
            print(ewarn + ' Proceeding to storage module')
			
        else:
            continue

userinit()

