origin = open('origin.md', 'r', encoding="utf-8")
result = open('result.md', 'r', encoding="utf-8")
merge = open('merge.md', 'w', encoding="utf-8")

paragraphStart = False

while True:
	lineO = origin.readline()
	lineR = result.readline()
	if not lineO:
		break;
	if lineR != '```\n' and lineR != '\n':
		merge.write('<div>\n<div class="result">\n\n\n')
		merge.write(lineR)
		merge.write('\n\n</div>\n<div class="origin">\n\n\n')
		merge.write(lineO)
		merge.write('\n\n</div>\n</div>\n')
	elif lineR == '```\n':
		paragraphStart = not paragraphStart
		if paragraphStart:
			merge.write('<div class="paragraphe">\n')
		else:
			merge.write('</div>\n')
	else:
		merge.write(lineO)
	

origin.close()
result.close()
merge.close()

# convert the generated md file to html with https://spec.commonmark.org/dingus/
