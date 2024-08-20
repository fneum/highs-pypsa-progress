import pypsa
import pip

version = snakemake.wildcards.highs_version
resolution = int(snakemake.wildcards.resolution)

pip.main(
    [
        "install",
        "--force-reinstall",
        "--no-deps",
        "--no-cache-dir",
        f"highspy=={version}",
    ]
)

n = pypsa.Network(snakemake.input[0])

n.snapshots = n.snapshots[::resolution]

n.optimize(
    solver_name="highs",
    # **snakemake.config['solver_options']
)
