uillean-bore-plotter

# installation
On a system with python3, change directory to this project and run
```shell
pip install -r requirements.txt
```

# usage
## setup

Create a subdirectory in the `data` directory, and in it place CSV files
containing bore data. Name the subdirectory meaningfully. You may place as many
CSVs in it as you want, but make the the filename of each CSV represents
uniquely what the measurement type and source is--the name of the file will
become the name of the data series in the legend of the plot.

The first column in a CSV file should be the distance from the chanter bell in
mm, and the second column should be the probe diameter in mm at that distance.
The plots should contain only values, no headers.

## command
Run
```shell
python3 plot_bore_data.py <path_to_subdirectory>
```
or make the file executable and run
```shell
./plot_bore_data.py <path_to_subdirectory>
```

and extrapolate the data you need using the matplotlib plot.
