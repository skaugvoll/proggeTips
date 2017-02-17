import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

/**
 * Created by skaugvoll on 16.02.2017.
 */
public class LambdaTutorial {

    /*
    * Welcome to Lambda expressions in Java tutorial.
    *
    * First, lets figure out what lambda expressions are!
    * Lambdas provide a clear and concise way to represent ONE method interface using an expression (anonymous inner classes).
    * All this means is that it allows you to easily and quickly write a method, that might will be used only once,
    * and you don't have to wright the entire method, with head and body. Only the body of the method.
    *
    * Lambda expressions also improve the Collection libraries making it easier to iterate through, filter, and extract data from a Collection.
    * We will see examples of this, and explain it in depth.
    *
    * Lambda will make you write simpler code, and execute functional programming, and also write less lines of code,
    * and for-loops.
    *
    * */

    /*
    * FUNCTIONAL INTERFACES
    *
    * To understand and be able to write lambda expressions, you need to understand and know
    * what a functional interface is.
    *
    * All it is, is a interface, that has only / exactly one method defined.
    * The method, takes in arguments, and returns a result.
    *
    * There is only one requirement to the class that implements the interface,
    * and that is, that the method defined in the interface, is the only method in the class that implements it.
    *
    * It's as simple as that.
    * */

    /*
    * Lambda expressions
    *
    * The difference between a Functional Interface and a lambda expresisons is;
    * that he lambda expression only cares about what the interface method is suppose to do and return.
    * And lets us implement and use only that. We doen't have write a interface and a class that implements that interface,
    * and then implement the method, then use the method.
    *
    * Lambda expressions uses the operator "->"
    * To the left of the "arrow / ->" the arguments that are given to the method is provided,
    * and to the right of the "arrow / ->" the body of the method is defined and what to return.
    *
    * */

    /*
    * Pre defined functional interfaces from Java.
    *
    * Predicate : a method "Test" that takes in an object as a argument, and returns a boolean
    *
    * Consumer : a method "accept" that takes in a object as argument, and returns nothing (void)
    *
    * BinaryOparator<T> : a method "apply" that takes in two objects of the given type <T>, and returns ONE object of the type <T>
    *      example is addition: takes in two doubles, and returns the sum as a double .
    *
    * */

    /*
    * Lets get started!
    *
    * Now that all the boring theory is overwith, lets get to the good part, CODING!
    * To illustrate Lambda expressions, we will create a basic and simple person class (see Person.class),
    * that we will be using the Lambda expressions on.
    *
    * When we have implemented the Person class, we will create a list of persons, and then
    * add 5 person object to the list. So we have some data to play with.
    *
    * */


    ArrayList<Person> persons; // Initialize a list to contain persons to use lambdas on.

    public LambdaTutorial() {
        persons = new ArrayList<Person>(); // instanciate / create the list

        // Create person object and add to the persons list.
        persons.add(new Person("Ola", 10, 'M'));
        persons.add(new Person("Kari", 12, 'F'));
        persons.add(new Person("Per", 22, 'M'));
        persons.add(new Person("Pål", 17, 'M'));
        persons.add(new Person("Espen", 19, 'M'));
    }

    /* How to use lambda expression to sort a ArrayList.
    *
    * Since we call sort on the list we want to sort, sort takes in two and two (the arguemnts) persons from the persons list
    * and sends them into the expression. Then the expression compares and sorts, and then returns the order of the two persons
    *
    * This happens for the entire list, and therfore the list is sorted.
    * We just saved a bunch of lines! #Sweet.
    *
    */

    public void sortOnNameWithLambda(){
        System.out.println("Before sorting with lambda: " + persons);
        persons.sort(
              // Args   LamdaOperator       method body and return statement
                (a, b)        ->            a.getName().compareTo(b.getName())
        );
        System.out.println("After sorting with lambda: " + persons);
    }

    private void sortOnNameWithoutLambda(){
        persons.sort(new Comparator<Person>() {
            public int compare(Person a, Person b) {
                return a.getName().compareTo(b.getName());
            }
        });
        System.out.println(persons);
    }



    /* Lets sort the list of persons after age!
    *
    * */

    public void sortOnAgeWithLambda(){
        System.out.println("Before sorting with lambda: " + persons);
        persons.sort(
                (a, b) -> a.getAge() - b.getAge()
        );
        System.out.println("After sorting with lambda: " + persons);

    }

    private void sortOnAgeWithoutLambda(){
        persons.sort(new Comparator<Person>() {
                         @Override
                         public int compare(Person a, Person b) {
                             return a.getAge() - b.getAge();
                         }
                     }
                    );
        System.out.println(persons);
    }

    /*
    * To iterate through each object in a list, the Stream function hits the sweet spot.
     * It returns one and one (like a for each loop).
     *
     * anyMatch() is a function that takes in a "predicate" instance and returns atleast one of the elements in the stream,
     * that satisfy the "anyMatch requirement". If one match is found, "true" is returned, else "false"
     *
    * */

    public void checkIfListContainsAtleastOneWithGenderMaleWithlambda(){
        System.out.println("");

        System.out.println(persons.stream().anyMatch(
                p -> p.getGender() == 'M'
        ));

        System.out.println("");
    }


    /* Filtering!
     * Lets filter the persons list on persons that are 18 years old or younger.
     *
     * For this we have to use the "stream()" and  "filter()" functions.
     * */

    public void filterOnAgeWithLambda(){
        System.out.println("Persons list: " + persons);
        List youths = persons.stream().
                filter(
                    p -> p.getAge() <= 18
                ).
                collect(
                        Collectors.toList()
                );

        System.out.println("New list containing youths: " + youths);

    }





    // Method to run the tutorial examples
    public static void main(String[] args) {
        LambdaTutorial tutorial = new LambdaTutorial();
        System.out.println("*Sorting on Name!");
        tutorial.sortOnNameWithLambda();

        tutorial.printSpacesBetweenMethod();

        System.out.println("*Sorting on Age");
        tutorial.sortOnAgeWithLambda();

        tutorial.printSpacesBetweenMethod();

        System.out.println("*Checking for person in list with Gender for Male");
        tutorial.checkIfListContainsAtleastOneWithGenderMaleWithlambda();

        tutorial.printSpacesBetweenMethod();

        System.out.println("*Filtering on persons younger then 19");
        tutorial.filterOnAgeWithLambda();


    }

    private void printSpacesBetweenMethod(){
        for(int i = 0; i < 2; i++){
            System.out.println();
        }
    }

}
