## Continuous HiGHS Benchmark

This workflow runs small benchmark cases for solving
[PyPSA](https://pypsa.readthedocs.io) networks with the
[HiGHS](https://highs.dev) solver. The test case is a small single-node capacity
expansion model for a 100% renewable electricity system with exogenous demand,
wind and solar generation, battery storage and hydrogen storage. The temporal
resolution is currently varied from 2-hourly to 6-hourly resolution for a full
year.

The benchmark is automatically executed for **all** available HiGHS versions on
[PyPI]("https://pypi.org/pypi/highspy") every Tuesday at 5 AM and the results
are subsequently deployed to https://fneum.github.io/highs-pypsa-progress/.

## Run Locally

```sh
mamba create -n highs python=3.10 pip
mamba activate highs
pip install -r requirements.txt
snakemake -j1 -F
```

## License

MIT
