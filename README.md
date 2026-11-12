# Small Quantum Classifiers Under Matched Classical and Hardware Tests

Vivek Reddy, independent researcher (vvardhan00@gmail.com).

- **Full version** ([main.pdf](main.pdf), 15 pages): the pre-registered text benchmark, Fourier dequantization check, IBM Heron hardware study, and the quantum-data study (entanglement, phases, two-copy purity test with a 2-qubit hardware run).
- **Workshop version** ([workshop.pdf](workshop.pdf), 7 pages plus references): the classical-data and hardware parts, with the quantum-data results summarised.

Code: [H3XY/AGI](https://github.com/H3XY/AGI) (v1.0.4, doi:10.5281/zenodo.24150592) and [H3XY/Entangle](https://github.com/H3XY/Entangle) (v1.0.1, doi:10.5281/zenodo.24150608).

## Build

```bash
brew install tectonic        # once
tectonic -X compile main.tex # -> main.pdf
./make_arxiv.sh               # -> main.pdf, workshop.pdf and arxiv.zip for upload
```

Figures in `figures/` are copied from the two repos' `results/` folders. Re-copy them if the results change.

## Before submitting

- [x] Confirm every number against the repos' `results/` files (done; you still read it end to end)
- [x] Check every entry in `refs.bib` against the publisher's page (done: arXiv + Crossref)
- [x] Make `H3XY/AGI` and `H3XY/Entangle` public (done 2026-11-09)
- [x] Archive the code on Zenodo (AGI v1.0.4, Entangle v1.0.1)
- [x] Author line: Vivek Reddy, independent researcher, vvardhan00@gmail.com
- [ ] Keep or edit the AI-assistance statement in the acknowledgements (arXiv and most journals require disclosure)
- [ ] arXiv: category `quant-ph`, with `cs.LG` as a cross-list. First-time submitters need an endorsement

See [SUBMISSION.md](SUBMISSION.md) for the arXiv metadata, endorsement email and venues.

## Blog post

A copy of the blog draft is in [blog/post.md](blog/post.md).
