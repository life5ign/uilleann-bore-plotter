#!/usr/bin/env python3

import os
from glob import glob
import argparse
import csv
import math

import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import pandas as pd
from scipy import polyval, polyfit

# create argparser
def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
       description='''Plot all CSV files, assumed to have one column of x
        values, and one column of y vaues each, on a graph using matplotlib,
        and name each series after the filename.  The x should be the distance
        from the bell of the chanter in mm.  The y values should be the
        diameter of the probe in mm.'''
    )
    parser.add_argument(
        "plot_directory", type=str, help='''The directory from which to plot all CSV
        files'''
    )
    parser.add_argument(
        "--fit-plots", dest="fit_plots", action='store_true',
        help='''Fit the plots with a 3rd degree polynomial for each series'''
    )
    return parser

def main() -> None:
    # parse args
    parser = init_argparse()
    args = parser.parse_args()

    # read data
    files = glob(f"{args.plot_directory}/*.csv")
    headers = ('x','y')

    # create axes
    fig, ax = plt.subplots()

    # loop through the files and plot the data
    for file in files:
        series_name = os.path.basename(file).split('.csv')[0]

        data = pd.read_csv(file, names=headers)
        x,y = data['x'], data['y']

        # plot data
        ax.plot(x, y, linewidth=2.0, label=series_name)

        # fit data and plot fit line
        if args.fit_plots:
            a, b, c, d = polyfit(x, y, 3)
            y_predicted = polyval([a, b, c, d], x)
            ax.plot(x, y_predicted, linewidth=2.0, label=f"fit{series_name}")

    # set labels and titles
    ax.set_xlabel("Distance from bell (mm)")
    ax.set_ylabel("Diameter of probe (mm)")
    ax.set_title(f'''Plot of probe diameter vs. distance from chanter bell
                 for series in directory "{args.plot_directory}"''')
    ax.legend()

    # set grid properties
    ax.grid(which='both', axis='both')
    ax.minorticks_on()

    # set x axis format
    ax.xaxis.set_major_locator(MultipleLocator(50))
    ax.xaxis.set_major_formatter('{x:.2f}')
    ax.xaxis.set_minor_locator(MultipleLocator(10))

    # draw vertical lines at locations of interest along the x axis
    # vertical_line_spacing = 50

    #max_oval_x_value = max(oval_x)
    #max_round_x_value = max(round_x)
    #max_x_value = max([max_oval_x_value, max_round_x_value])
    #
    #
    #for i in range(0, math.floor(max_x_value), vertical_line_spacing):
    #    ax.axvline(x=i)
    #
    ## plot a line at the final datapoint common to the two sets
    #ax.axvline(x=min([max_oval_x_value, max_round_x_value]))

    plt.show()

if __name__ == '__main__':
    main()
