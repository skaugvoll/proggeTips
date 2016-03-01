package proggeTriks;

import org.junit.Test;

import junit.framework.TestCase;

/*
 * For å lage en testklasse, trenger vi en klasse såm MÅ extende TestCase-klassen til JUnit
 * for å kunne få kjørt testkodene vi skriver, må vi legge koden inn i metoder, disse metodenes navn MÅ begynne med test.
 * metodene må også være void-metoder uten argumenter. Over methode-hodet må vi ha en "assertion" --> @ -tegnet. 
 * assertion må være etterfulgt av hva det er metoden skal gjøre. Skal det være en test-metode må det stå @Test
 */


/*  JUnit annotations:
 *@Test  : The @Test annotation identifies a method as a test method.
 *@Test(expected = Exception.class : Fails if the method does not throw the named exception.
 *@Test(timeout=100) : Fails if the method takes longer than 100 milliseconds.
 *  
 *@Before : This method is executed before each test. It is used to prepare the test environment (e.g., read input data, initialize the class).
 *@BeforeClass : This method is executed once, before the start of all tests. It is used to perform time intensive activities, for example, to connect to a database. Methods marked with this annotation need to be defined as static to work with JUnit.
 *  
 *@After : This method is executed after each test. It is used to cleanup the test environment (e.g., delete temporary data, restore defaults). It can also save memory by cleaning up expensive memory structures.
 *@AfterClass : This method is executed once, after all tests have been finished. It is used to perform clean-up activities, for example, to disconnect from a database. Methods annotated with this annotation need to be defined as static to work with JUnit.
 *  
 *@Ignore or @Ignore("Why disabled") : Ignores the test method. This is useful when the underlying code has been changed and the test case has not yet been adapted. Or if the execution time of this test is too long to be included. It is best practice to provide the optional description, why the test is disabled.
 */


/* Assert Statements
 * fail(message) : Let the method fail. Might be used to check that a certain part of the code is not reached or to have a failing test before the test code is implemented. The message parameter is optional.
 * assertTrue([message,] boolean condition) : Checks that the boolean condition is true. 
 * assertFalse([message,] boolean condition) : Checks that the boolean condition is false.
 * assertEquals([message,] expected actual) : Tests that two values are the same. Note: for arrays the reference is checked not the content of the arrays.
 * assertEquals([message,] expected, actual tolerance) : Test that float or double values match. The tolerance is the number of decimals which must be the same.
 * assertNull([message,] object) : 	Checks that the object is null.
 * assertNotNull([message,] object) : Checks that the object is not null.
 * assertSame([message,] expected actual) : Checks that both variables refer to the same object.
 * assertNotSame([message,] expected actual) : Checks that both variables refer to different objects.
 */

public class PersonTest extends TestCase {
	//creates a test object from the class we want to test.
	
	Person pers = new Person("Anonymous", 21, "12345678");
	
	//creates a valid testmetod, it's void, starts with 'test' and no parameters
	@Test
	public void testConstructer(){
		assertEquals("Anonymous", pers.getName()); //assertEquals, check to see if first parameter is equal to second parameter (if expected name matches name from testobject)
		assertEquals(21, pers.getAge()); //checks if the age that we was set in the test persons constructor is what we wanted
		assertEquals("12345678", pers.getMobile()); //checks if the mobile number we gave the test person 'pers', is what we expected.
	}
	
	@Test(expected = IllegalArgumentException.class) //denotes that the method under is a testmethod that's going to test and expect a exception to be thrown. if not thrown, it fails
	public void testSetNameException(){ //void method, no arguments and starts with test
		pers.setName("Anno86"); //set the name on testPerson from Sigve to Kim, --> should throw IllegalArgumentException and give green test. If changed to Anno --> Red test.
	}
	

}
