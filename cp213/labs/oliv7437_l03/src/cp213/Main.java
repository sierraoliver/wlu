package cp213;

import java.time.LocalDate;

/**
 * Tests the Student class.
 *
 * @author Sierra Oliver ID: 169067437 Email: oliv7437@mylaurier.ca
 * @version 2022-01-17
 */
public class Main {

    public static void main(String[] args) {
	final String line = "-".repeat(40);
	int id = 123456;
	String surname = "Brown";
	String forename = "David";
	LocalDate birthDate = LocalDate.parse("1962-10-25");
	Student student = new Student(id, surname, forename, birthDate);
	System.out.println("New Student:");
	System.out.println(student);
	System.out.println(line);
	String studentFormat = student.toString();
	System.out.println(studentFormat);
	System.out.println("Test Getters");

	// call getters here
	int getID = student.getId();
	System.out.println("Expected: " + id + " Got: " + getID);

	String getSurname = student.getSurname();
	System.out.println("Expected: " + surname + " Got: " + getSurname);

	String getForename = student.getForename();
	System.out.println("Expected: " + forename + " Got: " + getForename);

	LocalDate getBirthDate = student.getBirthDate();
	System.out.println("Expected: " + birthDate + " Got: " + getBirthDate);

	System.out.println(line);
	System.out.println("Test Setters");

	// call setters here
	student.setId(999999);
	System.out.println("Set to: 999999" + " Got: " + student.getId());

	student.setSurname("Dave");
	System.out.println("Set to: Dave" + " Got: " + student.getSurname());

	student.setForename("Dawson");
	System.out.println("Set to: Dawson" + " Got: " + student.getForename());

	student.setBirthDate(LocalDate.parse("1998-01-23"));
	System.out.println("Set to: 1998-01-23" + " Got: " + student.getBirthDate());

	System.out.println("Updated Student:");
	System.out.println(student);
	System.out.println(line);
	System.out.println("Test compareTo");

	// create new Students - call comparisons here
	Student s1 = new Student(123456, "Brown", "David", LocalDate.parse("1962-10-25"));
	Student s2 = new Student(0, "Brown", "David", LocalDate.parse("1962-10-25"));
	int result = s1.compareTo(s2);
	System.out.println("Expected: " + 1 + " CompareTo Result: " + result);

    }

}
