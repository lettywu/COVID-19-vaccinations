print("<table id=\"vaccine\" class=\"table table-bordered\"")

print("<thead>")
print("<tr>")
print("<th>County</th>")
print("<th>Vaccines to be Distributed</th>")
print("<th>Estimated Vaccines Administered</th>")
print("<th>Population</th>")
print("<th>People Per Vaccines Administered</th>")
print("</tr>")
print("</thead>")
print("<tbody>")

infile = open("../clean_data/California_2021_02_07.csv", "r")

for i in infile:
    row = i.split(",")
    county = row[0]
    vaccines_dist = row[3]
    vaccines_admin = row[4]
    population = row[5]
    people_vaccines = row[7]
    
    print("<tr>")
    print("<td>%s</td>" % county)
    print("<td>%s</td>" % vaccines_dist)
    print("<td>%s</td>" % vaccines_admin)
    print("<td>%s</td>" % population)
    print("<td>%s</td>" % people_vaccines)
    print("</tr>")

print("</tbody>")
print("</table>")
