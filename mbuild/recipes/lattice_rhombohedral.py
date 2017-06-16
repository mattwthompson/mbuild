__all__ = ['RhombohedralPrim']

from mbuild.lattice import Lattice
from mbuild.recipes.lattice_cubic import compound_dict_expansion


def input_error_rhombohedral(lattice_spacings, angles):
    """Check for input errors and incorrect monoclinic information.

    input_error_monoclinic ensures that the lattice spacings and angles
    inputted by the user are correct for the monoclinic bravais lattice
    definitions.

    Parameters:
    -----------
    lattice_spacings: float, size=1, float,
        Edge lengths of the lattice unit cell.
    angles: float, size=1, float
        Interplanar angles of the unit cell.

    """

    try:
        float(lattice_spacings)
    except ValueError:
        raise ValueError('Cannot convert lattice_spacings to float, '
                         'ensure that the spacing is a single value that '
                         'represents the edge lengths of the unit cell.')
    try:
        float(angles)
    except ValueError:
        raise ValueError('Cannot convert angle to float, ensure that angle is '
                         'a single value that represents the interplanar '
                         'angle beta.')

    if angles != 90:
        pass
    else:
        raise ValueError('Incorrect interplanar angle value for angles. '
                         'Angles != 90.')

    lattice_spacings = float(lattice_spacings)
    angles = float(angles)
    return_angles = [angles for x in range(3)]
    return_spacings = [lattice_spacings for x in range(3)]

    return  return_spacings, return_angles


class RhombohedralPrim(Lattice):
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
    basis_atoms = {'A': [[0, 0, 0]]}

    def __init__(self, lattice_spacings, angles):
        lattice_spacings, angles = input_error_rhombohedral(lattice_spacings,
                                                            angles)

        super().__init__(lattice_spacings=lattice_spacings,
                         dimension=self.dimension,
                         angles=angles,
                         basis_atoms=self.basis_atoms)

    def populate(self, compound_dict=None, x=1, y=1, z=1):
        compound_dict = compound_dict_expansion(self.basis_atoms,
                                                compound_dict, 1)
        return super().populate(compound_dict=compound_dict,
                                x=x,
                                y=y,
                                z=z)
