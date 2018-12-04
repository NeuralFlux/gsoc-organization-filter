import pandas as pd

def make_table(inp_file):
	inp = open(inp_file, "r").read().splitlines()
	curr_line = []
	data = {'name': [], \
			'link': [], \
			'technologies': [], \
			'topics': []}
	first = True
	for line in inp:
		if line == '' and first == True:
			continue
		if line == '':
			data['name'].append(curr_line[0])
			data['link'].append(curr_line[1])
			data['technologies'].append(curr_line[2])
			data['topics'].append(curr_line[3])
			curr_line = []
			first = True
		else:
			if first:
				curr_line += line.split(', ')
			else:
				curr_line.append(line)
			first = False

	out = open("out.html", "w+")
	print('<table border="0|0" class="table-borderless gsoc-table">', file=out)
	print("<tr>", file=out)
	print("<th> Name </th>", file=out)
	print("<th> Technologies </th>", file=out)
	print("<th> Topics </th>", file=out)
	print("</tr>", file=out)

	for i in range(len(data['name'])):
		print("<tr>", file=out)
		print("<td> <a target='_blank' href=" + data['link'][i] + "> " + data['name'][i] + "</a> </td>", file=out)
		print("<td> " + data['technologies'][i] + " </td>", file=out)
		print("<td> " + data['topics'][i] + " </td>", file=out)
		print("</tr>", file=out)

	print("</table>", file=out)
	out.close()
