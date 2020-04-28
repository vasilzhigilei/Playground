package student

import (
	"fmt"
	"math/rand"
	"testing"
)

func BenchmarkStudent(b *testing.B){
	student := NewStudent("Jared")

	for i := 0; i < b.N; i++{
		student.AddCourse("CourseName", 4*rand.Float32())
	}
	student.CalculateGPA()

	fmt.Printf("Student GPA: %f", student.GetGPA())
}