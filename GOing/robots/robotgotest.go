package main

import "github.com/go-vgo/robotgo"

func main() {
	// you really shouldn't run this.
	for i := 0; i < 1920; i+=20 {
		for j:=0; j < 1080; j+=10 {
			robotgo.MoveMouse(i,j)
			robotgo.MouseClick("right", true)
		}
	}
}