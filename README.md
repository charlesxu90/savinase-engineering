# Savinase engineering with the AlphaVariant framework

## Install

## Download data files
Please download the data files associated with this repository through [Zenodo](Linke to add).

## Usage
Please follow the notebooks in each of the three rounds to see specific workflow.

A general workflow is as follows:

1. Prepare for the RL run:
- 1) Train a prior model for an enzyme of interest (see [0.prep_prior_data.ipynb](first_round/0.prep_prior_data.ipynb) and `train_prior` in **`AlphaVariant`**)
- 2) Set up the hotspots to explore for this enzyme (see [1.select_hotspot.ipynb](first_round/1.select_hotspot.ipynb))
- 3) Build predictive models to serve as feedback in RL steps (see [1.eval_act_model.ipynb](first_round/1.eval_act_model.ipynb) and `train_fit_model` in **`AlphaVariant`**)

2. Run the RL workflow
- 1) Prepare prior and predictive models, start variant, and hotspots, and set up the config file, e.g. [train_agent_config.yaml](first_round/config/train_agent_config.yaml)
- 2) Execute the RL run by calling `train_agent` in **`AlphaVariant`**
- 3) Analyze the RL result and design libraries (see [3.design_libraries.ipynb](second_round/3.design_libraries.ipynb) for degenerate codon library design using [**dgc-libgen**](https://github.com/charlesxu90/dgc-libgen))

3. Analyze the wet-lab results
- 1) Show the dot plots of variants (e.g [4.plot_lib_act_dot_plot.ipynb](second_round/4.plot_lib_act_dot_plot.ipynb) and []())
- 2) Visualize the top variants (e.g. [5.top5_variants_in_two_rounds.ipynb](second_round/5.top5_variants_in_two_rounds.ipynb))
- 3) Show fitness landscape (e.g. [9.draw_fitness_landscape.ipynb](second_round/9.draw_fitness_landscape.ipynb))

## License
This code is licensed under [MIT License](./LICENSE.txt).

