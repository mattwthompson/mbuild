__all__ = ['OrthoPrim', 'OrthoBase', 'OrthoBody', 'OrthoFace']

from mbuild.lattice import Lattice
from mbuild.recipes.lattice_cubic import compound_dict_expansion


class OrthoPrim(Lattice):
    """Primitive orthorhombic 3D lattice system.

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
    angles : list-like,  shape=(dimension,), default=[90,90,90]
        Interplanar angles describing unit cell.

    OrthoPrim Defaults
    ---------------------
    dimension : 3
    angles = [90, 90, 90]
    basis_atoms : 'A', [[0, 0, 0]]
    """

    dimension = 3
    angles = [90, 90, 90]
    basis_atoms = {'A': [[0, 0, 0]]}

    def __init__(self, lattice_spacings):
        super().__init__(lattice_spacings=lattice_spacings,
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


class OrthoBase(Lattice):
    """Base-centered orthorhombic 3D lattice system.

    Attributes
    ----------
    dimension : int, default=3
        Dimension of the system of interest.
    lattice_vectors : numpy array, shape=(dimension, dimension), optional
        Vectors that define edges of the cubic system.
    lattice_spacings : float, shape=1, required, default=None
        Length of unit cell edge.
    basis_atoms : dictionary, shape={'id':[list of atom positions]},
    default= default base centered positons
        Location of all basis compounds in unit cell.
    angles : list-like,  shape=(dimension,), default=[90,90,90]
        Interplanar angles describing unit cell.

    OrthoBase Defaults
    ---------------------
    dimension : 3
    angles = [90, 90, 90]
    basis_atoms : 'A', [[0, 0, 0]], 'B', [[.5, .5, 0]]
    """

    dimension = 3
    angles = [90, 90, 90]
    basis_atoms = {'A': [[0, 0, 0]],
                   'B': [[.5, .5, 0]]}

    def __init__(self, lattice_spacings):
        super().__init__(lattice_spacings=lattice_spacings,
                         dimension=self.dimension,
                         basis_atoms=self.basis_atoms,
                         lattice_vectors=self.lattice_vectors)

    def populate(self, compound_dict=None, x=1, y=1, z=1):
        compound_dict = compound_dict_expansion(self.basis_atoms,
                                                compound_dict, 2)
        return super().populate(compound_dict=compound_dict,
                                x=x,
                                y=y,
                                z=z)


class OrthoBody(Lattice):
    """Primitive orthorhombic 3D lattice system.

    Attributes
    ----------
    dimension : int, default=3
        Dimension of the system of interest.
    lattice_vectors : numpy array, shape=(dimension, dimension), optional
        Vectors that define edges of the cubic system.
    lattice_spacings : float, shape=1, required, default=None
        Length of unit cell edge.
    basis_atoms : dictionary, shape={'id':[list of atom positions]},
    default=[0, 0, 0], [.5, .5, .5]
        Location of all basis compounds in unit cell.
    angles : list-like,  shape=(dimension,), default=[90,90,90]
        Interplanar angles describing unit cell.

    OrthoBody Defaults
    ---------------------
    dimension : 3
    angles = [90, 90, 90]
    basis_atoms : 'A', [[0, 0, 0]], 'B', [[.5, .5, .5]]
    """

    dimension = 3
    angles = [90, 90, 90]
    basis_atoms = {'A': [[0, 0, 0]],
                   'B': [[.5, .5, .5]]}

    def __init__(self, lattice_spacings):
        super().__init__(lattice_spacings=lattice_spacings,
                         dimension=self.dimension,
                         basis_atoms=self.basis_atoms,
                         lattice_vectors=self.lattice_vectors)

    def populate(self, compound_dict=None, x=1, y=1, z=1):
        compound_dict = compound_dict_expansion(self.basis_atoms,
                                                compound_dict, 2)
        return super().populate(compound_dict=compound_dict,
                                x=x,
                                y=y,
                                z=z)


class OrthoFace(Lattice):
    """Primitive orthorhombic 3D lattice system.

    Attributes
    ----------
    dimension : int, default=3
        Dimension of the system of interest.
    lattice_vectors : numpy array, shape=(dimension, dimension), optional
        Vectors that define edges of the cubic system.
    lattice_spacings : float, shape=1, required, default=None
        Length of unit cell edge.
    basis_atoms : dictionary, shape={'id':[list of atom positions]},
    default=[0, 0, 0], [.5, .5, 0], [0, .5, .5]
        Location of all basis compounds in unit cell.
    angles : list-like,  shape=(dimension,), default=[90,90,90]
        Interplanar angles describing unit cell.

    OrthoFace Defaults
    ---------------------
    dimension : 3
    angles = [90, 90, 90]
    basis_atoms = {'A': [[0, 0, 0]],
                   'B': [[0, 0.5, 0.5]],
                   'C': [[0.5, 0, 0.5]],
                   'D': [[0.5, 0.5, 0]]}
    """

    dimension = 3
    angles = [90, 90, 90]
    basis_atoms = {'A': [[0, 0, 0]],
                   'B': [[0, 0.5, 0.5]],
                   'C': [[0.5, 0, 0.5]],
                   'D': [[0.5, 0.5, 0]]}

    def __init__(self, lattice_spacings):
        super().__init__(lattice_spacings=lattice_spacings,
                         dimension=self.dimension,
                         basis_atoms=self.basis_atoms,
                         lattice_vectors=self.lattice_vectors)

    def populate(self, compound_dict=None, x=1, y=1, z=1):
        compound_dict = compound_dict_expansion(self.basis_atoms,
                                                compound_dict, 4)
        return super().populate(compound_dict=compound_dict,
                                x=x,
                                y=y,
                                z=z)
