__all__ = ['Hex3D']

from mbuild.lattice import Lattice
from mbuild.recipes.lattice_cubic import compound_dict_expansion


def spacing_error(lattice_spacings):
    """Check that the inputted lattice spacings are a list of two.

    spacing_error will determine if the user inputted a list of 2 values
    that can be converted to floats. These values represent the a and c
    lattice edges. In a hexagonal cell, a and b are equivalent, while c is
    not.

    Parameters:
    -----------
    lattice_spacings: list, length=2, required
        Edge lengths of the hexagonal cell.
    """
    if not isinstance(lattice_spacings, list):
        raise TypeError('Lattice spacings should be a list '
                        'of at least 2 values.')
    else:
        if len(lattice_spacings) != 2:
            raise ValueError('Must supply 2 values for lattice '
                             'spacings.')
        else:
            for space in lattice_spacings:
                try:
                    float(space)
                except ValueError:
                    raise ValueError('Cannot convert lattice spacings to '
                                     'type \'float\'.')


def expand_spacings_3d_hex(lattice_spacings):
    """Convert single lattice spacing to list of lattice spacings.

    expand_spacings_3d_hex expands the list of inputted lattice spacings
    to their proper 3d notation. For the case of a hexagonal cell, the first
    value is a and b, while the second value is c.

    Parameters:
    -----------
    lattice_spacings: list, length=2, required
        Edge lengths of the hexagonal cell.
    """
    a_edge = float(lattice_spacings[0])
    c_edge = float(lattice_spacings[1])
    return [a_edge, a_edge, c_edge]


class Hex3D(Lattice):
    """Hexagonal 3D lattice system.

    Attributes
    ----------
    dimension : int, default=3
        Dimension of the system of interest.
    lattice_vectors : numpy array, shape=(dimension, dimension), optional
        Vectors that define edges of the hexagonal system.
    lattice_spacings : list-like, shape=2, required, default=None
        Lengths of unit cell edges.
    basis_atoms : dictionary, shape={'id':[list of atom positions]},
    default=[0, 0, 0]
        Location of all basis compounds in unit cell.
    angles : list-like,  shape=(dimension,), default=[90,90,120]
        Interplanar angles describing unit cell.

    HEX_3D Defaults
    ---------------------
    dimension : 3
    angles = [90, 90, 120]
    basis_atoms : 'A', [[0, 0, 0]]
    """

    dimension = 3
    angles = [90, 90, 120]
    basis_atoms = {'A': [[0, 0, 0]]}

    def __init__(self, lattice_spacings):
        spacing_error(lattice_spacings=lattice_spacings)

        super().__init__(lattice_spacings=expand_spacings_3d_hex(lattice_spacings),
                         dimension=self.dimension,
                         basis_atoms=self.basis_atoms,
                         angles=self.angles)

    def populate(self, compound_dict=None, x=1, y=1, z=1):
        compound_dict = compound_dict_expansion(self.basis_atoms,
                                                compound_dict, 1)
        return super().populate(compound_dict=compound_dict,
                                x=x,
                                y=y,
                                z=z)
