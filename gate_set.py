from draw_bounds import DrawBounds


class GateSet(object):

    def __init__(self, data):
        self.data = data
        self.gates = {}
        self.coordinates = []

    def add_gate(self, gate, name=None):
        """
        Records the coordinates of the passed gate.

        :param gate: (DrawBounds object) Gate to record coordinates of.
        :param name: {str}  Optional name for gate.
        :return: None
        """

        try:
            vertices = gate.vertices
        except AttributeError:
            return "Argument must be an instance of DrawBounds"

        if name:
            try:
                self.gates[name] = {'id': len(self.gates)}
            except NameError:
                return "gate name must be a type string"
        else:
            name = 'gate{}'.format(len(self.gates))
            self.gates[name] = {'id': len(self.gates)}
        # TODO: Need safeguards to check that the gate is a closed shape
        # May want to have a check at drawing that removes a point if it is a duplicate
        # If I just check for a duplicate it isn't guaranteed a closed polygon has been created
        # Need to consider if I want warning/failure if there are multiple closed shapes

        coordinates = []
        for vertex in vertices:
            x, y = vertex.get_offsets()[0]
            coordinates.append([x, y])
        self.gates[name]['coordinates'] = coordinates
