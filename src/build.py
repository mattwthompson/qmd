import mbuild as mb


c = mb.Compound()
c.name = 'C'

n_atoms = 1000
L = (n_atoms * 12.011 / 1000 / 950 / 6.0221409e23 *
     1e27) ** (1 / 3)  # amu / (kg / m ** 3) to nm

system = mb.fill_box(compound=c, n_compounds=n_atoms, box=mb.Box(3 * [L]))

system.save('data/system.lmp', atom_style='charge', overwrite=True)
