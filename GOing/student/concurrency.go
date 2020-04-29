package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main(){
	var charset string = "abcdefghijklmnopqrstuvwxyz"
	var seededRand *rand.Rand = rand.New(rand.NewSource(time.Now().UnixNano()))

	studentsToGPA := make(chan *Student, 100)
	studentsToSort := make(chan *Student, 100)

	go workerMakeStudent(studentsToGPA, seededRand, charset, 5)
	go workerMakeGPA(studentsToGPA, studentsToSort, seededRand)

	for i := 0; i < 100; i ++ {
		fmt.Println((<-studentsToSort).GetGPA())
	}
}

func workerMakeStudent(results chan<- *Student, random *rand.Rand, charset string, length int) {
	for i := 0; i < 100; i++ {
		b := make([]byte, length)
		for i := range b {
			b[i] = charset[random.Intn(len(charset))]
		}
		s := NewStudent(string(b))
		results <- s
	}
}

func workerMakeGPA(students <- chan *Student, results chan<- *Student, random *rand.Rand){
	for s := range students{
		for i:= 0; i < 5; i++ {
			s.AddCourse("course", 4*random.Float32())
		}
		s.CalculateGPA()
		results <- s
	}
}