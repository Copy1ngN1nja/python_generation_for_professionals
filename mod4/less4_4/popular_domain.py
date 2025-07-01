import csv

with open('data.csv', mode='r') as input_file, open('domain_usage.csv', mode='w') as output_file:
    csv_reader = csv.DictReader(input_file)
    csv_writer = csv.writer(output_file)
    csv_writer.writerow(['domain', 'count'])
    popular_domains = {}
    for d in csv_reader:
        _, domain = d['email'].split('@')
        popular_domains[domain] = popular_domains.get(domain, 0) + 1
    for domain, count in sorted(popular_domains.items(), key=lambda x: (x[1], x[0])):
        csv_writer.writerow([domain, count])
