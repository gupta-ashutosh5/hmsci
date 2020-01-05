import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

def connectionOpen():
  return mysql.connector.connect(host="localhost", database="hmsci", user="root", password="root")

def isStudentPresent(enrollment_number):
  connection = connectionOpen()
  cursor = connection.cursor()
  sql = "SELECT stuid FROM hms_students WHERE stuEnrollment = %s"
  val = (enrollment_number, )
  cursor.execute(sql, val)
  student_id = int(cursor.fetchone()[0])
  if student_id is None:
    student_id = 0
  return student_id

def addStudent():
  print("---------- Enter student details -----------")
  student_name = input("Enter Student Name:")
  student_number = input("Enter Student Enrollment Number:")
  student_department = input("Enter Student department:")
  student_year = input("Enter Student year:")
  student_gender = input("Enter Student Gender")
  try:
    connection = connectionOpen()
    cursor = connection.cursor()
    sql = "INSERT INTO hms_students (stuEnrollment, stuName, stuGender, stuDept, stuYear) VALUES (%s, %s, %s, %s, %s)"
    val = (student_number, student_name, student_gender, student_department, student_year)
    cursor.execute(sql, val)
    connection.commit()
    print("Record inserted successfully into student table.")
  except mysql.connector.Error as error:
    connection.rollback()
    print("Failed inserting record into hms_students table".format(error))
  finally:
    if (connection.is_connected()):
      connection.close()
    print('MySQL connection is closed.')


def updateStudent():
  print("----------- Update Student details ------------")
  student_number = input("Enter Student Enrollment Number:")
  if isStudentPresent(student_number):
    flag = 'y'
    while (flag == 'y'):
      detail_choice = int(input("Enter the number of detail to update: \n1.Department \n2.Year \n3.Hostel \n4.Room \n5.Name"))
      if (detail_choice == 1):
        update_info = input("Enter the new department:")
        sql = "UPDATE hms_students SET stuDept = %s WHERE stuEnrollment = %s"
      elif (detail_choice == 2):
        update_info = input("Enter the new year: ")
        sql = "UPDATE hms_students SET stuYear = %s WHERE stuEnrollment = %s"
      elif (detail_choice == 3):
        update_info = input("Enter the new hostel:")
        sql = "UPDATE hms_students SET stuHostel = %s WHERE stuEnrollment = %s"
      elif (detail_choice == 4):
        update_info = int(input("Enter the new room:"))
        sql = "UPDATE hms_students SET stuRoom = %s WHERE stuEnrollment = %s"
      elif (detail_choice == 5):
        update_info = input("Enter the new name:")
        sql = "UPDATE hms_students SET stuName = %s WHERE stuEnrollment = %s"
      try:
        connection = connectionOpen()
        cursor = connection.cursor()
        val = (update_info, student_number)
        cursor.execute(sql, val)
        connection.commit()
        print("Record updated successfully.")
      except mysql.connector.Error as error:
        connection.rollback()
        print("Failed updating record into hms_students table".format(error))
      finally:
        if (connection.is_connected()):
          connection.close()
        print('MySQL connection is closed.')
      flag = input("Do you want to continue(y/n):")
  else:
    print("Student is not present.")

def showStudent():
  print("------------- Show Student Details ------------------")
  student_number = input("Enter Student Enrollment Number:")
  if isStudentPresent(student_number):
    try:
      connection = connectionOpen()
      cursor = connection.cursor()
      sql = "SELECT * FROM hms_students WHERE stuEnrollment = %s"
      val = (student_number,)
      cursor.execute(sql, val)
      student_details = cursor.fetchall()
      print("(Id, Enrollment number, Name, Gender, Department, Year, Hostel, Room)")
      for detail in student_details:
        print(detail)
    except mysql.connector.Error as error:
      connection.rollback()
      print("Failed fetching record from hms_students table".format(error))
    finally:
      if (connection.is_connected()):
        connection.close()
      print('MySQL connection is closed.')
  else:
    print("Student is not present.")

def showAllStudents():
  print("------------- Show Student Details ------------------")
  try:
    connection = connectionOpen()
    cursor = connection.cursor()
    sql = "SELECT * FROM hms_students"
    cursor.execute(sql)
    student_details = cursor.fetchall()
    print("(Id, Enrollment number, Name, Gender, Department, Year, Hostel, Room)")
    for detail in student_details:
      print(detail)
  except mysql.connector.Error as error:
    print("Failed fetching record from hms_students table".format(error))
  finally:
    if (connection.is_connected()):
      connection.close()
    print('MySQL connection is closed.')


def addHostel():
  print("---------- Enter hostel details -----------")
  hostel_name = input("Enter Hostel Name:")
  hostel_warden = input("Enter Hostel Warden Name:")
  hostel_gender = ''
  while (hostel_gender != "M" and hostel_gender != "F"):
    hostel_gender = input("Enter Hostel Type(M/F):")
    print(hostel_gender)
    if (hostel_gender != "M" and hostel_gender != "F"):
      print("Wrong entry. Please provide Hostel Type as M/F.")
  try:
    connection = connectionOpen()
    cursor = connection.cursor()
    sql = "INSERT INTO hms_hostel (hostelName, hostelWarden, hostelGender) VALUES (%s, %s, %s)"
    val = (hostel_name, hostel_warden, hostel_gender)
    cursor.execute(sql, val)
    connection.commit()
    print("Record inserted successfully into hostel table.")
  except mysql.connector.Error as error:
    connection.rollback()
    print("Failed inserting record into hms_hostel table".format(error))
  finally:
    if (connection.is_connected()):
      connection.close()
    print('MySQL connection is closed.')

def addRoomsInHostel(hostel_name):
  print("--------- Add rooms --------")
  room_count = int(input("Enter number of rooms in the hostel"))
  try:
    connection = connectionOpen()
    cursor = connection.cursor()
    sql = "SELECT hostelId from hms_hostel WHERE hostelName = %s"
    val = (hostel_name, )
    cursor.execute(sql, val)
    hostel_id = int(cursor.fetchone()[0])
    for x in range(room_count):
      sql = "INSERT INTO hms_hostel_room_map (hostelid, roomnumbers) values (%s, %s)"
      val = (hostel_id, int(x+1))
      cursor.execute(sql, val)
      connection.commit()
      print("Rooms are entered successfully.")
  except mysql.connector.Error as error:
    connection.rollback()
    print("Failed inserting record into hms_hostel_room_map table".format(error))
  finally:
    if (connection.is_connected()):
      connection.close()
    print('MySQL connection is closed.')

def showAllHostels():
  print("-------- Hostels List ------------")
  try:
    connection = connectionOpen()
    cursor = connection.cursor()
    sql = "SELECT * FROM hms_hostel"
    cursor.execute(sql)
    hostel_details = cursor.fetchall()
    print("(Id, Name, Warden, Type)")
    for detail in hostel_details:
      print(detail)
  except mysql.connector.Error as error:
    print("Failed fetching record from hms_hostel table".format(error))
  finally:
    if (connection.is_connected()):
      connection.close()
    print('MySQL connection is closed.')

def allocateRoom(enrollment_number):
  print("---------- Allocate Room ------------")
  print("------- Fetching Hostels for student ---------")
  try:
    connection = connectionOpen()
    cursor = connection.cursor()
    sql = "SELECT stuGender FROM hms_students WHERE stuEnrollment = %s"
    val = (enrollment_number, )
    cursor.execute(sql, val)
    student_gender = cursor.fetchone()
    sql = "SELECT hostelName FROM hms_hostel WHERE hostelGender = %s"
    val = (student_gender)
    cursor.execute(sql, val)
    hostel_names = cursor.fetchall()
    if len(hostel_names) == 0 :
      print('No hostels are available.')
    else:
      print('Select Hostel from below List')
      hostel_list = []
      for hostel in hostel_names:
        print(hostel[0])
        hostel_list.append(hostel[0])
      flag = 1
      while(flag):
        hostel_name = input('Enter hostel choice:')
        if (hostel_name not in hostel_list):
          print("Please enter correct hostel name.")
        else:
          flag = 0
          hostel_id = 0
          print("Select rooms from below")
          sql = "SELECT hrm.hostelid, hrm.roomnumbers FROM hms_hostel_room_map hrm INNER JOIN hms_hostel h ON h.hostelId = hrm.hostelid WHERE h.hostelName = %s AND hrm.available = 0"
          val = (hostel_name, )
          cursor.execute(sql, val)
          hostel_rooms = cursor.fetchall()
          if len(hostel_rooms) == 0:
            print("No rooms available")
          else:
            room_list = []
            for room in hostel_rooms:
              print(room[1])
              room_list.append(room[1])
              hostel_id = room[0]
            flag_room = 1
            while(flag_room):
              hostel_room = int(input("Enter the room choice"))
              if (hostel_room not in room_list):
                print("Please enter correct room number.")
              else:
                flag_room = 0
                sql = "UPDATE hms_hostel_room_map SET available = 1 WHERE hostelid = %s AND roomnumbers = %s"
                val = (hostel_id, hostel_room)
                cursor.execute(sql, val)
                sql = "UPDATE hms_students SET stuHostel=%s, stuRoom=%s WHERE stuEnrollment = %s"
                val = (hostel_name, hostel_room, enrollment_number)
                cursor.execute(sql, val)
                connection.commit()
                print("Room successfully allocated.")
  except mysql.connector.Error as error:
    print("Failed allocating room to the student".format(error))
  finally:
    if (connection.is_connected()):
      connection.close()
    print('MySQL connection is closed.')

def main():
  while (1):
    print("1.Enter Student Data.")
    print("2.Update Student Data.")
    print("3.Show Student Data.")
    print("4.Show All Student Data.")
    print("5.Add Hostel Data.")
    print("6.Show Hostel List.")
    print("7.Add rooms in hostel.")
    print("8.Allocate room to Student.")
    print("9.EXIT")

    b = int(input("\nEnter your choice:"))
    if (b == 1):
      addStudent()

    elif (b == 2):
      updateStudent()

    elif (b == 3):
      showStudent()

    elif (b == 4):
      showAllStudents()

    elif (b == 5):
      addHostel()

    elif (b == 6):
      showAllHostels()

    elif (b == 7):
      flag = 1
      while(flag):
        showAllHostels()
        hostel_name = input("Enter hostel name from above list:")
        if not hostel_name:
          print("Please provide hostel name.")
        else:
          flag = 0
          addRoomsInHostel(hostel_name)

    elif (b == 8):
      student_number = input("Enter Student Enrollment Number:")
      if student_number is None:
        print("Please provide enrollment number")
      else:
        if isStudentPresent(student_number):
          allocateRoom(student_number)
        else:
          print("Student is not present.")

    else:
      quit()


main()
