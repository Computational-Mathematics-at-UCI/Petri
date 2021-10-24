from scipy.spatial import ConvexHull
import numpy as np


class Macromolecule:
    """
        Docstring macromolecule.
    """

    def __init__(self, id, atoms):
        self.id = id
        self.atoms = atoms
        self.convexHull = []
        self.size = []
        self.volume = 0

    def getID(self):
        """
        Returns assigned ID.
        """
        return self.id

    def getAtoms(self):
        return self.atoms

    def computeConvexHull(self):
        hull = ConvexHull(self.atoms)
        self.convexHull = np.array(hull.points[hull.vertices[:]])

    def getConvexHull(self):
        return self.convexHull

    def computeSize(self):
        self.size.append(abs(np.amax(self.atoms[:, 0]) - np.amin(self.atoms[:, 0])))
        self.size.append(abs(np.amax(self.atoms[:, 1]) - np.amin(self.atoms[:, 1])))
        self.size.append(abs(np.amax(self.atoms[:, 2]) - np.amin(self.atoms[:, 2])))

    def computeVolume(self):
        self.volume = self.size[0] * self.size[1] * self.size[2]

    def getVolume(self):
        return self.volume

    def getSize(self):
        return self.size

    def computeAll(self):
        self.computeConvexHull()
        self.computeSize()
        self.computeVolume()
