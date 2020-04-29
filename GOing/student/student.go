package main

/*
Student struct, all member fields are private, access given via funcs
 */
type Student struct {
	// lowercase, so private fields
	name string
	year int
	major string
	gpa float32
	courses map[string]float32 // map of courses, name of course : grade out of 4.0
}

/*
Constructor for new student, returns pointer to new student
 */
func NewStudent(name string) *Student {
	/*
	return address of Student
	 */
	return &Student{
		name: name,
		year: 1,
		major: "undecided",
		gpa: 4.0,
		courses: make(map[string]float32), // initialize map to avoid nil runtime errors
	}
}

// UTILITY FUNCS

func (s *Student) AddCourse(course string, grade float32){
	s.courses[course] = grade
}

func (s *Student) CalculateGPA(){
	// running sum variable
	var sum float32
	for _, grade := range s.courses{
		sum += grade
	}
	// set gpa to calculated grade point average from courses
	s.gpa = sum/float32(len(s.courses))
}

// GETTER AND SETTERS BELOW

// SETTER FUNCS
func (s *Student) SetName(name string){
	s.name = name
}

func (s *Student) SetYear(year int){
	s.year = year
}

func (s *Student) SetMajor(major string){
	s.major = major
}

func (s *Student) SetGPA(gpa float32){
	s.gpa = gpa
}

func (s *Student) SetCourses(courses map[string]float32){
	s.courses = courses
}

// GETTER FUNCS
func (s *Student) GetName() string{
	return s.name
}

func (s *Student) GetYear() int{
	return s.year
}

func (s *Student) GetMajor() string{
	return s.major
}

func (s *Student) GetGPA() float32{
	return s.gpa
}

func (s *Student) GetCourses() map[string]float32{
	return s.courses
}


