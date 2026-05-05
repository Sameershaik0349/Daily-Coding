from django.shortcuts import render

# http respose ==> it create new webpage and display our content

from django.http import HttpResponse

# def first(reqest):
#     return HttpResponse("<h1 style='color:green'>my django code</h1>")


# def even(reqest):
#     l=[]
#     for i in range(10,20):
#         if i%2==0:
#             l.append(i)
#     return HttpResponse(l)



# def employee(reqest):
#     data={'emp_name':'anjali','emp_id':1001,'emp_sal':3000}
#     return HttpResponse(f"<table><tr><th>EmPNAME</th><th>EMP_ID</th><th>EMP_SAL</th></tr><tr><td>{data['emp_name']}</td><td>{data['emp_id']}</td><td>{data['emp_sal']}</td></tr></table>")


employees = [
    {"emp_name": "Anjali", "emp_id": 1001, "emp_sal": 3000},
    {"emp_name": "Ravi", "emp_id": 1002, "emp_sal": 4500},
    {"emp_name": "Sneha", "emp_id": 1003, "emp_sal": 5000},
    {"emp_name": "Kiran", "emp_id": 1004, "emp_sal": 3500}
]

def employee(reqests):
    table ="""
            <table> <tr>
                    <th>EMPNAME</th>
                    <th>EMPID</th>
                    <th>EMPSAL</th>
                    </tr>
                """
    for x in employees:
        table+=f"""
                <tr>
                <td>{x['emp_name']}</td>
                <td>{x['emp_id']}</td>
                <td>{x['emp_sal']}</td>
                </tr>"""
    table+="""</table>"""

    return HttpResponse(table)
        
# caluculator

# def cal(re,val1,val2):
#     return HttpResponse(f'<h1>{val1} + {val2}={val1+val2}</h1>')


# def emp(r,emp_name,emp_id,emp_sal):
#     return HttpResponse(f"""
#                             <table><tr>
#                                     <th>EMPName</th>
#                                     <th>EMPID</th>
#                                     <th>EMPSAL</th>
#                                     </tr>   
#                                     <tr>
#                                         <td>{emp_name}</td>
#                                         <td>{emp_id}</td>
#                                         <td>{emp_sal}</td>
#                                         </tr></table>""")



def even(reqest,val):
    if val%2==0:
        return HttpResponse(f"""<h1 style='color:green'>{val}</h1>its even""")
    else:
        return HttpResponse(f"""<h1 style='color:red'>{val}</h1>its odd""")