package proggeTriks;

import java.sql.*;
import java.util.ArrayList;

/**
 * @author SigveAndreEvensen
 * Simple 'getting started' class for connecting to MySQL using JDBC.
 * We need to use the try-catch block to handle if there are thrown any exception when trying to speak with the database
 * Since there is a lot of things that could go wrong, such as not getting a connection, wrong password/username, wrong in sql-query, ect.
 * When we use try-catch, we can pick up the exception being thrown and handle it as we like. So that the program dosen't crash, but handles exception
 * and continue running.
 * 
 * In this example I am using a person database, and the Table in the database with is called Person.
 */
public class DatabaseConnection {
	//STEP 1: Set up all the variables and objects we need to connect, speak and maintain connection with the database.

	// JDBC driver name(you will need the mysql-connector-java JAR-file, and build a path to it. Link[https://dev.mysql.com/downloads/connector/j/])
	private String JDBC_DRIVER = "com.mysql.jdbc.Driver";  
	//Database URL written on JDBC format.    jdbc:mysql://host:port/database, we specify which table to insert / select from in our SQL-query / SQL-statements.
	private String DB_URL = "jdbc:mysql://mysql.stud.ntnu.no/databaseName";  

	// Database credentials, login information. 
	private final String USER = "username";
	private final String PASS = "password";

	// Initialize Connection object and Statement object. Connection will be used to connect and 'hold' the connection to the database.
	// Statement object will be used as a cursor/executor. This object will execute all the querys, statements and commits. (the communication between DatabaseConnection object and database.
	private Connection conn = null;
	private Statement stmt = null;

	// this 
	private PreparedStatement preparedStatement; // This is derived from the more general class Statemetn. IF you want to execute a Statement object many times, it usually reduces the execution time to use a PreparedStatement object instead. 
												 // The PreparedStatement is sendt to the DBMS right away, where it is compiled. As a result, the PreparedStatement object contains a SQL statement that has been precompiled. THE DBMS can just run the PreparedStatement SQL statement without having to compile it first. 

	// This creates a ResultSet object, which will contain the result set/result table from a select-query to the database. 
	private ResultSet rs;
	
	/**
	 * Establishes connection to MySQL database using JDBC
	 * Class.forName register JDBC Driver
	 * 'conn' tries to establish the physical connection
	 */
	public void establishConnection(){	
		try{
			//STEP 2: Register JDBC driver
			Class.forName("com.mysql.jdbc.Driver").newInstance();

			//STEP 3: Open a connection
			conn = DriverManager.getConnection(DB_URL,USER,PASS);
		}
		catch(SQLException se){
			//Handle errors for JDBC
			se.printStackTrace();
		}
		catch(Exception e){
			//Handle errors for Class.forName
			e.printStackTrace();
		}
	}

	/**
	 * Method to execute SQL-query statement. 
	 * Prints SQLEceptions if thrown.
	 * @param query Complete SQL-query statement.
	 */
	public void insert(String query){
		//STEP 4: Execute a query
		//		System.out.println("Creating statement...");
		try {
			stmt = conn.createStatement(); // Make stmt (Statement object), ready to execute a SQL-query on the Connection object conn.
			preparedStatement = conn.prepareStatement(query); // Make the PreparedStatement object, a pre-compiled statement (makes it faster to execute), of the given query.  
			stmt.executeUpdate(query);
		} catch (SQLException e) {
			System.out.println(e);;
		}

	}

	/**
	 * Method to handle the resultTabel generated from executeQuery(String query)
	 * @param query String written with SQL-syntax, SELECT - query.
	 * @return ArrayList with the result from select-query.
	 */
	public ArrayList<String> select(String query){
		// ArrayList containing String objects/elements called result. This will contain the result from the select query.
		ArrayList<String> result = new ArrayList<String>();

		//STEP 5: Extract data from result set
		try {	//Display or do something with values, we will be saving the result in an ArrayList<Strings> and returning the ArrayList<String>
			stmt = conn.createStatement(); //Make the statement object ready to execute a statement on the Connection object 'conn'.
			rs = stmt.executeQuery(query); //Make the statement object, stmt, execute the query and save the result from the database. 
			ResultSetMetaData meta = rs.getMetaData(); //Create a ResultSetMetaData object called 'meta'. This object will contain meta-data such as how many rows, how many columns, ect there are in our resultSet object (the result we got back from the database when we executed the select-statement.)
			while(rs.next()){ //As long as there are more rows/object in the result we got from the database, we will do these things:
				StringBuilder row = new StringBuilder(); //Create a new StringBuilder object called row, this will contain the row in the result set we currently 'watching'-manipulating. We are using a StringBuilder because the result we got from the database is all Strings.
				for (int i = 1; i <= meta.getColumnCount(); i ++) { //Go through every column in the result set. (only on the given row we are watching).
					String label = meta.getColumnName(i); //Create a String object called 'label', and give it the String value / the name of the given column.
					row.append(label).append(";"); //Add the label/colum name to the row (StringBuilder), and add a ";" to the end of it. We do this to separete the column name and the colum value.
					row.append(rs.getString(label)); //Add the column value to the row (StringBuilder). Now it will look something like this; "columnName;columnValue" ... This will make it easy for us to separate the given columns and column values on the tuple/object/row in the resultSet from the database.
					if (i != meta.getColumnCount()) { //If we aren't on the last column for the row in the database result, do this: 
						row.append(","); //Add a "," to the String. This so we can separate all the column for the row/tuple/object in the result set we are watching/manipulating.  The StringBuilder row should look like "columnName1;value1,columName2;value2,"columName3;value3,..." and so on for each row/object in the database result.
					}
				}
				result.add(row.toString()); //When we have iterated/ gone through all the columns for the tuple/object/row in the database result set. add the string containing all the information about that row/tuple/object in the database result set to the result ArrayList, which we will be returning when we have worked our way through all the rows/tuples/object in the result from the database
			}
		}
		catch (Exception e) { //If there is thrown any exceptions when we try to run/ work our way through or get the result from our query to the database. to this
			e.printStackTrace(); //Print to the terminal the exception that was thrown. Then continue running the program.
		}
		return result; //If no exceptions where thrown, return the result ArrayList<String> containing the result as strings from the database. ["columnName1;value1,columName2;value2","columnName1;value1,columName2;value2","columnName1;value1,columName2;value2",....]
	}

	/**
	 * Terminates the established connections, if they were established/ initialized
	 * Closes stmt, and conn.
	 */
	public void terminateConnection(){
		//STEP 6: Clean-up environment
		try{
			if(stmt!=null) //If the statement is not null (not been initialized with a connection or as a statement. If it's not Null, we need to close it. if it's Null, we don't need to close it, because its never been opened/initialized 
				stmt.close(); //Close the statement. 
		}catch(SQLException se2){
		}//Nothing we can do
		try{
			if(conn!=null) //If the connection is not null (not been initialized with a connection. If it's not Null, we need to close it. if it's Null, we don't need to close it, because its never been opened/initialized 
				conn.close(); //Close the connection
		}catch(SQLException se){
			se.printStackTrace();
		}
	}
	
	public static void main(String[] args) {
		DatabaseConnection dbConnection = new DatabaseConnection();
		System.out.println("Will now try and connect to database...");
		dbConnection.establishConnection();
		System.out.println("Connection established");
		System.out.println("Will now try and push to database..");
		String insertStatement = "INSERT INTO Person VALUES('Test person',99999999,'test@person.no','testadresse 99')";
		dbConnection.insert(insertStatement);
		System.out.println("Insert successful");
		System.out.println("Will now try and execute select-query [Read from database]");
		System.out.println("Select successfull");
		String selectQuery = "SELECT * FROM Person";
		ArrayList<String> result = dbConnection.select(selectQuery);
		System.out.println("Will now print the ArrayList returned from select");
		System.out.println(result.toString());
		System.out.println("Will now Terminate database connection");
		dbConnection.terminateConnection();
		System.out.println("Database connections successfully terminated/closed.");
		System.out.println("Program will now terminate. Hope this code helped. Bye!");
		
	}
	

}
