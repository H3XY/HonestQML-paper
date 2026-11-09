# Submission kit

Everything needed to post the preprint and submit it. Steps marked **you** need your accounts or decisions.

## 1. Before submitting

- [x] External review (ChatGPT) addressed on 2026-11-09: seeds, tuned baselines, CIs, ablation, 200-input hardware study, exact shot-noise tests, related work, reproducibility appendix.

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
| Comments | 9 pages, 4 figures, 4 tables. Code: https://github.com/H3XY/AGI and https://github.com/H3XY/Entangle |

**Abstract** (plain text, 1573 of 1,920 characters):

> We compare small quantum neural networks (QNNs) with classical models under a fixed protocol: classical baselines receive the same inputs and are tuned by cross-validation, a strong classical reference is always reported, hardware runs are compared with noise-free simulation on identical inputs, and hardware deviations are tested against the exact shot-noise expectation. On two text tasks, a 4-qubit QNN fed by a sentence encoder is within 1.5 percentage points of tuned classical models on the same four features: slightly but significantly below on sentiment (0.757 ± 0.007 vs. 0.772 over three seeds) and statistically tied on CVE severity (0.699 ± 0.015 vs. 0.691). A controlled ablation attributes most of the effect of circuit design to the data encoding (21 points), while 2–6 qubits changed accuracy by at most 1.2 points. On IBM's ibm_marrakesh, with 200 inputs per task and repeated runs on fixed physical qubits, device accuracy is statistically indistinguishable from noise-free simulation, but the device shows a small, resolvable bias in output probability (−0.006 and −0.004, 95% CIs excluding zero). A noise model of the same device reproduces this bias; a model of an older 5-qubit device overstates it about fivefold. In exact simulation of quantum data, a learned two-copy QNN distinguishes pure from mixed states with 16–64 copies per seed from 2 to 6 qubits, while the classical-shadow method we test needs 128–4,096, a small-scale illustration of a known multi-copy separation. All code, data pipelines, result files and job identifiers are public.

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
