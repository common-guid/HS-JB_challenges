/*
Write a program that continuously makes coffee for everyone until the shutdown command is provided. 
Introduce two new options: remaining and exit.

Do not forget that you can overstretch your supplies while making coffee. 
If the coffee machine doesn't have enough resources to make coffee, the program should output a message saying that it can't 
make it anymore and state what is missing.

And the last improvement to the program at this step — if users enter buy to buy a cup of coffee but change their mind afterward, 
allow them to input back to return to the main menu.

For a start, the coffee machine has $550, 400 ml of water, 540 ml of milk, 120 g of coffee beans, and 9 disposable cups.
*/

package main

import (
	"fmt"
)

var (
	water int = 400
	milk int  = 540
	beans int = 120
	cups int = 9
	money int = 550
	action, drink string
	fill_water, fill_milk, fill_beans, fill_cups int
)

func main() {
	for {
		fmt.Println("Write action (buy, fill, take, remaining, exit): ")
		fmt.Scan(&action)
		if action == "buy" {
			fmt.Println("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
			fmt.Scan(&drink)
			switch drink { 
			case "1":
				espresso()
			case "2":
				latte()
			case "3":
				cappuccino()
			case "back":
				continue
			}
		} else if action == "fill" {
			fill()
		} else if action == "take" {
			take()
		} else if action == "remaining" {
			print_all()
		} else {
			break
			}
		}
	}
func fill() {
	fmt.Println("Write how many ml of water you want to add: ")
	fmt.Scan(&fill_water)
	fmt.Println("Write how many ml of milk you want to add: ")
	fmt.Scan(&fill_milk)
	fmt.Println("Write how many grams of coffee beans you want to add: ")
	fmt.Scan(&fill_beans)
	fmt.Println("Write how many disposable cups of coffee you want to add: ")
	fmt.Scan(&fill_cups)
	water = water + fill_water
	milk = milk + fill_milk
	beans = beans + fill_beans
	cups = cups + fill_cups
	}	

func take() {
	fmt.Print("I gave you $",money, "\n")
	fmt.Println(" ")
	money = money - money
}

func print_all() {
	fmt.Println("The coffee machine has:")
	fmt.Println(water, "ml of water")
	fmt.Println(milk, "ml of milk")
	fmt.Println(beans, "g of coffee beans")
	fmt.Println(cups, "disposable cups")
	fmt.Print("$", money, " of money\n")
}

func espresso() {
	water = water - 250
	beans = beans - 16
	cups = cups - 1
	money = money + 4
	if water < 1 || beans < 1 || cups < 1 {
		switch {
		case water < 1:
			fmt.Println("Sorry, not enough water!")
		case beans < 1:
			fmt.Println("Sorry, not enough coffee beans!")
		case cups < 1:
			fmt.Println("Sorry, not enough cups!")
		}
		water = water + 250
		beans = beans + 16
		cups = cups + 1
		money = money - 4
	} else {
		fmt.Println("I have enough resources, making you a coffee!")
	}
}

func latte() {
	water = water - 350
	milk = milk - 75
	beans = beans - 20
	cups = cups - 1
	money = money + 7
	if water < 1 || milk < 1 || beans < 1 || cups < 1 {
		switch {
		case water < 1:
			fmt.Println("Sorry, not enough water!")
		case milk < 1:
			fmt.Println("Sorry, not enough milk!")
		case beans < 1:
			fmt.Println("Sorry, not enough coffee beans!")
		case cups < 1:
			fmt.Println("Sorry, not enough cups!")
		}
		water = water + 350
		milk = milk + 75
		beans = beans + 20
		cups = cups + 1
		money = money - 7
	} else {
		fmt.Println("I have enough resources, making you a coffee!")
	}
}

func cappuccino() {
	water = water - 200
	milk = milk - 100
	beans = beans - 12
	cups = cups - 1
	money = money + 6
	if water < 1 || milk < 1 || beans < 1 || cups < 1 {
		switch {
		case water < 1:
			fmt.Println("Sorry, not enough water!")
		case milk < 1:
			fmt.Println("Sorry, not enough milk!")
		case beans < 1:
			fmt.Println("Sorry, not enough coffee beans!")
		case cups < 1:
			fmt.Println("Sorry, not enough cups!")
		}
		water = water + 200
		milk = milk + 100
		beans = beans + 12
		cups = cups + 1
		money = money - 6
	} else {
		fmt.Println("I have enough resources, making you a coffee!")
	}
}