__all__ = ['SC', 'BCC', 'FCC']

import numpy as np
from mbuild.lattice import Lattice
from warnings import warn

def spacing_error(lattice_spacings):

    try:
        float(lattice_spacings)
    except TypeError:
        raise TypeError('Too many lattice_spacings for type cubic. '
                     'Spacings {} were passed in, expected 1 value that can '
                     'be converted to a float.'.format(lattice_spacings))

def expand_spacings_3d(lattice_spacings):
    lattice_spacings = float(lattice_spacings)
    return [lattice_spacings for x in range(3)]

def compound_dict_expansion(basis_atoms, compound_dict, num_basis_atoms):
    if isinstance(compound_dict, dict):
        if len(compound_dict.keys()) == 1:
            if num_basis_atoms > 1:
                warn('Multiple basis atoms and only 1 key to compound passed. '
                     'Will fill in remaining basis atoms with compound found '
                     'at key \'A\'.')
                for key, val in basis_atoms.items():
                    try:
                        compound_dict[key]
                    except KeyError:
                        compound_dict[key] = compound_dict['A']
            else:
                pass
        elif len(compound_dict.keys()) < num_basis_atoms:
            raise ValueError('Compound dictionary does not have enough keys. '
                             '{} was expected, {} provided.'
                             .format(num_basis_atoms, len(compound_dict.keys)))
        elif len(compound_dict.keys()) >  num_basis_atoms:
            raise ValueError('Compound dictionary has too many keys. '
                             '{} was expected, {} provided.'
                             .format(num_basis_atoms, len(compound_dict.keys)))
        else:
            pass
    else:
        raise TypeError('Compound dict is not of type dict. Refer to docs '
                        'for proper compound_dict design.')

    return compound_dict


class SC(Lattice):
    """Simple cubic Bravais lattice system.

    Attributes
    ----------
    dimension : int, default=3
        Dimension of the system of interest.
    lattice_vectors : numpy array, shape=(dimension, dimension), optional
                      default=([1,0,0], [0,1,0], [0,0,1])
        Vectors that define edges of the cubic system.
    lattice_spacings : float, shape=1, required, default=None
        Length of unit cell edge.
    basis_atoms : dictionary, shape={'id':[list of atom positions]},
    default=[0, 0, 0]
        Location of all basis compounds in unit cell.
    angles : list-like,  shape=(dimension,), optional, default=None
        Interplanar angles describing unit cell.

    Simple Cubic Defaults
    ---------------------
    dimension : 3
    lattice_vectors : [1, 0, 0
                       0, 1, 0
                       0, 0, 1]

    basis_atoms : 'A', [[0, 0, 0]]
    """

    dimension = 3
    lattice_vectors = np.identity(dimension, dtype=float)
    basis_atoms = {'A':[[0, 0, 0]]}

    def __init__(self, lattice_spacings):
        spacing_error(lattice_spacings=lattice_spacings)

        super().__init__(lattice_spacings=expand_spacings_3d(lattice_spacings),
                         dimension=self.dimension,
                         basis_atoms=self.basis_atoms,
                         lattice_vectors=self.lattice_vectors
                         )

    def populate(self, compound_dict=None, x=1, y=1, z=1):
        compound_dict = compound_dict_expansion(self.basis_atoms, compound_dict, 1)
        return super().populate(compound_dict=compound_dict,
                                x=x,
                                y=y,
                                z=z)

class BCC(Lattice):
    """Simple cubic Bravais lattice system.

    Attributes
    ----------
    dimension : int, default=3
        Dimension of the system of interest.
    lattice_vectors : numpy array, shape=(dimension, dimension), optional
                      default=([1,0,0], [0,1,0], [0,0,1])
        Vectors that define edges of the cubic system.
    lattice_spacings : float, shape=1, required, default=None
        Length of unit cell edges.
    basis_atoms : dictionary, shape={'id':[list of atom positions]},
    default=bcc basis positions
        Location of all basis compounds in unit cell.
    angles : list-like,  shape=(dimension,), optional, default=None
        Interplanar angles describing unit cell.

    Simple Cubic Defaults
    ---------------------
    dimension : 3
    lattice_vectors : [1, 0, 0
                       0, 1, 0
                       0, 0, 1]

    basis_atoms : 'A' : [0, 0, 0], 'B' : [0.5, 0.5, 0.5]
    """

    dimension = 3
    lattice_vectors = np.identity(dimension, dtype=float)
    basis_atoms = {'A':[[0, 0, 0]],
                   'B':[[0.5, 0.5, 0.5]]}

    def __init__(self, lattice_spacings):
        spacing_error(lattice_spacings=lattice_spacings)
        super().__init__(lattice_spacings=expand_spacings_3d(lattice_spacings),
                         dimension=self.dimension,
                         basis_atoms=self.basis_atoms,
                         lattice_vectors=self.lattice_vectors
                         )

    def populate(self, compound_dict=None, x=1, y=1, z=1):
        compound_dict = compound_dict_expansion(self.basis_atoms, compound_dict, 2)
        return super().populate(compound_dict=compound_dict,
                                x=x,
                                y=y,
                                z=z)

class FCC(Lattice):
    """Simple cubic Bravais lattice system.

    Attributes
    ----------
    dimension : int, default=3
        Dimension of the system of interest.
    lattice_vectors : numpy array, shape=(dimension, dimension), optional
                      default=([1,0,0], [0,1,0], [0,0,1])
        Vectors that define edges of the cubic system.
    lattice_spacings : float, shape=1, required, default=None
        Length of unit cell edges.
    basis_atoms : dictionary, shape={'id':[list of atom positions]},
    default=fcc basis positions
        Location of all basis compounds in unit cell.
    angles : list-like,  shape=(dimension,), optional, default=None
        Interplanar angles describing unit cell.

    Simple Cubic Defaults
    ---------------------
    dimension : 3
    lattice_vectors : [1, 0, 0
                       0, 1, 0
                       0, 0, 1]

    basis_atoms : 'A', [[0, 0, 0]]
    """

    dimension = 3
    lattice_vectors = np.identity(dimension, dtype=float)
    basis_atoms = {'A':[[0, 0, 0]],
                        'B':[[0, 0.5, 0.5]],
                        'C':[[0.5, 0, 0.5]],
                        'D':[[0.5, 0.5, 0]]}

    def __init__(self, lattice_spacings):
        spacing_error(lattice_spacings=lattice_spacings)
        super().__init__(lattice_spacings=expand_spacings_3d(lattice_spacings),
                         dimension=self.dimension,
                         basis_atoms=self.basis_atoms,
                         lattice_vectors=self.lattice_vectors
                         )

    def populate(self, compound_dict=None, x=1, y=1, z=1):
        compound_dict = compound_dict_expansion(self.basis_atoms, compound_dict, 4)
        return super().populate(compound_dict=compound_dict,
                                x=x,
                                y=y,
                                z=z)

