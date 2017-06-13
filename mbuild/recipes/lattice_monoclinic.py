__all__ = ['MonoPrim', 'MonoBase']

from mbuild.lattice import Lattice
from mbuild.recipes.lattice_cubic import compound_dict_expansion


def input_error_monoclinic(lattice_spacings, angles):
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

class MonoPrim(Lattice):
    """Primitive monoclinic Bravais lattice system.

    Monoclinic lattice class based on the primitive monoclinic
    Bravais lattice.

    alpha == gamma = 90, beta != 90
    a != c

    Attributes
    ----------
    dimension: int, 3
        Dimension of crystal system of interest.
    lattice_vectors: numpy array, shape=(dimension, dimension), optional
        Vectors that define the edges of the lattice system.
    lattice_spacings: list, float, length=3, required
        Lengths of the unit cell edges.
    angles: float, required
        Interplanar angles describing the unit cell.
    basis_atoms: dictionary, shape={'id':[list of atom positions]

    Primitive monoclinic defaults
    -----------------------------
    dimension : 3
    lattice_vectors : None
    angles : None
    basis_atoms : 'A', [[0, 0, 0]]
    """

    dimension = 3
    basis_atoms = {'A': [[0, 0, 0]]}

    def __init__(self, lattice_spacings, angles):
        input_error_monoclinic(lattice_spacings, angles)

        super().__init__(lattice_spacings=lattice_spacings,
                         dimension=self.dimension,
                         basis_atoms=self.basis_atoms,
                         lattice_vectors=None,
                         angles=self.angles)

    def populate(self, compound_dict=None, x=1, y=1, z=1):
        compound_dict = compound_dict_expansion(self.basis_atoms,
                                                compound_dict, 1)


class MonoBase(Lattice):
    """Base-centered monoclinic Bravais lattice system.

    Monoclinic lattice class based on the base-centered monoclinic
    Bravais lattice.

    alpha == gamma = 90, beta != 90
    a != c

    Attributes
    ----------
    dimension: int, 3
        Dimension of crystal system of interest.
    lattice_vectors: numpy array, shape=(dimension, dimension), optional
        Vectors that define the edges of the lattice system.
    lattice_spacings: list, float, length=3, required
        Lengths of the unit cell edges.
    angles: float, required
        Interplanar angles describing the unit cell.
    basis_atoms: dictionary, shape={'id':[list of atom positions]

    Base-centered monoclinic defaults
    -----------------------------
    dimension : 3
    lattice_vectors : None
    angles : None
    basis_atoms : 'A', [[0, 0, 0]]
                  'B', [[0.5, 0.5, 0]]
    """

    dimension = 3
    basis_atoms = {'A': [[0, 0, 0]],
                   'B': [[0.5, 0.5, 0]]}

    def __init__(self, lattice_spacings, angles):
        input_error_monoclinic(lattice_spacings, angles)

        super().__init__(lattice_spacings=lattice_spacings,
                         dimension=self.dimension,
                         basis_atoms=self.basis_atoms,
                         lattice_vectors=None,
                         angles=self.angles)

    def populate(self, compound_dict=None, x=1, y=1, z=1):
        compound_dict = compound_dict_expansion(self.basis_atoms,
                                                compound_dict, 2)
