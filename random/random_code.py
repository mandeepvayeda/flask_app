from flask import Flask, render_template

app = Flask(__name__)

f = open("customerdata.txt", "r")
mylist = list(f)
my_list = [line.rstrip('\n') for line in mylist]
li = []
li_once = {}
lis = []
labels = []
values = []
count = 0
amount = 0
c1 = c2 = c3 = c4 = c = 0
for x in my_list:
	li.append(list(x.split(",")))

length = len(li)

for i in range(1, 28):
	labels.append(li[i][0])
	values.append(li[i][3])

for i in range(1, length - 1):
		count += 1
		amount += int(li[i][3])
		if li[i][2] not in li_once:
			li_once[li[i][2]] = 1
		else:
			li_once[li[i][2]] += 1
for j in li_once:
	if li_once[j] == 1:
		lis.append(j)
	if li_once[j] == 1:
		c1 += 1
	elif li_once[j] == 2:
		c2 += 1
	elif li_once[j] == 3:
		c3 += 1
	elif li_once[j] == 4:
		c4 += 4
	else:
		c += 1

@app.route("/")
def h():
	l = ", ".join(lis)
	return render_template('index.html', c = c, c1 = c1, c2 = c2, c3 = c3, c4 = c4, count = count, amount = amount, lis = l, labels = labels, values = values)

app.run(debug = True)
