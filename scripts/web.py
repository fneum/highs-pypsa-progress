
import pandas as pd
import holoviews as hv

import hvplot.pandas
hv.extension('bokeh')

def load_benchmark(fn):
    s = pd.read_csv(fn, sep='\t').mean(numeric_only=True)
    s.name = tuple(fn[:-4].split("_")[1:])
    return s

df = pd.concat(
    [load_benchmark(fn) for fn in snakemake.input],
    axis=1,
).T
df.index.names = ['resolution', 'highs_version']

df.to_csv(snakemake.output.csv)

opts = dict(fontscale=2, legend_position='top_left')

common = dict(
    height=500,
    width=500,
    xlabel="n-hourly resolution",
)

left = df["s"].unstack().hvplot(
    title="Time",
    ylabel="seconds",
    **common
).opts(**opts)

right = df["max_rss"].unstack().hvplot(
    title="Memory",
    ylabel='megabytes',
    **common
).opts(**opts)

figure = (left + right).opts(shared_axes=False)

hv.save(figure, snakemake.output.html, title='HiGHS Progress Tracker')
