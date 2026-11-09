# Honest Quantum Machine Learning on Real IBM Hardware

Vivek Reddy · November 9, 2026

Quantum machine learning beat classical methods only when the data was itself quantum. Over two projects we trained small quantum neural networks, ran them on IBM's 156-qubit `ibm_marrakesh`, and held every result against a fair classical baseline.

Three findings stand out:

- **On ordinary data, quantum never won.** A 4-qubit classifier for movie-review sentiment and CVE severity came within about 1 point of a classical model given the same inputs, and never clearly beat it.
- **Real hardware was better than its reputation.** On the same test samples, `ibm_marrakesh` gave exactly the noise-free answers on 4 of 5 datasets. Repeated runs showed the one drop was shot noise, not device error.
- **On quantum data, the gap was exponential.** Telling pure from mixed quantum states took a 2-copy quantum model about 32 copies at every size from 2 to 6 qubits. The classical method needed 128 copies at 2 qubits and 4,096 at 6.

## Why honest benchmarking matters

A quantum accuracy number means little on its own. "Our quantum model scored 80%" says nothing if a classical model on the same inputs scores 85%. Demos often leave that comparison out. We held ourselves to four rules:

1. **Same inputs.** Classical baselines see exactly the features the quantum circuit sees, so the comparison isolates the model.
2. **A strong classical ceiling.** We also report the best practical classical model, trained on all the data, so a quantum win can't come from a weak baseline.
3. **Same samples on hardware.** Real-device runs use a subset of the test set to save quantum time, so we compare them only with the noise-free simulator on those exact samples.
4. **Repeat before concluding.** A surprising hardware number gets rerun, and checked against the variation expected from finite sampling (shot noise).

Rule 3 mattered in practice. Our first hardware chart put a 40-sample hardware score beside 200-sample simulator scores. It made the device look better than the simulator on one dataset, purely because the question sets differed.

## Project 1: a quantum text classifier

The first project asks the obvious question: can a small quantum circuit classify everyday text? The answer: about as well as a classical model handed the same 4 numbers, and no better.

The pipeline is hybrid. A sentence-embedding model turns each text into 384 numbers. Partial least squares (PLS) squeezes those to the 4 directions that best predict the label. A 4-qubit circuit makes the final call. We tested two tasks: movie-review sentiment (Rotten Tomatoes, 10,662 sentences), and CVE severity, predicting from a vulnerability's description whether it is rated high/critical (12,116 NVD entries from early 2024, tested on CVEs published after the training ones).

| Task | Always guess the common class | Quantum, 4 qubits | Classical, same 4 numbers | Classical, full embedding |
| --- | --- | --- | --- | --- |
| Sentiment (1,066 test sentences) | 0.500 | 0.758 | 0.769 | 0.774 |
| CVE severity (2,424 test CVEs) | 0.578 | 0.699 | 0.692 | 0.715 |

**Circuit design mattered more than qubit count.** Our first circuit used the textbook `ZZFeatureMap` encoding, read out the parity of all qubits, and trained on sampled measurement counts. It barely beat a coin flip. Three changes fixed it:

- plain angle encoding, re-uploading the input before each trainable layer
- reading out a single qubit
- training on exact simulated probabilities

Breast-cancer accuracy rose from 0.68 to 0.92. The same lesson applied to the classical side: on text, supervised PLS beat unsupervised PCA by about 15 points, because it keeps the label-relevant directions.

## On real hardware: closer to ideal than expected

We ran the trained circuits on `ibm_marrakesh` through IBM's free Open Plan, 1,024 shots per input. On 4 of 5 datasets, the device gave exactly the answers of the noise-free simulator on the same test samples.

| Dataset | Test samples | Noise-free simulator | ibm_marrakesh |
| --- | --- | --- | --- |
| Breast cancer | 40 | 0.875 | 0.875 |
| Iris | 30 | 0.900 | 0.900 |
| Two moons | 40 | 0.900 | 0.900 |
| Sentiment | 40 | 0.675 | 0.675 |
| CVE severity | 40 | 0.725 | 0.650 |

The circuit is small after compiling for the device: depth 37, with 6 two-qubit gates. Noise still nudges every probability, but rarely across the 0.5 decision line.

**The CVE drop was luck, not the device.** We reran the same 40 CVE inputs 3 more times. Accuracy came out 0.725, 0.675 and 0.700. Five answers flipped in total, where shot noise alone predicts 3.45 (a gap that large arises by chance about 27% of the time). No input flipped in every run, and every flipped input sat within 0.025 of the 0.5 line.

**Simulated noise was too pessimistic.** Qiskit's `FakeManilaV2` noise model, based on an older 5-qubit device, shifted scores 5 times more than the real machine (−0.030 vs −0.006 on average). It also flipped 2 inputs in every run. Benchmarks that rely only on such models may understate today's hardware.

## Project 2: quantum-native data

If quantum models have an edge, theory says it is on data that is quantum to begin with. The second project, Entangle, classifies quantum states directly, comparing a quantum model with classical methods that only see measurement results.

**Entanglement (2 to 4 qubits).** A quantum model that receives two copies of each state at once (a "2-copy" model) told entangled from unentangled states perfectly, 1.000. The same model with one copy stayed at chance, about 0.50: its output is a linear function of the state, and entanglement is not. Classical models given the raw state vectors also struggled, around 0.55 at 3 qubits. But classical models given 256 random-measurement snapshots ("classical shadows") reached 0.94 to 0.99 (best model at each size). So quantum access helps here, but classical shadows close most of the gap.

**Phases of matter.** Classifying ground states of the Ising spin chain (4 to 8 qubits) gave no quantum edge: every model, quantum or classical, scored 0.96 to 1.00. A toy lattice gauge theory gave the same picture. The tutorial version of the quantum convolutional network (QCNN) also output a constant 0.5 on these symmetric states, so we replaced its building blocks.

**Pure or mixed: an exponential gap.** Here theory predicts that single-copy strategies need exponentially many copies as the system grows, while a 2-copy test needs a fixed number. The experiment reproduced that cleanly:

![Copies needed for 90% accuracy: classical shadows double with each qubit, the 2-copy quantum model stays flat at about 32](copies_for_90pct.png)

*Source: Entangle stage 5 ([results/stage5_purity.md](https://github.com/H3XY/Entangle/blob/main/results/stage5_purity.md)), exact simulation, 200 training and 400 test states per size, 3 seeds.*

One caveat: this confirms a known theoretical separation (multi-copy quantum learning) at small scale rather than discovering a new one. The 2-copy model also needed care to train. At 5 qubits it hit a barren plateau, where gradients vanish; sharing one block of weights across copy pairs fixed it.

## What we learned

Quantum models earned their place in only one setting: quantum data that can be loaded two copies at a time. Everywhere else, a well-built classical model matched them.

| Setting | Quantum edge? | Why |
| --- | --- | --- |
| Everyday data (text, medical, synthetic) | No | A classical encoder does the heavy lifting; the circuit only classifies 4 numbers |
| Quantum data, one copy at a time | No | The model's output is linear in the state; classical shadows do as well |
| Phases of matter, lattice gauge toy | No | Every model scores 0.96 to 1.00 |
| Quantum data, two copies at once | Yes, exponential | Purity needs a fixed ~32 copies vs 128 to 4,096 for classical shadows |

Practical lessons for anyone trying this:

- **Design the circuit before adding qubits.** Encoding and readout choices moved accuracy by 25 points; qubit count did not.
- **Test small circuits on real hardware.** A depth-37 circuit was effectively noise-free on a current IBM processor, and older noise models overstate the damage.
- **Expect tooling friction.** Both projects hit the same bug: `qiskit-ibm-runtime` 0.44.1 claims Qiskit 1.x support but breaks real-device compiling on it. We reported it as [Qiskit/qiskit-ibm-runtime#3563](https://github.com/Qiskit/qiskit-ibm-runtime/issues/3563).
- **Run it on a free plan.** All hardware runs fit within IBM's free Open Plan, using a few minutes of quantum time.

## Limitations and what's next

These are small experiments, and they should be read that way:

- **Small scale.** At most 8 qubits, simulated exactly, so nothing here is beyond classical computers.
- **Small hardware samples.** 30 to 40 test inputs per dataset on the device for project 1, and 10 states per task for Entangle. Enough for an end-to-end check, not for fine-grained accuracy claims.
- **A known result.** The exponential gap matches the multi-copy separation proven by Huang et al. in ["Quantum advantage in learning from experiments"](https://arxiv.org/abs/2112.00778). We reproduce it on a small scale; we do not claim a new one.
- **Approximate labels.** Predicting CVE severity from the description alone approximates CVSS, which also scores attack vector, privileges and impact.

Next steps:

- Run the 2-copy purity test on real hardware, where copies must be prepared side by side.
- Push the hardware study past where noise starts to matter: more qubits, deeper circuits, and a plot of accuracy loss against two-qubit gate count.
- Test whether classical models built to mimic quantum circuits ("dequantized" models) can match the quantum ones on the text tasks.

Code, data pipelines and every result file live in two repositories: [H3XY/AGI](https://github.com/H3XY/AGI) (project 1) and [H3XY/Entangle](https://github.com/H3XY/Entangle) (project 2). Each reproduces its numbers with one command per experiment.
