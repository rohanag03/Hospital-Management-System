import pymysql

conn=pymysql.connect(host="localhost", user="root", password="password", database="database_name")
c=conn.cursor()

try:
    c.execute('''CREATE TABLE `patient` (
      `id` int(11) PRIMARY KEY AUTO_INCREMENT,
      `name` char(25) ,
      `gender` char(1) ,
      `age` int(3) ,
      `date` varchar(20) ,
      `contact` bigint(20) ,
      `address` varchar(50) ,
      `email` varchar(30) ,
      `Doctor` char(30) ,
      `department` char(20) ,
      `category` char(20) ,
      `room_type` char(25),
      `room_no` int(5),
      `room_price` int(10));''')
    print("Patient Table Created")
except:
    print("Patient Table can't be created")

try:
    c.execute('''CREATE TABLE `employee` (
      `id` int(11) PRIMARY KEY AUTO_INCREMENT,
      `name` char(25) ,
      `gender` char(1) ,
      `age` int(3) ,
      `date_of_joining` date ,
      `contact` bigint(20) ,
      `address` varchar(50) ,
      `email` varchar(30) ,
      `salary` char(30) ,
      `department` char(20) ,
      `experience` int(5));''')
    print("Patient Table Created")
except:
    print("Patient Table can't be created")

try:
    c.execute('''CREATE TABLE appointments (
      app_id int(11) PRIMARY KEY AUTO_INCREMENT,
      name char(25) ,
      gender char(1) ,
      age int(3) ,
      contact bigint(20) ,
      queue_no int(4),
      app_date date ,
      app_time time,
      doctor char(25),
      department char(20),
      c_fee int(5));''')
    print("Appointments Table Created")
except:
    print("Appointments Table can't be created")

try:
    c.execute('''CREATE TABLE sur_test (
      id int(11) ,
      `test/surgery` char(25),
      `date_sur/test` date,
      cost int(10));''')
    print("sur_test Table Created")
except:
    print("sur_test Table can't be created")

    try:
    c.execute('''CREATE TABLE bill (
      id int(11) ,
      name char(25),
      date_of_admission date,
      date_of_discharge date,
      ins_category char(30),
      total float);''')
    print("Bill Table Created")
except:
    print("Bill Table can't be created")
