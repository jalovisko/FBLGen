from parfunlib.topologies.diamond import diamond_heterogeneous_lattice

# USER INPUT

unit_cell_size = 10
min_strut_diameter = 1
max_strut_diameter = 1
min_node_diameter = 1.2
max_node_diameter = 1.2
Nx = 1
Ny = 1
Nz = 1

# END USER INPUT

# Register our custom plugin before use.
cq.Workplane.diamond_heterogeneous_lattice = diamond_heterogeneous_lattice

#result = unit_cell(unit_cell_size, strut_radius)
result = diamond_heterogeneous_lattice(unit_cell_size,
                                    min_strut_diameter, 
                                    max_strut_diameter,
                                    min_node_diameter,
                                    max_node_diameter,
                                    Nx, Ny, Nz
                                    #rule = 'sin'
                                    )