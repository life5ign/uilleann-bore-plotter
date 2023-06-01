uillean-bore-plotter

This project aids in plotting bore data for woodwind instruments and extrapolating values from
different types of measurements of the same bore.

[TOC]

# Installation
On a system with python installed, change directory to this project and run
```shell
pip install -r requirements.txt
```

# Usage
## Setup

### `data` directory structure
To keep things organize, and if you with to submit a PR with data, create a subdirectory in the
`data` directory for the set of pipes you're modeling. In it, create sub directories for the
different parts of the set that contain bores. These subdirectories should represent a single
physical entity, e.g. the chanter, the bass drone, etc.  In each subdirectory, place CVSs containing
bore data for that object.  You may place as many CSVs as you want. Make sure the filename of each
CSV represents uniquely the measurement type and dimension (see existing data for examples). The
name of the file will become the name of the data series in the legend of the plot.

### CSV data file format
The first column in a CSV file should be the distance from the chanter bell in
mm, and the second column should be the probe diameter in mm at that distance.
The plots should contain only values and no headers.

Generally, there will be bore data for round probes in one file, and data for oval probes in
another.  This project will allow you to graph them in the same plot, so you can easily visually
calculate averages.

TODO: calculate the average for the user.

## Running the script
cd to the project directory and run
```shell
python plot_bore_data.py <path_to_subdirectory>

# e.g.
python plot_bore_data.py data/B_hannan_coyne/chanter
```
or make the file executable and run
```shell
./plot_bore_data.py <path_to_subdirectory>
```

and extrapolate the data you need using the matplotlib plot.
