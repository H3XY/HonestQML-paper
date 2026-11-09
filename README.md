# Where Small Quantum Classifiers Help, and Where They Don't

A short paper (5 pages) covering two projects:
[H3XY/AGI](https://github.com/H3XY/AGI), a 4-qubit text classifier with real-hardware runs, and
[H3XY/Entangle](https://github.com/H3XY/Entangle), quantum-native data.

## Build

```bash
brew install tectonic        # once
tectonic -X compile main.tex # -> main.pdf
```

Figures in `figures/` are copied from the two repos' `results/` folders. Re-copy them if the results change.

## Before submitting

- [ ] Read the whole paper and confirm every number against the repos' `results/` files
- [ ] Check every entry in `refs.bib` against the publisher's page (authors, volume, pages)
- [ ] Make `H3XY/AGI` and `H3XY/Entangle` public, and archive each release on Zenodo for a DOI
- [ ] Decide on the author line and affiliation, and add a contact email if you want one
- [ ] Keep or edit the AI-assistance statement in the acknowledgements (arXiv and most journals require disclosure)
- [ ] arXiv: category `quant-ph`, with `cs.LG` as a cross-list. First-time submitters need an endorsement
