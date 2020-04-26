import re

sample_string = "+1AB+2CBA+1B"

results = re.findall(r"\+[0-9]+[ABCD]+", sample_string)

a = re.search(r"\+[0-9]+[ABCD]+", sample_string)
print(a.groups())

for i in range(len(results)):
	tmp = re.match(r"\+([0-9]+)", results[i])
	length = tmp.group(1);
	pattern = r"\+([0-9]+)[ABCD]{0," +  str(length) + "}"
	tmp = re.match(pattern, results[i])
	results[i] = tmp.group(0)

print("Results: ")
print(results)

