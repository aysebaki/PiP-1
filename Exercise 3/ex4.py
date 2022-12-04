def parse_list(in_string):
    var = ''
    new_list = list()
    for i,val in enumerate(in_string):
        if not val.isspace():
            var += val
        if val.isspace() or len(in_string)-1 == i:
            new_list.append(int(var))
            var = ''
    return new_list

def sum_matrix_columns(matrix):
    sums_matrix = [0] * max_matrix_length(matrix)
    for i, vals in enumerate(matrix):
        for i2, vals2 in enumerate(vals):
            sums_matrix[i2] += vals2
    return list(sums_matrix)

def expand_matrix(matrix):
    max_el = max_matrix_length(matrix)
    for vals in matrix:
        while(len(vals) != max_el):
            vals.append(0)
    return matrix

def sum_matrix_rows(matrix):
    sums_matrix = list()
    for vals in matrix:
        sum_vals = 0
        for inner_vals in vals:
            sum_vals += inner_vals
        sums_matrix.append(sum_vals)
    return sums_matrix

def max_matrix_length(matrix):
    max_length_l = 0
    for val in matrix:
        if len(val) > max_length_l:
            max_length_l = len(val)
    return max_length_l

outer_list = list()
switch = True

while switch:
    row_in = input("Enter row: ")
    if(not "x" in row_in):
        outer_list.append(parse_list(row_in))
    else:
        switch = False
outer_list = expand_matrix(outer_list)

print("""%s
row sums: %s
column sums: %s
total sum: %s""" %(outer_list, sum_matrix_rows(outer_list), sum_matrix_columns(outer_list), sum(b for b in sum_matrix_rows(outer_list))))