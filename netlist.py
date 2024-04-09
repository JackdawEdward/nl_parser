
class t_port:

    def __init__(self):
        self.name = "default"
        self.direction = "input"
        self.wire_type = "wire"
        self.msb = 0
        self.lsb = 0
        # prot conn
        self.ports = {}

    def new_port(self, name, direction="input", wire_type="wire", msb=0, lsb=0):
        self.direction = direction
        self.msb = msb
        self.lsb = lsb
        self.name = name
        if msb != 0:
            for i in range(lsb, msb+1):
                self.ports["{}[{}]".format(self.name, i)] = []
        else:
            self.ports["{}".format(self.name)] = []

    def add_conn(self, port, inst, pin):
        if port not in self.ports:
            self.ports[port] = []
        self.ports[port].append([inst, pin])

    def print_this(self):
        if self.msb != 0:
            print("Port {}: {} {} [{}:{}]".format(self.name, self.direction, self.wire_type, self.msb, self.lsb))
            for port in self.ports:
                for c in self.ports[port]:
                    print("   {} {} {}".format(port, c[0], c[1]))
        else:
            print("Port {}: {} {} ".format(self.name, self.direction, self.wire_type))
            for c in self.ports[port]:
                print("   {} {}".format(port, c[0], c[1]))

        
class t_wire:
    def __init__(self, name):
        self.name = name
        self.conn = [] #a wire can connect to multi term

    def add_conn(self, inst, pin):
        self.conn.append([inst, pin])

    def print_this(self):
        print("Wire {}".format(self.name))
        for c in self.conn:
            if c == None:
                print("    {} {}".format("port", c[1]))
            else:
                print("    {} {}".format(c[0], c[1]))

        
class t_inst:
    def __init__(self, name):
        self.name = name        
        self.module_name = "default"
        self.port_map = [] #.A(a), .B(b), ...

    def new_inst(self, module_name, name):
        self.module_name = module_name
        self.name = name

    def add_port_map(self, port_name, wire_name):
        self.port_map.append([port_name, wire_name])

    def add_port_maps(self, port_map):
        for port_pairs in port_map:
            self.port_map.append(port_pairs)

    def print_this(self):
        print("Inst {}: {}".format(self.name, self.module_name))
        print("Port maps:")
        for m in self.port_map:
            print("    .{}({})".format(m[0], m[1]))
            
class t_module:

    def __init__(self, name):
        self.name = name
        self.ports = []
        self.wires = []
        self.insts = []

    def add_port(self, port):
        self.ports.append(port)

    def add_wire(self, wire):
        self.wires.append(wire)

    def add_inst(self, inst):
        self.insts.append(inst)

    def exist_wire(self, name):
        for wire in self.wires:
            if wire.name == name:
                return True
        return False

    def find_wire(self, name):
        for i in range(len(self.wires)):
            if self.wires[i].name == name:
                return i
        return None
    # port
    def exist_port(self, name):
        for port in self.ports:
            for bit_port in port.ports:
                if bit_port == name:
                    return True
        return False

    def find_port(self, name):
        for i in range(len(self.ports)):
            for bit_port in self.ports[i].ports:
                if bit_port == name:
                    return True
        return False

    def print_this(self):
        print("Module {}".format(self.name))
        for port in self.ports:
            port.print_this()
        for wire in self.wires:
            wire.print_this()
        for inst in self.insts:
            inst.print_this()

    def get_ports(self):
        for port in self.ports:
            port.print_this()

    def get_wires(self):
        for wire in self.wires:
            wire.print_this()

    def get_insts(self):
        for inst in self.insts:
            inst.print_this()
            
        
    
