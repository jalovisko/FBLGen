#import cadquery as cq
from parfunlib.commons import eachpointAdaptive
from parfunlib.topologies.fcc import unit_cell
#from parfunlib.topologies.martensite import fcc_martensite

# USER INPUT

unit_cell_size = 10
strut_diameter = 1
node_diameter = 1.1
# Nx = 2
Ny = 1
Nz = 7
uc_break = 3

# END USER INPUT

# Register our custom plugins before use.
cq.Workplane.eachpointAdaptive = eachpointAdaptive
cq.Workplane.unit_cell = unit_cell

def fcc_martensite(unit_cell_size: float,
                    strut_diameter: float,
                    node_diameter: float,
                    # Nx: int,
                    Ny: int,
                    Nz: int,
                    uc_break: int):
    if uc_break < 1:
        raise ValueError('The value of the beginning of the break should larger than 1')
    UC_pnts = []
    Nx = Nz + uc_break - 1
    for i in range(Nx):
        for j in range(Ny):
            for k in range(Nz):
                if k - 1 < i:
                    UC_pnts.append(
                        (i * unit_cell_size,
                        j * unit_cell_size,
                        k * unit_cell_size))
    print("Datapoints generated")
    result = cq.Workplane().tag('base')
    result = result.pushPoints(UC_pnts)
    unit_cell_params = []
    for i in range(Nx * Ny):
        for j in range(Nz):
            unit_cell_params.append({"unit_cell_size": unit_cell_size,
                "strut_radius": strut_diameter * 0.5,
                "node_diameter": node_diameter,
                "type": 'fcc'})
    result = result.eachpointAdaptive(unit_cell,
                                        callback_extra_args = unit_cell_params,
                                        useLocalCoords = True)
    print("The lattice is generated")
    return result

result = fcc_martensite(unit_cell_size,
                        strut_diameter,
                        node_diameter,
                        Ny, Nz, uc_break)