__all__ = ['RhombohedralPrim', 'RhombohedralConventional']

from mbuild.lattice import Lattice
from mbuild.recipes.lattice_cubic import compound_dict_expansion

def input_error_rhombohedral(lattice_spacings, angles):
    """Check for input errors and incorrect monoclinic information.

    input_error_monoclinic ensures that the lattice spacings and angles
    inputted by the user are correct for the monoclinic bravais lattice
    definitions.

    Parameters:
    -----------
    lattice_spacings: list, length=3, float,
        Edge lengths of the lattice unit cell.
    angles: float

    """
    if isinstance(lattice_spacings, list):
        if len(lattice_spacings) == 3:
            if lattice_spacings[0] != lattice_spacings[2]:
                pass
            else:
                raise ValueError('Incorrect values for lattice spacings. '
                                 'Bravais monoclinic lattices cannot have '
                                 'a == c.')
        else:
            raise ValueError('Incorrect amount of lattice spacings, 3 '
                             'expected, {} passed.'
                             .format(len(lattice_spacings)))
    else:
        raise TypeError('lattice_spacings incorrect type, {} was provided, '
                        'expected list.'.format(type(lattice_spacings)))

    try:
        float(angles)
    except ValueError:
        raise ValueError('Cannot convert angle to float, ensure that angle is '
                         'a single value that represents the interplanar '
                         'angle beta.')

    if angles != 90:
        pass
    else:
        raise ValueError('Incorrect interplanar angle value for beta. '
                         'Beta cannot be equal to 90.')
    return [90, angles, 90]

class Rhombohedral(Lattice):
    """Rhombohedral 3D lattice system.

    Attributes
    ----------
    dimension : int, default=3
        Dimension of the system of interest.
    lattice_vectors : numpy array, shape=(dimension, dimension), optional
        Vectors that define edges of the Rhombohedral system.
    lattice_spacings : float, size=1, required, default=None
        Lengths of unit cell edges.
    basis_atoms : dictionary, shape={'id':[list of atom positions]},
    default=[0, 0, 0]
        Location of all basis compounds in unit cell.
    angles : float,  size=1, required
        Interplanar angles describing unit cell.

    Rhombohedral Defaults
    ---------------------
    dimension : 3
    alpha = beta = gamma != 90
    a = b = c
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
                         lattice_vectors=self.lattice_vectors)

    def populate(self, compound_dict=None, x=1, y=1, z=1):
        compound_dict = compound_dict_expansion(self.basis_atoms,
                                                compound_dict, 1)
        return super().populate(compound_dict=compound_dict,
                                x=x,
                                y=y,
                                z=z)
