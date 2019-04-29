import numpy as np
import pandas as pd
import json
import matplotlib.pyplot as plt

with open(
    "./../MPHYG001_files/python_language_1/python_language_1_example_data.json"
) as dfile:
    data = json.load(dfile)
    # data = np.genfromtxt(dfile)

print(data)

data_file = "./../MPHYG001_files/python_language_1/python_language_1_data.csv"
df = pd.read_csv(data_file)

ylist = []
dict = {}
for i in range(df.shape[0]):
    if df["year"].iloc[i] in ylist:
        dict[str(df["year"].iloc[i])].append(df["rainfall (mm/day)"].iloc[i])
    else:
        dict[str(df["year"].iloc[i])] = [df["rainfall (mm/day)"].iloc[i]]
        ylist.append(df["year"].iloc[i])
print(dict)
with open("dict.json", "w") as f:
    json.dump(dict, f)


def for_plot(file_name, year, colour="b"):
    with open(file_name, "r") as f:
        data = json.load(f)
    plt.plot(data[year], color=colour)
    plt.ylabel("rainfall (mm/day)")
    plt.xlabel("day")
    plt.title(year)
    plt.savefig("rainfall_plot_" + year + ".png")
    plt.close()


def mean_plot(file_name, start, end):

    with open(file_name, "r") as f:
        data = json.load(f)
    plot_list = []
    for i in range(start, end + 1):
        plot_list.append(np.mean(data[str(i)]))
    plt.plot(plot_list)
    plt.xlabel("years")
    plt.ylabel("mean rainfall (mm/day)")
    plt.xticks(list(range(0, end - start + 1)), list(range(start, end + 1)))
    plt.savefig("mean_plot_" + str(start) + "_" + str(end) + ".png")
    plt.close()


def correct_val(value):
    return value * 1.2 ** (np.sqrt(2))


def for_correct(year_vals):
    new_vals = []
    for x in year_vals:
        new_vals.append(correct_val(x))
    return new_vals


def for_comprehend(year_vals):

    """list comprehension has a more compact notation,
    but it might be less interpretable.
    Furthermore, list comprehension can avoid
    storing two array names,
    while modifying an array when it is being
    looped over can be more tricky."""

    new_vals = [correct_val(x) for x in year_vals]

    return new_vals


# for_plot('dict.json', '1998', colour = 'b')
# mean_plot('dict.json', 1988, 2000)
