package proggeTriks;


/**
 * @author SigveAndreEvensen
 * This is example and demonstration of the ways to format a string in Java.
 * Source: http://examples.javacodegeeks.com/core-java/lang/string/java-string-format-example/
 * I put together the code from this site, and it's comments and explanation.
 */
public class StringFormating {

/*
* There are multiple ways of formatting a string in Java. It can be done with the use of String.format()
* or by system.out.printf() or by the StringFormatter class
*/

/* Syntax: 
 * "% [argument index] [flag] [width] [.precision] type"
 * % is a special character denoting that a formatting instruction follows.
 * [argument index] explicitly denoted the index of the arguments to be formatted. If it not present, arguments will be formatted in the same order as they appear in the arguments list.
 * [flag] is a special formatting instruction. For example, the + flag specifies that a numeric value should always be formatted with a sign, and the 0 flag specifies that 0 is the padding character. Other flags include – that is pad on the right , + pad on the left (if the formatted object is a string). Note that some flags cannot be combined with certain other flags or with certain formatted objects.
 * [width] denotes the minimum number of output characters for that Object.
 * [.precession] denotes the precision of floating point numbers in the output. That is basically the number of decimal digits you wish to print on the output. But it can be used for other types to truncate the output width
 * type along with %, are the only mandatory formatting arguments. type simply denotes the type of the object that will be formatted in the output. For integers that is d, for strings that is s, for floating point numbers that is f, for integers with hex format that is x.
 * 
 */
	
	public void example(){
		System.out.printf("Integer : %d\n",15);
		System.out.printf("Floating point number with 3 decimal digits: %.3f\n",1.21312939123);
		System.out.printf("Floating point number with 8 decimal digits: %.8f\n",1.21312939123);
		System.out.printf("String: %s, integer: %d, float: %.6f", "Hello World",89,9.231435);
	}
	
	
/* Integer formatting
*  %d   : will print the integer as it is.
*  %6d  : will pint the integer as it is. If the number of digits is less than 6, the output will be padded on the left.
*  %-6d : will pint the integer as it is. If the number of digits is less than 6, the output will be padded on the right.
*  %06d : will pint the integer as it is. If the number of digits is less than 6, the output will be padded on the left with zeroes.
*  %.2d : will print maximum 2 digits of the integer.
*/
	
	
	public void integerFormatting(){
		System.out.printf("%-12s%-12s%s\n","Column 1","Column 2","Column3");
		System.out.printf("%-12d%-12d%07d\n",15,12,5);
	}

/* String formatting
 * %s       : will print the string as it is.
 * %15s    : will pint the string as it is. If the string has less than 15 characters, the output will be padded on the left.
 * %-6s  : will pint the string as it is. If the string has less than 6 characters, the output will be padded on the left.
 * %.8d : will print maximum 8 characters of the string.
 */
	
	public void stringFormatting(){
		System.out.printf("%-12s%-12s%s\n","Column 1","Column 2","Column3");
		System.out.printf("%-12.5s%s", "Hello World","World");
	}

/* Floating point formatting
 * %f       : will print the number as it is.
 * %15f    : will pint the number as it is. If the number has less than 15 digits, the output will be padded on the left.
 * %.8f : will print maximum 8 decimal digits of the number.
 * %9.4f : will print maximum 4 decimal digits of the number. The output will occupy 9 characters at least. If the number of digits is not enough, it will be padded
 */
	
	public void floatFormatting(){
		System.out.printf("%-12s%-12s\n","Column 1","Column 2");
		System.out.printf("%-12.5f%.20f", 12.23429837482,9.10212023134);
	}
	
/*Using String.format
 * If you don’t want to print out the String and just want to format it for later use,
 *  you can use the static format method of the String class
 */
	
	public void stringFormatFormatting(){
		String s = String.format("%-12.5f%.20f", 12.23429837482,9.10212023134);
		System.out.println(s);
	}

	public static void main(String[] args) {
		StringFormating formatter = new StringFormating();
		System.out.println("Lets see an example");
		formatter.example();
		System.out.println();
		System.out.println();
		System.out.println("Lets see how integer formatting looks");
		formatter.integerFormatting();
		System.out.println();
		System.out.println("Lets see how string formatting looks");
		formatter.stringFormatting();
		System.out.println();
		System.out.println();
		System.out.println("Lets see how floating point formatting looks");
		formatter.floatFormatting();
		System.out.println();
		System.out.println();
		System.out.println("lets see how String.format() looks");
		formatter.stringFormatFormatting();
	}
	
	
	
}
