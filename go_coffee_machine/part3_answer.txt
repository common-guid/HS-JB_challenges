/*
Write a program that does the following:

It requests the amounts of water, milk, and coffee beans available at the moment and then asks for the number of required coffee cups;
If the coffee machine has the supplies to make enough coffee, the program should print the following: Yes, I can make that amount of coffee.
If the coffee machine can make more than that, the program should output Yes, I can make that amount of coffee (and even N more than that), where N is the number of extra cups.
If you're running short, the program should output No, I can make only N cups of coffee.
Like in the previous stage, the coffee machine needs 200 ml of water, 50 ml of milk, and 15 g of coffee beans for one cup.
*/
package main

import (
	"fmt"
)

const (
	eachWater int = 200
	eachMilk int = 50
	eachBeans int = 15
)
var (
	water int
	milk int 
	beans int
	num int
	cups int
	coffees int
)

func main() {
	fmt.Println("Write how many ml of water the coffee machine has:")
	fmt.Scan(&water)
	fmt.Println("Write how many ml of milk the coffee machine has:")
	fmt.Scan(&milk)
	fmt.Println("Write how many grams of coffee beans the coffee machine has:")
	fmt.Scan(&beans)
	fmt.Println("Write how many cups of coffee you will need:")
	fmt.Scan(&num)
	// if req == min(amt) print yes...
	// if req < min(amt) print yes and can make more...
	// if req > min(amt) print can only make...
	cups = int(calc_coffee())
	if num < cups {
		diff := cups - num
		fmt.Println("Yes, I can make that amount of coffee (and even", diff, "more than that)")
	} else if num > cups {
		fmt.Println("No, I can make only", cups, "cups of coffee") 
	} else {
		fmt.Println("Yes, I can make that amount of coffee")
	}
}

func calc_coffee() (coffees int) {
	cupWater := int(water / eachWater)
	cupMilk := int(milk / eachMilk)
	cupBeans := int(beans / eachBeans)
	switch {
	case cupWater <= cupMilk && cupWater <= cupBeans:
		coffees = cupWater
	case cupMilk <= cupWater && cupMilk <= cupBeans:
		coffees = cupMilk
	case cupBeans <= cupWater && cupBeans <= cupMilk:
		coffees = cupBeans
	}
	return
	}