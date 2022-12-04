lowercase = []
uppercase = []
other = []
unique = []
sent = str(input("Enter string: "))

for element in sent:
    if element not in unique:
        unique.append(element)
    if element.isupper() is True:
        uppercase.append(element)
        continue
    if element.islower() is True:
        lowercase.append(element)
        continue
    else:
        other.append(element)

print(f"lowercase: {lowercase}\n"
      f"uppercase: {uppercase}\n"
      f"other: {other}\n"
      f"unique: {unique}")
