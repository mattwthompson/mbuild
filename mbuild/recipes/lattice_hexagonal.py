__all__ = ['HEX_3D']

import numpy as np
from mbuild.lattice import Lattice
from mbuild.recipes.lattice_cubic import expand_spacings_3d
from mbuild.recipes.lattice_cubic import compound_dict_expansion

def spacing_error(lattice_spacings):

    if not isinstance(lattice_spacings, list):
        raise TypeError('Lattice spacings should be a list of at least 2 values.')
    else:
        if len(lattice_spacings) < 2 or len(lattice_spacings) > 3:
            raise ValueError('Must supply 2-3 values for lattice '
                             'spacings.')

def spacing_error(lattice_spacings):
     

class HEX_3D(Lattice):
    """Hexagonal 3D lattice system.

    Attributes
    ----------
    dimension : int, default=3
        Dimension of the system of interest.
    lattice_vectors : numpy array, shape=(dimension, dimension), optional
        Vectors that define edges of the cubic system.
    lattice_spacings : float, shape=1, required, default=None
        Length of unit cell edge.
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
