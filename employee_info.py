import sys
if len(sys.argv) != 5:
  print ("usage: python employee_details_jen.py <id> <name> <salary> <experience>")
  sys.exit(1)

id = sys.argv[0]
name = sys.argv[1]
salary = sys.argv[2]
experience = sys.argv[3]

print("employee id: ", id)
print("employee name: ", name)
print("employee salary: ", salary)
print("employee experience: ", experience)


