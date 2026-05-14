from django.shortcuts import render
from app_5.models import employee
import MySQLdb

def user(request):

    data = ""

    if request.method == "POST":

        emp_name= request.POST.get("emp_name")
        emp_pass= request.POST.get("emp_pass")

        # employee.objects.create(
        #     emp_name=name,
        #     emp_pass=password
        # )

        # data = f"""
        # <table border="1">
        #     <tr>
        #         <th>username</th>
        #         <th>password</th>
        #     </tr>

        #     <tr>
        #         <td>{name}</td>
        #         <td>{password}</td>
        #     </tr>
        # </table>
        # """

        con=MySQLdb.connect(user='root',
                            host='localhost',
                            database= '',
                            password='')
        cursor=con.cursor()
        sql_table="Create table IF NOT EXISTS(emp_name varchar(20),emp_pass int)"
        cursor.execute(sql_table)
        insert_data="insert into sql_table values(f"{emp_name}","{emp_pass}")
        

        employee.objects.create(
            emp_name=emp_name,
            emp_pass=emp_pass
        )
    data=employee.objects.all()

    return render(request, "Html/app_5.html", {"data": data})