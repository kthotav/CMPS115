package db;

import java.sql.*;
import java.util.Scanner;
import java.io.*;
import java.util.Date;
import java.util.Calendar;


public class db {	
	public static void main(String[] args) throws IOException {
		//open the scanner so that we can read in the file to be inserted into the database;
		Scanner in = new Scanner (new BufferedReader(new FileReader(new File( args[0]))));
		
		/*open the FileWriter so that we can dump information from the database to a file
		 * so that the data can then be visualized.
		 */
		BufferedWriter out = new BufferedWriter (new FileWriter("fromdb_" +"dick.csv"));
		BufferedWriter outBMS1 = new BufferedWriter (new FileWriter("cleanBMS1.csv"));
		BufferedWriter outBMS2 = new BufferedWriter (new FileWriter("cleanBMS2.csv"));
		// variables that are used by jdbc to connect to our database;
		String url = "jdbc:mysql://localhost/homedb" ;
		String username = "root";

		
		try{
			//establish connection to database.
			Connection myConn = DriverManager.getConnection(url , username , "");
			
			//create a statement.
			Statement myStmt = myConn.createStatement();
			
			//testing the print from PV function
			printFromDB_PV(out , myConn);
			printFromDB_BMS(outBMS1, myConn, 1);
			printFromDB_BMS(outBMS2, myConn, 2);
			System.out.println("printtobms");
			
			//make and SQL query.
			ResultSet myRs = myStmt.executeQuery("select * from PV");
			
			//process the results
			while(myRs.next()){
				out.write(myRs.getString("TimeStamp") + "," + myRs.getString("Temperature") +"\n");
							
			}
			
			//manual insertion into database without reading from file.
			String insert = "insert into PV "
						  + "(TimeStamp,Temperature) " 
						  + " values ('00:00','32.32')";
						  
			//Execute the actual insertion of the data into the database.
			myStmt.executeUpdate(insert);
			//making sure that the Scanner is reading from the file given
			if(in.hasNextLine()){
				System.out.println("reading");
				out.write("writing");
			}
			System.out.println("----------Insertion complete-----------");
			
			
			String delete = "delete from PV where Date = '0'";
			
			System.out.println("----------Deletion complete-----------");
			
			//Execute deletion from the database.
			myStmt.executeUpdate(delete);
			
			
			
		} 
		catch (Exception exc){
			exc.printStackTrace();
		
		}
		in.close();
		outBMS1.flush();
		outBMS1.close();
		outBMS2.flush();
		outBMS2.close();
		out.flush();
		out.close();

	}
	
	//used for inserting into the PV table in the database
	void insertToDB_PV(){
		
	}
	//used for inserting into the BMS-R1 table in the database
	void insertToDB_BMS_R1(){
		
	}
	//used for inserting into the BMS-R2 table in the database
	void inserToDB_BMS_R2(){
		
	}
	//used to print all data from the PV table into a file specified by the program
	static void printFromDB_PV(BufferedWriter out, Connection myConn){
		//create a statement.
		try{
		Statement pvStmt = myConn.createStatement();
		
		//make and SQL query for the PV table in the database.
		ResultSet pvResults = pvStmt.executeQuery("select * from PV");
		
		//write the columns of the database before the data is written out 
		out.write("TimeStamp" 
				+ "," + "Date" 
				+ "," + "Pac" 
				+ "," + "Temperature"
				+ "\n");
		//process the results from the pv table in the database
		while(pvResults.next()){
			out.write(pvResults.getString("TimeStamp") 
						+ "," + pvResults.getString("Date") 
						+ "," + pvResults.getString("Pac") 
						+ "," + pvResults.getString("Temperature")
						+ "\n");
						
		}
		}catch(Exception x){
			x.printStackTrace();
		}
	}
	 //used to print all data from the BMS table into a file specified by the program
	static void printFromDB_BMS(BufferedWriter out, Connection myConn, int roomNum){
		try{
		Statement pvStmt = myConn.createStatement();
		ResultSet pvResults = null;
		
		//pick query based on room number
		switch (roomNum){
		case 1: 
			pvResults = pvStmt.executeQuery("select * from bmsr1");
			break;
		
		case 2: 
			pvResults = pvStmt.executeQuery("select * from bmsr2");
			break;
		}

		//write the column names
		out.write("TimeStamp" 
				+ "," + "Date" 
				+ "," + "Temperature" 
				+ "," + "Relative-Humidity"
				+ "," + "CO_2"
				+ "," + "Sensible-Heat"
				+ "\n");
		//process the data from database in BMS
		while(pvResults.next()){
			out.write(pvResults.getString("TimeStamp") 
						+ "," + pvResults.getString("Date") 
						+ "," + pvResults.getString("Temperature") 
						+ "," + pvResults.getString("Relative-Humidity")
						+ "," + pvResults.getString("CO_2")
						+ "," + pvResults.getString("Sensible-Heat")
						+ "\n");
						
		}
		}catch(Exception x){
			x.printStackTrace();
		}
		
	}
}
