# Submission kit

Everything needed to post the preprint and submit it. Steps marked **you** need your accounts or decisions.

## 1. Before submitting

- [x] External review (ChatGPT) addressed on 2026-11-09: seeds, tuned baselines, CIs, ablation, 200-input hardware study, exact shot-noise tests, related work, reproducibility appendix.

- [x] Numbers cross-checked against `results/` in both repos (2026-11-09). One fix: shadow accuracy range 0.94–0.99.
- [x] References checked against arXiv and Crossref. DOIs added; Qiskit is cited via its 2024 paper.
- [x] Overclaim fixed: the QNN "does not clearly beat" classical models (CVE: 0.699 vs 0.692).
- [x] Code repos: full MIT license and CITATION.cff added; history cleaned (no personal email or hostname) and both repos made public (2026-11-09). Original histories and PRs are in the private, archived H3XY/AGI-archive and H3XY/Entangle-archive.
- [ ] **you:** read the paper end to end.
- [x] Author line: Vivek Reddy, Independent researcher, vvardhan00@gmail.com.
- [x] H3XY/AGI and H3XY/Entangle are public.
- [ ] **you (optional):** archive both repos on Zenodo for a DOI. Log in to zenodo.org with GitHub, enable the repos, then create a GitHub release.

## 2. arXiv

Build the upload: `./make_arxiv.sh` → `arxiv.zip`.

| Field | Value |
|---|---|
| Primary category | quant-ph (Quantum Physics) |
| Cross-list | cs.LG (Machine Learning) |
| License | CC BY 4.0 (matches LICENSE) |
| Title | Small Quantum Classifiers Under Matched Classical and Hardware Tests: Pre-Registered Benchmarks, Fourier Surrogates and IBM Heron Runs |
| Authors | Vivek Reddy |
| Comments | 16 pages, 5 figures, 7 tables. Code: AGI v1.0.5 (doi:10.5281/zenodo.24152278) and Entangle v1.0.1 (doi:10.5281/zenodo.24150608) |

**Abstract** (plain text, 1,918 of 1,920 characters):

> We compare small quantum neural networks (QNNs) with classical models under a fixed protocol: classical baselines get the same inputs and are tuned by cross-validation, hardware runs are compared with noise-free simulation on identical inputs, and hardware deviations are tested against the exact shot-noise expectation. In a pre-registered evaluation on untouched data, a 4-qubit QNN on sentence-encoder features is within about two points of tuned classical models on the same features and has no higher point estimate than any of them (sentiment 0.766 vs. 0.769; CVE severity 0.708 vs. 0.720, a tie within a pre-set ±3-point margin); a 1.5-point gap seen during design did not replicate. An ablation crossing encoding with re-uploading attributes most of the design effect to the encoding (19–24 points). The circuit's output lies exactly in a small Fourier basis; a classical model trained on that basis outperforms the QNN on CVE (0.727 vs. 0.708) and is inconclusive on sentiment (0.756 vs. 0.766). On IBM's ibm_marrakesh (200 inputs per task; three CVE runs, one sentiment run), no run's accuracy differs significantly from noise-free, but the mean output shifts towards one class in every run (−0.002 to −0.006). Single observed executions on two further Heron devices show the same sign with larger shifts (to −0.015); the device's noise model matched ibm_marrakesh but understated ibm_fez. In simulation, a trained two-copy QNN separates pure from mixed states with 16–32 copies per state from 2 to 6 qubits, against 128–4,096 for the classical-shadow baseline we test, illustrating a known multi-copy separation; in a preliminary 2-qubit hardware run on one shared 60-state set its copy ratio is 2.5–2.9 (job-conditional intervals above 1), with point estimates below the same-state noise-free ratio (6.3) but intervals too broad to establish a reduction. All code, results and job identifiers are archived.

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
