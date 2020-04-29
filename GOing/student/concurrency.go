package student

import (
	"fmt"
	"math/rand"
	"time"
)

func main(){
	var charset string = "abcdefghijklmnopqrstuvwxyz"

	studentsToName := make(chan Student, 100)
	studentsToGPA := make(chan Student, 100)

	go workerMakeStudent(studentsToName, studentsToGPA, charset, 5)

}

func workerMakeStudent(students <-chan Student, results chan<- Student, charset string, length int) {
	var seededRand *rand.Rand = rand.New(rand.NewSource(time.Now().UnixNano()))
	for s := range students{
		b := make([]byte, length)
		for i := range b {
			b[i] = charset[seededRand.Intn(len(charset))]
		}
		s.SetName(string(b))
		results <- s
	}
}