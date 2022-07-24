package main

import (
	"fmt"
	"strconv"
)

const (
	water int = 200
	milk int = 50
	beans int = 15
	cups int = 1
)
var num int

func main() {
	fmt.Println("For "+ strconv.Itoa(num) +" cups of coffee you will need:")
	fmt.Scan(&num)
	amt_water := num * water
	amt_milk := num * milk
	amt_beans := num * beans
	fmt.Println(strconv.Itoa(amt_water) +" ml of water")
	fmt.Println(strconv.Itoa(amt_milk) +" ml of milk")
	fmt.Println(strconv.Itoa(amt_beans) +" g of coffee beans")
}