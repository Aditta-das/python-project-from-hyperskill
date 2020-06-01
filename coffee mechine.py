money = 550
water = 400 
milk = 540
beans = 120
cups = 9

def ResourceError():
	pass

def print_state():
    
    print('The coffee machine has:')
    print(water, 'of water')
    print(milk, 'of milk')
    print(beans, 'of coffee beans')
    print(cups, 'of disposable cups')
    print(money, 'of money')
    

def select_action():
    return input('Write action (buy, fill, take, remaining, exit):\n')

    
def select_flavor() -> int:
    print()
    response = input('What do you want to buy?'
                     ' 1 - espresso,'
                     ' 2 - latte,'
                     ' 3 - cappuccino,'
                     ' back - to main menu: ')

    if response == 'back':
        return 0
    return int(response)
    
def is_need(need_water=0, need_milk=0, need_beans=0):    
    if water < need_water:
        print('Sorry, not enough water!\n')
        raise ResourceError()
    elif milk < need_milk:
        print('Sorry, not enough milk!\n')
        raise ResourceError()
    elif beans < need_beans:
        print('Sorry, not enough beans!\n')
        raise ResourceError()
    elif cups < 1:
        print('Sorry, not enough cups!\n')
        raise ResourceError()
    print('I have enough resources, making you a coffee!\n')


def buy():
    global money, water, milk, beans, cups
    
    flavour = select_flavor()
    

    try:
        if flavour == 1:  # esparsso
            is_need(need_water=250, need_beans=16)
            
            money += 4
            water -= 250
            beans -= 16
            cups -= 1 
        elif flavour == 2:
            is_need(need_water=350, need_beans=20, need_milk=75)
            
            money += 7
            water -= 350
            milk -= 75
            beans -= 20
            cups -= 1
        elif flavour == 3:
            is_need(need_water=200, need_beans=12, need_milk=100)
            
            money += 6
            water -= 200
            milk -= 100
            beans -= 12
            cups -= 1
    
        else:
            raise ValueError('Unknown flavour', flavour)

    except:
        pass
    
    
def fill():
    global water, milk, beans, cups
    print()
    water += int(input('Write how many ml of water do you want to add:\n'))
    milk += int(input('Write how many ml of milk do you want to add:\n'))
    beans += int(input('Write how many grams of coffee beans do you want to add:\n'))
    cups += int(input('Write how many disposable cups of coffee do you want to add:\n'))
    print()
    
    
def take():
    global money
    print()
    print('I gave you',money)
    print()
    money = 0

def exit_mac():
	exit()

    
def main():
    while True:
        action = select_action()
        if action == "buy":
            buy()
        elif action == "fill":
            fill()
        elif action == "take":
            take()
        elif action == "remaining":
            print_state()
        elif action == "exit":
        	exit_mac()
        else:
            raise ValueError(action)
            

if __name__ == '__main__':
    main()
