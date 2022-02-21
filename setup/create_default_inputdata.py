import json


def create_default_input_file():
    schema = {
        "spin": 0.998,
        "black_hole_mass": 1,
        "initial_polar_angle": 60,
        "number_of_trajectories": 1,
        "select_procedure": {
            "compute_u_final": False,
            "compute_mu_final": True
        },
        "select_grid_type": {
            "square": True,
            "circular": False
        },
        "select_grid_density": {
            "grid_density_based_on_number_of_trajectories": False,
            "grid_density_chosen_arbitrarily": True
        },
        "alfa_min": -10.0,
        "alfa_max": 10.0,
        "beta_min": -10.0,
        "beta_max": 10.0,
        "number_of_points_along_x_or_r_axis": 20,
        "number_of_points_along_y_or_phi_axis": 20,
        "number_of_points_along_trajectory": 500
    }
    with open("default_setup.json", "w+") as default_file:
        json.dump(schema, default_file, indent=2)


if __name__ == '__main__':
    create_default_input_file()
