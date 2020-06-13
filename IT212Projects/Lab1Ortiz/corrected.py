#Script to correct errors for Lab 1.
#Convert from meters to feet and inches.
#The program should repeatedly input a length in meters
#and then print that length in feet and inches.

more = input('Do you wish to input another length in meters? ').upper( )
while more[0] == 'Y':    
    meter = float(input('Enter length in meters: '))
    f = meter * 3.28084
    feet = int(f)
    inches = round(int(12.0 * (f - feet)))
    print ('The length is ')
    if feet == 1 :
        print (str(feet) + ' foot ')
    else:
        print (str(feet) + ' feet ')

    if inches == 1:
        print(str(inches) + ' inch.')
    elif (inches > 1):
        print(str(inches) + ' inches.')
    else:
        print()

    more = input('Do you wish to input another length in meters: ').upper( )
