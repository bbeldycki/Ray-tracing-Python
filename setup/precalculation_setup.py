import json
import numpy as np
from Functions.nodes_and_weights_gauss_legendre import gauss_legendre_nodes_and_weights


def precalculation_setup(data: dict) -> list:
    if data['select_grid_type']['square']:
        max_alfa_beta = np.maximum(data['alfa_min'] ** 2, data['alfa_max'] ** 2) + \
                        np.maximum(data['beta_min'] ** 2, data['beta_max'] ** 2)
    elif data['select_grid_type']['circular']:
        max_alfa_beta = data['radial_cut'] ** 2
        # Compute range of observed radii (logarithmically spaced)
        # interval is from 0 do ln(2)
        r_a = 0.0
        r_b = np.log(2.0)
        r_nodes, r_weights = gauss_legendre_nodes_and_weights(r_a, r_b, data['number_of_points_along_x_or_r_axis'])
        radius_list = []
        for node in r_nodes:
            radius_list.append(data['radial_cut'] * np.expm1(node))
    return []


if __name__ == '__main__':
    filename = "setup_file.json"
    with open(filename, "r") as initfile:
        data = json.load(initfile)
        z = 0
        precalculation_setup(data)
