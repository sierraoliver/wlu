package cp213;

/**
 * Inherited class in simple example of inheritance / polymorphism.
 *
 * @author Sierra Oliver ID: 169067437 Email: oliv7437@mylaurier.ca
 * @version 2022-02-25
 */
public class CAS extends Professor {

    protected String term = null;

    /**
     * CAS constructor
     * 
     * @param lastName   - CAS last name (surname): defined in Person
     * @param firstName  - CAS first name (given name): defined in Person
     * @param department - CAS department: defined in Professor
     * @param term       - CAS term (year, term)
     */
    public CAS(String lastName, String firstName, String department, String term) {
	super(lastName, firstName, department);
	this.term = term;
    }

    /**
     * Getter for term.
     *
     * @return this.term
     */
    public String getTerm() {
	return this.term;
    }

    /**
     * Creates formatted string version of CAS.
     */
    @Override
    public String toString() {
	return (super.toString() + "\nTerm: " + this.term);
    }
}
