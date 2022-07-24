package main

import (
	"fmt"
)

const (

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
fmt.Println("Write action (buy, fill, take): ")
fmt.Scan(&action)
if action == "buy" {
	fmt.Println("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ")
	fmt.Scan(&drink)
	switch drink { // not sure if this is correct usage
	case "1":
		espresso()
	case "2":
		latte()
	case "3":
		cappuccino()
	}
	fmt.Println("The coffee machine has:")
	fmt.Println(water, "ml of water")
	fmt.Println(milk, "ml of milk")
	fmt.Println(beans, "g of coffee beans")
	fmt.Println(cups, "disposable cups")
	fmt.Print("$", money, " of money")
} else if action == "fill" {
	fill()
	fmt.Println("The coffee machine has:")
	fmt.Println(water, "ml of water")
	fmt.Println(milk, "ml of milk")
	fmt.Println(beans, "g of coffee beans")
	fmt.Println(cups, "disposable cups")
	fmt.Print("$", money, " of money")
} else if action == "take" {
	take()
	fmt.Println("The coffee machine has:")
	fmt.Println(water, "ml of water")
	fmt.Println(milk, "ml of milk")
	fmt.Println(beans, "g of coffee beans")
	fmt.Println(cups, "disposable cups")
	fmt.Print("$", money, " of money")
} else {

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

func espresso() {
water = water - 250
beans = beans - 16
cups = cups - 1
money = money + 4
}

func latte() {
water = water - 350
milk = milk - 75
beans = beans - 20
cups = cups - 1
money = money + 7
}

func cappuccino() {
water = water - 200
milk = milk - 100
beans = beans - 12
cups = cups - 1
money = money + 6
}