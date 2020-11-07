# pylint OVERVIEW

# pylint is a library which evaluates and makes a report of the code

# repoting includes and unnecessary semicolon, bad-white space, lines duplicated and no. of methods,
# functions, variables declared etc

# installing pylint :
#   pip install pylint

# for eg lets try to evaluate the following code in cmd

# I'm making an error intentionally to see what happens in a report

a = 2
b = 12

print(a)
print(B)

# in order to run pylint u have to run the following code:

# ( 3pylint.py -r y ) ===>> { -r y } is necessary

# (base) C:\siddhant work\VS CODE\PYTHON\8Errors&Exception_Handling>pylint 3pylint.py -r y

# after running this code u'll get the following report

# ************* Module 3pylint
# 3pylint.py:15:0: W0301: Unnecessary semicolon (unnecessary-semicolon)
# 3pylint.py:16:0: W0301: Unnecessary semicolon (unnecessary-semicolon)
# 3pylint.py:18:0: W0301: Unnecessary semicolon (unnecessary-semicolon)
# 3pylint.py:19:0: C0304: Final newline missing (missing-final-newline)
# 3pylint.py:19:0: W0301: Unnecessary semicolon (unnecessary-semicolon)
# 3pylint.py:1:0: C0103: Module name "3pylint" doesn't conform to snake_case naming style (invalid-name)
# 3pylint.py:1:0: C0114: Missing module docstring (missing-module-docstring)
# 3pylint.py:15:0: C0103: Constant name "a" doesn't conform to UPPER_CASE naming style (invalid-name)
# 3pylint.py:16:0: C0103: Constant name "b" doesn't conform to UPPER_CASE naming style (invalid-name)
# 3pylint.py:19:6: E0602: Undefined variable 'B' (undefined-variable)
#
#
# Report
# ======
# 4 statements analysed.
#
# Statistics by type
# ------------------
#
# +---------+-------+-----------+-----------+------------+---------+
# |type     |number |old number |difference |%documented |%badname |
# +=========+=======+===========+===========+============+=========+
# |module   |1      |NC         |NC         |0.00        |100.00   |
# +---------+-------+-----------+-----------+------------+---------+
# |class    |0      |NC         |NC         |0           |0        |
# +---------+-------+-----------+-----------+------------+---------+
# |method   |0      |NC         |NC         |0           |0        |
# +---------+-------+-----------+-----------+------------+---------+
# |function |0      |NC         |NC         |0           |0        |
# +---------+-------+-----------+-----------+------------+---------+
#
#
#
# Raw metrics
# -----------
#
# +----------+-------+------+---------+-----------+
# |type      |number |%     |previous |difference |
# +==========+=======+======+=========+===========+
# |code      |5      |23.81 |NC       |NC         |
# +----------+-------+------+---------+-----------+
# |docstring |0      |0.00  |NC       |NC         |
# +----------+-------+------+---------+-----------+
# |comment   |8      |38.10 |NC       |NC         |
# +----------+-------+------+---------+-----------+
# |empty     |8      |38.10 |NC       |NC         |
# +----------+-------+------+---------+-----------+
#
#
#
# Duplication
# -----------
#
# +-------------------------+------+---------+-----------+
# |                         |now   |previous |difference |
# +=========================+======+=========+===========+
# |nb duplicated lines      |0     |NC       |NC         |
# +-------------------------+------+---------+-----------+
# |percent duplicated lines |0.000 |NC       |NC         |
# +-------------------------+------+---------+-----------+
#
#
#
# Messages by category
# --------------------
#
# +-----------+-------+---------+-----------+
# |type       |number |previous |difference |
# +===========+=======+=========+===========+
# |convention |5      |NC       |NC         |
# +-----------+-------+---------+-----------+
# |refactor   |0      |NC       |NC         |
# +-----------+-------+---------+-----------+
# |warning    |4      |NC       |NC         |
# +-----------+-------+---------+-----------+
# |error      |1      |NC       |NC         |
# +-----------+-------+---------+-----------+
#
#
#
# Messages
# --------
#
# +-------------------------+------------+
# |message id               |occurrences |
# +=========================+============+
# |unnecessary-semicolon    |4           |
# +-------------------------+------------+
# |invalid-name             |3           |
# +-------------------------+------------+
# |undefined-variable       |1           |
# +-------------------------+------------+
# |missing-module-docstring |1           |
# +-------------------------+------------+
# |missing-final-newline    |1           |
# +-------------------------+------------+
#
#
#
#
# ----------------------------------------------------------------------
# Your code has been rated at -25.00/10 (previous run: -25.00/10, +0.00)
