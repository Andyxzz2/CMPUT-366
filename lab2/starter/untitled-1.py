file = open('top95.txt', 'r')
problems = file.readlines()

for p in problems:
    # Read problem from string
    g = Grid()
    g.read_file(p)

    # Print the grid on the screen
    print('Puzzle')
    g.print()

    # Print the domains of all variables
    print('Domains of Variables')
    g.print_domains()
    print()

    # Iterate over domain values
    for i in range(g.get_width()):
        for j in range(g.get_width()):

            print('Domain of ', i, j, ': ', g.get_cells()[i][j])

            for d in g.get_cells()[i][j]:
                print(d, end=' ')
            print()

    # Make a copy of a grid
    copy_g = g.copy()

    print('Copy (copy_g): ')
    copy_g.print()
    print()

    print('Original (g): ')
    g.print()
    print()

    # Removing 2 from the domain of the variable in the first row and second column
    copy_g.get_cells()[0][1] = copy_g.get_cells()[0][1].replace('2', '')

    # The domain (0, 1) of copy_g shouldn't have 2 (first list, second element)
    print('copy_g')
    copy_g.print_domains()
    print()

    # The domain of variable g shouldn't have changed though
    print('g')
    g.print_domains()
    print()

    # Instance of AC3 Object
    ac3 = AC3()

    # Making all variables in the first row arc consistent with (0, 0), whose value is 4
    variables_assigned, failure = ac3.remove_domain_row(g, 0, 0)

    # The domain of all variables in the first row must not have 4
    print('Removed all 4s from the first row')
    g.print_domains()

    # variables_assigned contains all variables whose domain reduced to size 1 in the remove_domain_row opeation
    print('Variables that were assigned by remove_domain_row: ', variables_assigned)

    # failture returns True if any of the variables in the row were reduced to size 0
    print('Failure: ', failure)
    print()

    # Making all variables in the first column arc consistent with (0, 0), whose value is 4
    variables_assigned, failure = ac3.remove_domain_column(g, 0, 0)

    # The domain of all variables in the first column must not have 4
    print('Removed all 4s from the first column')
    g.print_domains()
    print()

    # Making all variables in the first unit arc consistent with (0, 0), whose value is 4
    variables_assigned, failure = ac3.remove_domain_unit(g, 0, 0)

    # The domain of all variables in the first column must not have 4
    print('Removed all 4s from the first unit')
    g.print_domains()
    print()