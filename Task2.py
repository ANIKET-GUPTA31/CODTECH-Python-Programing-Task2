# Task two : STUDENT GRADE TRACKER
# CodTech IT Solutions Pvt. Ltd.! 

#creating a class to manage all info of student 
class GradeManager:
    def __init__(self):
        self.grades = {}

    def add_grade(self, subject, grade):   # This function is created to add a grade.
        if subject in self.grades:
            self.grades[subject].append(grade)

        else:
            self.grades[subject] = [grade]


    def calculate_average(self):     # This function is created to calculate a average.
        total_grades = sum(sum(grades) for grades in self.grades.values()) #This line calculates the total of all grades by summing the grades for each subject in the self.grades dictionary.
        total_subjects = sum(len(grades) for grades in self.grades.values()) #This line calculates the total number of subjects by summing the count of grades for each subject in the self.grades dictionary.
        return total_grades / total_subjects if total_subjects > 0 else 0
    

    def get_letter_grade(self, average): #This function is created to add a grade.
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'


    def get_gpa(self, average): # calculate gpa 
        if average >= 90:
            return 4.0
        elif average >= 80:
            return 3.0
        elif average >= 70:
            return 2.0
        elif average >= 60:
            return 1.0
        else:
            return 0.0


    def display_grades(self):  # option 2 for Display Grades
        print("\nGrades by subject:")
        for subject, grades in self.grades.items():
            grades_str = ', '.join(map(str, grades))
            print(f"{subject}: {grades_str}")


    def display_summary(self):  # Option 3 for Display Summary 
        average = self.calculate_average() #This line calls the `calculate_average` method from the current instance to compute the average and assigns the result to the variable `average`.
        letter_grade = self.get_letter_grade(average)
        gpa = self.get_gpa(average)

        print(f"\nOverall Average Grade: {average:.2f}")
        print(f"Letter Grade: {letter_grade}")
        print(f"GPA: {gpa:.2f}")

def main():
    grade_manager = GradeManager()

    while True:
        print("\nMenu:")
        print("1. Add Grade")
        print("2. Display Grades")
        print("3. Display Summary")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1': # this function is add all subjects name and grades

            total_sub = input("How many subject you have:")
            for i in range(int(total_sub)): #This loop is designed to run as many times as there are subjects.
                subject = input(f"Enter subject name{i+1}: ")

                try:
                    grade = float(input("Enter grade (0-100): "))
                    if 0 <= grade <= 100:
                        grade_manager.add_grade(subject, grade)
                    else:
                        print("Grade must be between 0 and 100.")
                except ValueError:
                    print("Invalid input! Please enter a numerical grade.")


        elif choice == '2':
            grade_manager.display_grades()


        elif choice == '3':
            grade_manager.display_summary()


        elif choice == '4':
            print("Exiting the program.")
            break


        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":   # main function of code 
    main()
