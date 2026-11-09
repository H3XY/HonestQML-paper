# Submission kit

Everything needed to post the preprint and submit it. Steps marked **you** need your accounts or decisions.

## 1. Before submitting

- [x] Numbers cross-checked against `results/` in both repos (2026-11-09). One fix: shadow accuracy range 0.94–0.99.
- [x] References checked against arXiv and Crossref. DOIs added; Qiskit is cited via its 2024 paper.
- [x] Overclaim fixed: the QNN "does not clearly beat" classical models (CVE: 0.699 vs 0.692).
- [x] Code repos: full MIT license and CITATION.cff added; history cleaned (no personal email or hostname) and both repos made public (2026-11-09). Original histories and PRs are in the private, archived H3XY/AGI-archive and H3XY/Entangle-archive.
- [ ] **you:** read the paper end to end.
- [ ] **you:** decide on the author line and affiliation, and an optional contact email (currently "Vivek Reddy, Independent researcher").
- [x] H3XY/AGI and H3XY/Entangle are public.
- [ ] **you (optional):** archive both repos on Zenodo for a DOI. Log in to zenodo.org with GitHub, enable the repos, then create a GitHub release.

## 2. arXiv

Build the upload: `./make_arxiv.sh` → `arxiv.zip`.

| Field | Value |
|---|---|
| Primary category | quant-ph (Quantum Physics) |
| Cross-list | cs.LG (Machine Learning) |
| License | CC BY 4.0 (matches LICENSE) |
| Title | Where Small Quantum Classifiers Help, and Where They Don't: Fair Baselines and Real-Hardware Results on IBM Heron |
| Authors | Vivek Reddy |
| Comments | 5 pages, 3 figures, 1 table. Code: https://github.com/H3XY/AGI and https://github.com/H3XY/Entangle |

**Abstract** (plain text, 1147 of 1,920 characters):

> We benchmark small quantum neural networks (QNNs) against classical models under four rules: classical baselines see the same inputs, a strong classical ceiling is always reported, hardware runs are compared with noise-free simulation on identical samples, and anomalies are re-run against the shot-noise expectation. On classical data (two text tasks and three standard datasets), a 4-qubit QNN fed by a sentence-embedding encoder matches but does not clearly beat logistic regression on the same four features (within about one point) (sentiment: 0.758 vs. 0.769; CVE severity: 0.699 vs. 0.692). On IBM's 156-qubit ibm_marrakesh, the compiled circuits (depth 37, six two-qubit gates) reproduced noise-free predictions exactly on 4 of 5 datasets; repeated runs attribute the remaining drop to shot noise (p ≈ 0.27), and a standard fake-backend noise model overstated the bias fivefold. On quantum data, a two-copy QNN separates pure from mixed states with about 32 copies from 2 to 6 qubits, while classical shadows need 128 to 4,096, reproducing the known exponential multi-copy separation at small scale. Code and all result files are public.

**Endorsement (you).** First-time submitters to quant-ph need an endorsement. Start the submission, and arXiv shows an endorsement code. Send it to an established quant-ph author, ideally one whose work you cite or build on. A draft:

> Subject: arXiv quant-ph endorsement request: small-scale quantum ML benchmark on IBM hardware
>
> Dear Dr. [Name],
>
> I am an independent researcher preparing my first arXiv submission, a short benchmark of small quantum classifiers against matched classical baselines, with runs on IBM's ibm_marrakesh. It reproduces, at small scale, the multi-copy separation from your/[the cited] work on [topic], and finds that shallow circuits on current Heron hardware match noise-free simulation.
>
> Would you be willing to endorse me for quant-ph? My endorsement code is [CODE]. The PDF is attached and the code is public at https://github.com/H3XY/AGI and https://github.com/H3XY/Entangle. I understand if you are unable to; thank you for considering it.
>
> Best regards,
> Vivek Reddy

## 3. Peer-reviewed venues (after the preprint)

- **ReScience C** (rescience.github.io): reproductions of published results. The purity experiment reproduces Huang et al. (Science 2022). Best fit.
- **QTML** (Quantum Techniques in Machine Learning) and **IEEE Quantum Week (QCE)** workshops: benchmark and negative-result papers welcome.
- **Quantum Machine Intelligence** (Springer): a journal; reviewers will likely want more hardware samples and the 2-copy test on a device.

Check each venue's current call for papers and deadlines on its own site.

## 4. Blog post

The draft is the Claude doc "Honest Quantum Machine Learning on Real IBM Hardware". Export it (Markdown or PDF), then post on Medium, Substack, dev.to or a personal site, and link the arXiv abstract page once it is live.
