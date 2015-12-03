
import java.sql.*;
import java.io.*;
import java.util.Scanner;
import java.util.Calendar;



public class Driver {

	public static void main(String[] args) throws IOException {
		
		//open the scanner so that we can read in the file to be inserted into the database;
		Scanner pv = new Scanner (new BufferedReader(new FileReader(new File( args[0]))));
		Scanner pv1 = new Scanner (new BufferedReader(new FileReader(new File( args[1]))));
		Scanner pv2 = new Scanner (new BufferedReader(new FileReader(new File( args[2]))));
		Scanner pv3 = new Scanner (new BufferedReader(new FileReader(new File( args[3]))));
		Scanner pv4 = new Scanner (new BufferedReader(new FileReader(new File( args[4]))));
		Scanner BMSR1_temp = new Scanner (new BufferedReader(new FileReader(new File(args[5]))));
		Scanner BMSR1_humid = new Scanner (new BufferedReader(new FileReader(new File(args[6]))));
		Scanner BMSR1_heat = new Scanner (new BufferedReader(new FileReader(new File(args[7]))));
		Scanner BMSR2_temp = new Scanner (new BufferedReader(new FileReader(new File(args[8]))));
		Scanner BMSR2_humid = new Scanner (new BufferedReader(new FileReader(new File(args[9]))));
		Scanner BMSR2_heat = new Scanner (new BufferedReader(new FileReader(new File(args[10]))));
		
		// variables that are used by jdbc to connect to our database;
		String url = "jdbc:mysql://localhost:8889/CSV_DB" ;
		String username = "root";
		String password = "root";
		
		//store the current year.
		int year = Calendar.getInstance().get(Calendar.YEAR);
		
		try{
			//establish connection to database.
			Connection myConn = DriverManager.getConnection(url , username , password);
			System.out.print("-----------------------\n");
			System.out.println("Beginning Insertion into Database");
			System.out.print("-----------------------\n");
			delete(myConn);
			insertToDB_PV(myConn,pv,args[0]);
			insertToDB_PV(myConn,pv1,args[1]);
			insertToDB_PV(myConn,pv2,args[2]);
			insertToDB_PV(myConn,pv3,args[3]);
			insertToDB_PV(myConn,pv4,args[4]);
		    insertToDB_BMS_R1(myConn,BMSR1_temp,BMSR1_humid,BMSR1_heat,year);
			insertToDB_BMS_R2(myConn,BMSR2_temp,BMSR2_humid,BMSR2_heat,year);
			System.out.println("Insertion into the Database Complete");
			System.out.print("-----------------------\n");
			System.out.println("Beginning Printing from BMS Database");		
			System.out.print("-----------------------\n");
			printFromDB_BMS_Combined(myConn, 1);
			printFromDB_BMS_Combined(myConn, 2);
			printFromDB_PV(myConn);
			System.out.println("Printing from BMS Database Complete");
			System.out.print("-----------------------\n");
		} 
		catch (Exception exc){
			exc.printStackTrace();
		
		}
		//close all scanners and file writers.
		BMSR1_heat.close();
		BMSR1_humid.close();
		BMSR1_temp.close();
		BMSR2_heat.close();
		BMSR2_humid.close();
		BMSR2_temp.close();
		pv.close();
		pv1.close();
		pv2.close();
		pv3.close();
		pv4.close();

	}
	
	//used for inserting into the PV table in the database
	static void insertToDB_PV(Connection myConn,Scanner in1, String filename){
		try{
			String line,value1,value2,value3,date,timeStep;
			String insertDB = "INSERT INTO PV"
					+"(TimeStep, VarDate, PAC, Temperature, VAC) VALUES"
					+ "(?,?,?,?,?)";
			PreparedStatement myStmt = myConn.prepareStatement(insertDB);
		    date = date_parse(filename);
		    while(in1.hasNextLine()){
		    	line = in1.nextLine();
		    	String[] results = line.split(",");
		    	timeStep = results[0];
		    	value1 = results[1];
		    	value2 = results[2];
		    	value3 = results[3];
		    	myStmt.setString(1, timeStep);
		    	myStmt.setString(2, date);
		    	myStmt.setString(3, value1);
		    	myStmt.setString(4, value2);
		    	myStmt.setString(5, value3);
		    	myStmt.executeUpdate();
		    }
			
		}catch(Exception x){
			x.printStackTrace();
		}
	}
	
	//used for inserting into the BMS-R1 table in the database
	static void insertToDB_BMS_R1(Connection myConn,Scanner in1,Scanner in2,Scanner in3,int year){
		try{
			String line1,line2,line3, date, timeStamp;
			String value1,value2,value3;
			String insertDB = "INSERT INTO BMSR1"
					+"(TimeStamp, VarDate, Temperature, RelativeHumidity, CO_2, SensibleHeat) VALUES"
					+ "(?,?,?,?,?,?)";
			PreparedStatement myStmt = myConn.prepareStatement(insertDB);
			line1 = in1.nextLine();
			line2 = in2.nextLine();
			line3 = in3.nextLine();
			while(in1.hasNextLine()){
				line1 = in1.nextLine();
				line2 = in2.nextLine();
				line3 = in3.nextLine();
				String[] results1 = line1.split(",");
				String[] results2 = line2.split(",");
				String[] results3 = line3.split(",");
				results1[5] = time_adjustment(results1[5]);
				date = time_parse(results1[2]) + "-" + results1[3] + "-" + String.valueOf(year) ;
				timeStamp = results1[5] + ":" + time_parse(results1[6]);
				value1 = data_truncation(results1[10]);
				value2 = data_truncation(results2[10]);
				value3 = data_truncation(results3[10]);
				myStmt.setString(1,timeStamp);
				myStmt.setString(2,date);
				myStmt.setString(3,value1);
				myStmt.setString(4,value2);
				myStmt.setString(5, "0.0");
				myStmt.setString(6,value3);
				myStmt.executeUpdate();	
			}
		}catch(Exception r1){
			r1.printStackTrace();
		}
	}
	

	//used for inserting into the BMS-R2 table in the database
	static void insertToDB_BMS_R2(Connection myConn, Scanner in1, Scanner in2, Scanner in3, int year){
		try{
			String line1,line2,line3, date, timeStamp;
			String value1,value2,value3;
			String insertDB = "INSERT INTO BMSR2"
					+"(TimeStamp, VarDate, Temperature, RelativeHumidity, CO_2, SensibleHeat) VALUES"
					+ "(?,?,?,?,?,?)";
			PreparedStatement myStmt = myConn.prepareStatement(insertDB);
			line1 = in1.nextLine();
			line2 = in2.nextLine();
			line3 = in3.nextLine();
			while(in1.hasNextLine()){
				line1 = in1.nextLine();
				line2 = in2.nextLine();
				line3 = in3.nextLine();
				String[] results1 = line1.split(",");
				String[] results2 = line2.split(",");
				String[] results3 = line3.split(",");
				results1[5] = time_adjustment(results1[5]);
				date = time_parse(results1[2] + "-" + results1[3] + "-" + String.valueOf(year)) ;
				timeStamp = results1[5] + ":" + time_parse(results1[6]);
				value1 = data_truncation(results1[10]);
				value2 = data_truncation(results2[10]);
				value3 = data_truncation(results3[10]);
				myStmt.setString(1,timeStamp);
				myStmt.setString(2,date);
				myStmt.setString(3,value1);
				myStmt.setString(4,value2);
				myStmt.setString(5, "0.0");
				myStmt.setString(6,value3);
				myStmt.executeUpdate();	
			}
		}catch(Exception r1){
			r1.printStackTrace();
		}
		
	}
	
	//used to print all data from the PV table into a file specified by the program
	static void printFromDB_PV(Connection myConn){
		//create a statement.
		try{
		Statement pvStmt = myConn.createStatement();
		BufferedWriter out = new BufferedWriter (new FileWriter("dataC.csv"));
		
		//make and SQL query for the PV table in the database.
		ResultSet pvResults = pvStmt.executeQuery("select * from PV");
		
		//write the columns of the database before the data is written out 
		out.write("TimeStep" 
				+ "," + "VarDate" 
				+ "," + "Pac" 
				+ "," + "Temperature"
				+ "," + "Vac"
				+ "\n");
		//process the results from the pv table in the database
		while(pvResults.next()){
			out.write(pvResults.getString("TimeStep") 
						+ "," + pvResults.getString("VarDate") 
						+ "," + pvResults.getString("Pac") 
						+ "," + pvResults.getString("Temperature")
						+ "," + pvResults.getString("Vac")
						+ "\n");
						
		}
		out.flush();
		out.close();
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
				pvResults = pvStmt.executeQuery("select * from BMSR1");
				break;
			case 2:
				out = new BufferedWriter (new FileWriter("BMSTwo.csv"));
				pvResults = pvStmt.executeQuery("select * from BMSR2");
				break;
			default :
				throw new Exception("not a valid room number");
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
							+ "," + pvResults.getString("VarDate") 
							+ "," + pvResults.getString("Temperature") 
							+ "," + pvResults.getString("RelativeHumidity")
							+ "," + pvResults.getString("CO_2")
							+ "," + pvResults.getString("SensibleHeat")
							+ "\n");
			}
				out.flush();
				out.close();
							
			
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
	
	//used to adjust time to military time.
	static String time_adjustment(String hour){
		String hour1 = hour.replaceAll("\\s","");
		try{
		int time = Integer.valueOf(hour1);
		time = time - 1;
		hour1 = String.valueOf(time);

		}catch(NumberFormatException x){
			x.printStackTrace();
		}
		return hour1;
	}
	//used to get rid of any excess white space and/or digits.
	static String time_parse(String minute){
	    String[] space = minute.split("\\.");
	    String result = space[0].replaceAll("\\s","");
	    if(result.equals("0") || result.equals("5")){
	    	String special = "0" + result;
	    	return special;
	    }
		return result;
	}
	
	//parses the date from the pv file name
	static String date_parse(String date){
		String[] something = date.split("\\.");
		String[] something1 = something[0].split("_");
		String[] something2 = something1[1].split("-");
		String something3 = something2[0] + "-" + something2[1] + "-" + something2[2];
		return something3;
	}
	
	static String data_truncation(String value){
		String extract1, extract2;
		String[] extract = value.split("\\.");
		if (extract.length == 2){
			extract1 = extract[1].substring(0,1);
		}else{
			extract1 = "0";
		}
		extract2 = extract[0] + "." + extract1;
		return extract2;
	}
	
	//deletes all data from the databases.
	static void delete(Connection myConn){
		try{
		Statement myStmt = myConn.createStatement();
		String delete = "delete from BMSR1 where VarDate = '7-29-2015'";
		String delete1 = "delete from BMSR2 where VarDate = '7-29-2015'";
		String delete2 = "delete from PV where VarDate = '2015-05-01'";	
		String delete3 = "delete from PV where VarDate = '2015-05-02'";	
		String delete4 = "delete from PV where VarDate = '2015-05-03'";	
		String delete5 = "delete from PV where VarDate = '2015-05-04'";	
		String delete6 = "delete from PV where VarDate = '2015-05-05'";	
		myStmt.executeUpdate(delete);
		myStmt.executeUpdate(delete1);
		myStmt.executeUpdate(delete2);
		myStmt.executeUpdate(delete3);
		myStmt.executeUpdate(delete4);
		myStmt.executeUpdate(delete5);
		myStmt.executeUpdate(delete6);
		
		}catch(Exception x){
			x.printStackTrace();
		}
	}
}
