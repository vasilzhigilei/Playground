package main

import (
	"fmt"
	"math/rand"
	"testing"
	"time"
)

func BenchmarkStudent(b *testing.B){
	student := NewStudent("Jared")

	rand.Seed(time.Now().UnixNano())
	for i := 0; i < b.N; i++{
		student.AddCourse("CourseName", 4*rand.Float32())
	}
	student.CalculateGPA()

	fmt.Printf("Student GPA: %f\n", student.GetGPA())
}