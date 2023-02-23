## Continuous HiGHS Benchmark

For a PyPSA-based energy system model.

## How to Run

```sh
mamba create -n highs python=3.10 pip
mamba activate highs
pip install -r requirements.txt
snakemake -j1 -F
```
