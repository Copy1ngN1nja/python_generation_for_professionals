import csv

with open('salary_data.csv', mode='r') as file:
    csv_reader = csv.reader(file, delimiter=';')
    company_salaries = {}
    for row in list(csv_reader)[1:]:
        company, salary = row
        salary = int(salary)
        if company not in company_salaries:
            company_salaries[company] = (0, 0)
        company_salaries[company] = (company_salaries[company][0] + salary, company_salaries[company][1] + 1)
    average_salaries = {company: total / count for company, (total, count) in company_salaries.items()}
    for company, avg_salary in sorted(average_salaries.items(), key=lambda x: (x[1], x[0])):
        print(company)
        