package main

import (
	"fmt"

	"github.com/go-vgo/robotgo"
)

func main() {
	bitmap := robotgo.CaptureScreen(-1000, -1000, 1920+1000, 1080+1000)
	// use `defer robotgo.FreeBitmap(bit)` to free the bitmap
	defer robotgo.FreeBitmap(bitmap)

	fmt.Println("...", bitmap)

	fx, fy := robotgo.FindBitmap(bitmap)
	fmt.Println("FindBitmap------ ", fx, fy)

	robotgo.SaveBitmap(bitmap, "test.png")
}