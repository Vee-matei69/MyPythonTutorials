from time import sleep

#enter kilometre
kilometre_to_cover = int (input('enter kilometre to be covered: '))
kilometres_covered = 0

#loop
while True:
    kilometres_covered = kilometres_covered + 1
    print('You have covered ',kilometres_covered,'kilometres. ')
    sleep(0.1)

#comparing kilometre_to_coverthe inputs
    if kilometres_covered == kilometre_to_cover/4:
        print('Your are quarter the journey mate. ') 
    if kilometres_covered == kilometre_to_cover/2:
        print('Your are half the journey mate. ')    
    if kilometres_covered == kilometre_to_cover*0.75:
        print('Your are three quarter of the journey mate. ')   
    if kilometre_to_cover == kilometres_covered:
        print('Your journey is over') 
        break

   

