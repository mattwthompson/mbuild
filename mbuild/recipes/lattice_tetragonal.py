__all__ = ['TetragonalPrim', 'TetragonalBody']

from mbuild.lattice import Lattice
from mbuild.recipes.lattice_cubic import compound_dict_expansion


def input_error_tetragonal(lattice_spacings):
    """Check for input errors and incorrect tetragonal information.

    input_error_tetragonal ensures that the lattice spacings and angles
    inputted by the user are correct for the tetragonal bravais lattice
    definitions.

    Parameters:
    -----------
    lattice_spacings: list-like, size=2, floats,
        Edge lengths of the lattice unit cell.

    """

    if isinstance(lattice_spacings, list):
        for space in lattice_spacings:
            try:
                float(space)
            except ValueError:
                raise ValueError('Lattice spacings cannot be converted to '
                                 'floating point numbers.')

        if len(lattice_spacings) != 2:
            raise ValueError('Incorrect amount of lattice spacings provided. '
                             'Tetragonal class only requires 2 values for '
                             'lattice spacings, a and c. {} were passed.'
                             .format(len(lattice_spacings)))
    else:
        raise TypeError('Incorrect type for lattice_spacings. Expected list, '
                        'recieved {}.'.format(type(lattice_spacings)))

    return [lattice_spacings[0], lattice_spacings[0], lattice_spacings[1]]


class TetragonalPrim(Lattice):
    """Tetragonal 3D lattice system.

    Attributes
    ----------
    dimension : int, default=3
        Dimension of the system of interest.
    lattice_vectors : numpy array, shape=(dimension, dimension), optional
        Vectors that define edges of the Tetragonal system.
    lattice_spacings : list-like, size=2, required, default=None
        Lengths of unit cell edges.
    basis_atoms : dictionary, shape={'id':[list of atom positions]},
    default=[0, 0, 0]
        Location of all basis compounds in unit cell.
    angles : float,  size=1, required
        Interplanar angles describing unit cell.

    Tetragonal Defaults
    ---------------------
    dimension : 3
    alpha = beta = gamma = 90
    a = b != c
    basis_atoms : 'A', [[0, 0, 0]]
    """

    dimension = 3
    basis_atoms = {'A': [[0, 0, 0]]}
    angles = [90, 90, 90]

    def __init__(self, lattice_spacings):
        lattice_spacings = input_error_tetragonal(lattice_spacings)

        super().__init__(lattice_spacings=lattice_spacings,
                         dimension=self.dimension,
                         angles=self.angles,
                         basis_atoms=self.basis_atoms)

    def populate(self, compound_dict=None, x=1, y=1, z=1):
        compound_dict = compound_dict_expansion(self.basis_atoms,
                                                compound_dict, 1)
        return super().populate(compound_dict=compound_dict,
                                x=x,
                                y=y,
                                z=z)


class TetragonalBody(Lattice):
    """Tetragonal 3D lattice system.

    Attributes
    ----------
    dimension : int, default=3
        Dimension of the system of interest.
    lattice_vectors : numpy array, shape=(dimension, dimension), optional
        Vectors that define edges of the Tetragonal system.
    lattice_spacings : list-like, size=2, required, default=None
        Lengths of unit cell edges.
    basis_atoms : dictionary, shape={'id':[list of atom positions]},
    default=[0, 0, 0], [0.5, 0.5, 0.5]
        Location of all basis compounds in unit cell.
    angles : float,  size=1, required
        Interplanar angles describing unit cell.

    Tetragonal Defaults
    ---------------------
    dimension : 3
    alpha = beta = gamma = 90
    a = b != c
    basis_atoms : 'A', [[0, 0, 0]]
                  'B', [[0.5, 0.5, 0.5]]
    """

    dimension = 3
    basis_atoms = {'A': [[0, 0, 0]],
                   'B': [[0.5, 0.5, 0.5]]}
    angles = [90, 90, 90]

    def __init__(self, lattice_spacings):
        lattice_spacings = input_error_tetragonal(lattice_spacings)

        super().__init__(lattice_spacings=lattice_spacings,
                         dimension=self.dimension,
                         angles=self.angles,
                         basis_atoms=self.basis_atoms)

    def populate(self, compound_dict=None, x=1, y=1, z=1):
        compound_dict = compound_dict_expansion(self.basis_atoms,
                                                compound_dict, 2)
        return super().populate(compound_dict=compound_dict,
                                x=x,
                                y=y,
                                z=z)
