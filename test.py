from nl_parser import nl_parser

if __name__ == '__main__':
    parser = nl_parser()
    parser.read_netlist("test.v")

    for design in parser.designs:
        design.print_this()