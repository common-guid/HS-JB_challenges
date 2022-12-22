/*
Read two positive integer numbers that represent the number of rows and seats in each row and print the seating arrangement like in the first stage. Then, read two integer numbers from the input: a row number and a seat number in that row. These numbers represent the coordinates of the seat according to which the program should print the ticket price. The ticket price is determined by the same rules as the previous stage:

    If the total number of seats in the screen room is not more than 60, then the price of each ticket is 10 dollars.
    In a larger room, the tickets are 10 dollars for the front half of the rows and 8 dollars for the back half. Please note that the number of rows can be odd, for example, 9 rows. In this case, the first half is the first 4 rows, and the second half is the rest 5 rows.

After that, the program should print out all the seats in the screen room as shown in the example and mark the chosen seat by the B symbol. Finally, it should print the ticket price and stop. Note that in this project, the number of rows and seats won't be greater than 9.
 */

package cinema

import kotlin.math.round
import kotlin.text.Typography.half

fun main() {
    println("Enter the number of rows:")
    val n_rows = readln().toInt()
    println("Enter the number of seats in each row")
    val n_seats = readln().toInt()
    val total = n_rows * n_seats
    grid(n_seats, n_rows)
    print("\n")
    println("\nEnter a row number:")
    var sel_row = readln().toInt()
    println("Enter a seat number in that row:")
    var sel_seat = readln().toInt()
    if (total < 61) {
        var price = 10
        println("\nTicket price: $"+price)
    } else {
        var front_half = (n_rows / 2).toInt()
        var back_half = (n_rows / 2).toInt() + 1
        if (sel_row > front_half) {
            var price = 8
            println("\nTicket price: $"+price)
        } else {
            var price = 10
            println("\nTicket price: $"+price)
        }
    }
    seat_select(n_seats, n_rows, sel_row, sel_seat)
}

/*
    }
    if (total < 61) {
        val ticket = 10
        println("Total income:")
        print("$")
        println(total * ticket)

    } else {
        if (n_rows % 2 == 0) {
            val half_row = n_rows / 2
            val seats = half_row * n_seats
            println("Total income:")
            print("$")
            println(seats*8 + seats *10)
        } else {
            val front = (n_rows / 2).toInt()
            val back = (n_rows / 2).toInt() + 1
            val front_total = (front*n_seats) * 10
            val back_total = (back*n_seats) * 8
            println("Total income:")
            print("$")
            println(front_total + back_total)

        }
    }
}
*/

fun grid(n_seats: Int, n_rows:Int){
    var r = 1
    var i = 1
    println("\nCinema:")
    print(" ")
    do {
        print(" $i")
        i = i + 1
            } while (i < n_seats+1)

    repeat(n_rows){
        print("\n$r")
        r++
        repeat(n_seats){
            print(" S")
        }
    }
}

fun seat_select(n_seats: Int, n_rows:Int, sel_row: Int, sel_seat: Int) {
    var row_num = 1
    var i = 1
    var hloc = 1
    // print header row seat nums
    println("\nCinema:")
    print(" ")
    do {
        print(" $i")
        i = i + 1
    } while (i < n_seats+1)

    for (place in 1..n_rows) {

        if (hloc < (n_seats + 1) && row_num != sel_row) {
            // print the line with the purchasedf seat
            // else print the standard line with the rwo num
            for (seat in 1..n_seats+1) {
                if (seat == 1) {
                    print("\n"+row_num)
                } else {
                    print(" S")
                }
            }
            } else {
            for (seat in 1..n_seats+1) {
                if (seat == (sel_seat+1)) {
                    print(" B")
                } else if (seat == 1) {
                    print("\n"+row_num)
                } else {
                    print(" S")
                }                }
            }
        row_num = row_num + 1
    }

}
