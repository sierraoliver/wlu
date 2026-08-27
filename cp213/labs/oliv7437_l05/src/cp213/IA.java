package cp213;

/**
 * Inherited class in simple example of inheritance / polymorphism.
 *
 * @author Sierra Oliver ID: 169067437 Email: oliv7437@mylaurier.ca
 * @version 2022-02-25
 */
public class IA extends Student {

    protected String course = null;

    /**
     * IA constructor
     * 
     * @param lastName  - IA last name (surname): defined in Person
     * @param firstName - IA first name (given name): defined in Person
     * @param id        - IA id number: defined in Student
     * @param course    - IA course code
     */
    public IA(String lastName, String firstName, String id, String course) {
	super(lastName, firstName, id);
	this.course = course;
    }

    /**
     * Getter for course
     *
     * @return this.course
     */
    public String getCourse() {
	return this.course;
    }

    /**
     * Creates formatted string version of IA.
     */
    @Override
    public String toString() {
	return (super.toString() + "\nCourse: " + this.course);
    }

}
