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
			printFromDB_BMS(myConn, 1);
			printFromDB_BMS(myConn, 2);
			  
			printFromDB_BMS_Combined(myConn, 1);
			printFromDB_BMS_Combined(myConn, 2);
			
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
	
	static void printFromDB_BMS_Combined(Connection myConn, int roomNum){
		
		try{
			Statement pvStmt = myConn.createStatement();
			ResultSet pvResults = null;
			
			BufferedWriter out = null;
			switch (roomNum){
			case 1:
				out = new BufferedWriter (new FileWriter("BMSOne.csv"));
				break;
			case 2:
				out = new BufferedWriter (new FileWriter("BMSTwo.csv"));
				break;
			}

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
					+ "," + "VarDate" 
					+ "," + "Temperature" 
					+ "," + "RelativeHumidity"
					+ "," + "COtwo"
					+ "," + "SensibleHeat"
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
				out.flush();
				out.close();
							
			}
			}catch(Exception x){
				x.printStackTrace();
			}
	}
	
	
	 //used to print all data from the BMS table into a file specified by the program
	static void printFromDB_BMS(Connection myConn, int roomNum){
		try{
		Statement bmsStmt = myConn.createStatement();

		//create an array that represents each column in the database
		String[] column = {"Temperature", "Relative-Humidity", "CO_2", "Sensible-Heat"};
		String[] columnName = {"Temperature", "RelativeHumidity", "COtwo", "SensibleHeat"};
		//create a file and write data for date, time, and one of the columns.
		for(int i = 0; i < column.length; i++ ){
				//select database based on roomNum
				ResultSet bmsResults = bmsStmt.executeQuery("select * from bmsr" + roomNum);
				
				//filen vbxcame is based off of room number and column name.
				BufferedWriter out = null;
				switch (roomNum){
				case 1:
					out = new BufferedWriter (new FileWriter("BMSOne" + columnName[i] + ".csv"));
					break;
				case 2:
					out = new BufferedWriter (new FileWriter("BMSTwo" + columnName[i] + ".csv"));
					break;
				}
				
				//write first row with names of columns
				out.write("TimeStamp" 
						+ "," + "Date" 
						+ "," + columnName[i]
						+ "\n");
				
				//write data from database of timestamo, date, and the designated column
				while(bmsResults.next()){
					out.write(bmsResults.getString("TimeStamp")
							+ "," + bmsResults.getString("Date")
							+ "," + bmsResults.getString(column[i])
							+ "\n");
				}
				
				out.flush();
				out.close();
			}
		}catch(Exception x){
			x.printStackTrace();
		}
	}
	
	
}
