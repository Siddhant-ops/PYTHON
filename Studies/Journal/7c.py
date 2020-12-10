# Write a program to create a file and count total number of lines written in it.

sample_lines = [
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n",
    "Euismod quis viverra nibh cras.\n",
    "Amet luctus venenatis lectus magna fringilla urna porttitor.\n",
    "Ornare aenean euismod elementum nisi quis eleifend quam.\n",
    "Aenean et tortor at risus viverra adipiscing at.\n",
    "Est velit egestas dui id ornare arcu odio ut sem.\n",
    "Convallis posuere morbi leo urna molestie at elementum.\n",
    "Donec massa sapien faucibus et molestie ac feugiat sed lectus.\n",
    "Amet tellus cras adipiscing enim eu turpis.\n",
    "Massa tempor nec feugiat nisl pretium fusce id velit ut.\n",
    "Dolor sit amet consectetur adipiscing elit ut aliquam purus sit.\n",
    "Platea dictumst vestibulum rhoncus est pellentesque.\n",
    "Auctor neque vitae tempus quam pellentesque.\n",
    "Nisi lacus sed viverra tellus.\n",
    "Nisi porta lorem mollis aliquam ut porttitor leo a diam.",
]

with open("sample_text.txt", "w") as f:
    f.writelines(sample_lines)

with open("sample_text.txt", "r") as f:
    lines = f.readlines()
    print(len(lines))
