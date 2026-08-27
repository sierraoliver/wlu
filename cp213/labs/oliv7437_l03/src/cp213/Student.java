package cp213;

import java.time.LocalDate;

/**
 * Student class definition.
 *
 * @author Sierra Oliver ID: 169067437 Email: oliv7437@mylaurier.ca
 * @version 2022-01-17
 */
public class Student implements Comparable<Student> {

    // Attributes
    private LocalDate birthDate = null;
    private String forename = "";
    private int id = 0;
    private String surname = "";

    /**
     * Instantiates a Student object.
     *
     * @param studentID       student ID number
     * @param studentSurname  student surname
     * @param studentForename name of forename
     * @param date            birthDate in 'YYYY-MM-DD' format
     */
    public Student(int studentID, String studentSurname, String studentForename, LocalDate date) {
	id = studentID;
	surname = studentSurname;
	forename = studentForename;
	birthDate = date;
	return;
    }

    /*
     * (non-Javadoc)
     *
     * @see java.lang.Object#toString() Creates a formatted string of student data.
     */
    @Override
    public String toString() {
	String string = "";

	string = String.format("Name:      %s, %s%nID:        %d%n", surname, forename, id);
	string += "Birthdate: " + birthDate;

	return string;
    }

    /*
     * (non-Javadoc)
     *
     * @see java.lang.Comparable#compareTo(java.lang.Object)
     */
    @Override
    public int compareTo(final Student target) {
	int result = 0;
	String targetSur = target.surname;

	if (surname.compareTo(targetSur) == 0) {
	    String targetFore = target.forename;
	    result = forename.compareTo(targetFore);

	    if (result == 0) {
		int targetid = target.id;
		if (targetid < id) {
		    result = 1;
		} else if (targetid > id) {
		    result = -1;
		}

	    }

	} else {
	    result = surname.compareTo(targetSur);
	}

	return result;
    }

    // getters and setters defined here

    /**
     * Gets student ID
     *
     * @return id student ID number
     */
    public int getId() {
	return id;
    }

    /**
     * Sets student ID
     *
     * @param id student ID number
     */
    public void setId(int id) {
	this.id = id;
    }

    /**
     * Gets student Birth Date
     *
     * @return birthDate student Birth Date
     */
    public LocalDate getBirthDate() {
	return birthDate;
    }

    /**
     * Sets student Birth Date
     *
     * @param date student Birth Date
     */
    public void setBirthDate(LocalDate date) {
	birthDate = date;
    }

    /**
     * Gets student Surname
     *
     * @return surname student Surname
     */
    public String getSurname() {
	return surname;
    }

    /**
     * Sets student Surname
     *
     * @param surname student Surname
     */
    public void setSurname(String surname) {
	this.surname = surname;
    }

    /**
     * Gets student Forename
     *
     * @return forename student Forename
     */
    public String getForename() {
	return forename;
    }

    /**
     * Sets student Forename
     *
     * @param forename student Forename
     */
    public void setForename(String forename) {
	this.forename = forename;
    }
}
