Simple example of *in silico* generation of carbide-derived carbons using
quenched molecular dynamics and the ReaxFF force field.

Requires [mbuild](https://github.com/mosdef-hub/mbuild) 0.8.1+ (thanks to Ray
Matsumoto for updating the mBuild LAMMPS writer) and
[lammps](https://github.com/lammps/lammps) built with `user-reaxc`.

A ReaxFF force field file is also necessary. The file we used, `ff-feb14.reax`,
includes parameters reported in [this](https://doi.org/10.1021/jp510274e)
publication.

Usage
```
python src/build.py
lammps -i src/in.quench
```

If you find this useful for a publication, please cite [our
paper](https://doi.org/10.3390/c3040032)

The bibtex reference is
```
@article{Thompson2017,
    author = "Thompson, Matthew and Dyatkin, Boris and Wang, Hsiu-Wen and
        Turner, C. and Sang, Xiahan and Unocic, Raymond and Iacovella, Christopher and
        Gogotsi, Yury and van Duin, Adri and Cummings, Peter",
    doi = "10.3390/c3040032",
    issn = "2311-5629",
    journal = "C",
    number = "4",
    title = "An Atomistic Carbide-Derived Carbon Model Generated Using ReaxFF-Based Quenched Molecular Dynamics",
    url = "http://www.mdpi.com/2311-5629/3/4/32",
    volume = "3",
    year = "2017"
}
```
