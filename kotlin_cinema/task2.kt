fun main() {
    println("Enter the number of rows:")
    val n_rows = readln().toInt()
    println("Enter the number of seats in each row")
    val n_seats = readln().toInt()
    val total = n_rows * n_seats
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
