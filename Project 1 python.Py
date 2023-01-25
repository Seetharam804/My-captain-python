# My-captain-python
import csv
def write_into_csv(info_list):
    with open("Student_info.csv",'a',newline= '\n') as csv_file:
        writer = csv.writer(csv_file)

        writer.writerow("Name Age Contact_number E-mail_id")
        writer.writerow(info_list)
        

if __name__ == '__main__':
    condition=True
    student_num=1
    while(condition):
        student_info=input("Enter the stundent information for student #{}  in following way Name Age contact_number E-Mail_id :". format(student_num))
        student_info_list=student_info.split(' ')
        print("\n","The entered information is- \n Name: {} \n Age: {} \n Contact_number: {} \n Email_id: {}". format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))
        choice_check=input("Is this entered  info is correct (yes/no):")
        if choice_check== "yes":
            write_into_csv(student_info_list)
            condition_check=input("Enter (yes/no) if you want to emnter another studemt details:")
            if condition_check == "yes":
                condition=True
                student_num+=1
            else:
                condition = False
        else:
            print("\n Please re-enter the value!")
        
        
