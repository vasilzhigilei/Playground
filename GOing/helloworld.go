package main

/* imports input/output similar to C, and other i/o funcs */
import (
	"fmt"
	"time"
)

/* first hello world program in GO */
func main() {
	var name string
	number := 20
	const x uint8 = 10

	fmt.Printf("Enter name: ")
	fmt.Scanf("%s", &name)
	fmt.Printf("\n")

	fmt.Printf("Hello, %s, type is %T\n", name, name)
	fmt.Printf("number = %d, it's type is %T\n", number, number)
	fmt.Printf("const value x = %d, it's type is %T\n", x, x)

	c1 := make(chan string)
	c2 := make(chan string)

	go func() {
		time.Sleep(2 * time.Second)
		c1 <- "one"
	}()
	go func() {
		time.Sleep(1 * time.Second)
		c2 <- "two"
	}()
	for i := 0; i < 2; i++ {
		select {
		case msg1 := <-c1:
			fmt.Println("received", msg1)
		case msg2 := <-c2:
			fmt.Println("received", msg2)
		}
	}
}