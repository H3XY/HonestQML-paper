# Honest Quantum Machine Learning on Real IBM Hardware

Vivek Reddy · November 9, 2026

Quantum machine learning beat classical methods only when the data was itself quantum. Over two projects we trained small quantum neural networks, ran them on IBM's 156-qubit `ibm_marrakesh`, and held every result against a fair classical baseline.

Three findings stand out:

- **On ordinary data, quantum did not win.** A 4-qubit classifier for movie-review sentiment and CVE severity came within 1.5 points of tuned classical models given the same inputs: slightly but measurably worse on sentiment, tied on CVE.
- **Real hardware stayed close to ideal for these small circuits.** On 200 inputs per task, `ibm_marrakesh` was as accurate as the noise-free simulator within statistical error, but it shifted every output slightly in one direction, a small bias we could measure.
- **On quantum data, a two-copy model needed far fewer copies.** Telling pure from mixed states took the tested two-copy model 16 to 64 copies at every size from 2 to 6 qubits in simulation; the classical method we tested needed 128 at 2 qubits and up to 4,096 at 6. On the real device, at 2 qubits, the gap held but halved. That illustrates a known theoretical result rather than a new one.

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

| Model (mean over 3 training seeds) | Sentiment (1,066 test sentences) | CVE severity (2,424 test CVEs) |
| --- | --- | --- |
| Always guess the common class | 0.500 | 0.578 |
| Quantum, 4 qubits | 0.757 | 0.699 |
| Classical, same 4 numbers, tuned | 0.772 | 0.691 |
| Classical, full embedding | 0.774 | 0.715 |

On sentiment the quantum model was about 1.5 points behind in every seed, a small but statistically clear gap. On CVE it was nominally ahead, but within the margin of error.

**One design choice mattered far more than the rest.** Our first circuit used the textbook `ZZFeatureMap` encoding and barely beat a coin flip on our benchmark. A controlled test, changing one thing at a time over three seeds, pinned it down: that encoding alone cost 21 points on breast cancer (0.91 vs 0.70).

- re-uploading the input before each layer: about 2 points
- reading one qubit instead of all of them: about 1 point, in the other direction
- the optimizer, and training on exact vs sampled probabilities: about 1 point each
- 2, 4 or 6 qubits: within about 1 point

Everything else was noise next to the encoding. On the classical side, supervised PLS beat unsupervised PCA by about 15 points on text, because it keeps the label-relevant directions.

## On real hardware: closer to ideal than expected

We ran the trained sentiment and CVE classifiers on `ibm_marrakesh` through IBM's free Open Plan: 200 test inputs per task, 1,024 shots per input, no error mitigation, and the same four physical qubits in every run. We compared each run with the noise-free simulator on the same inputs, and with two simulated noise models.

| Task | Noise-free | ibm_marrakesh, per run | Bias in P(class 1) [95% CI] |
| --- | --- | --- | --- |
| CVE severity | 0.685 | 0.685, 0.655, 0.700 | −0.005 [−0.007, −0.003] |
| Sentiment | 0.740 | 0.730 | −0.004 [−0.006, −0.001] |

**Accuracy: no detectable difference.** With 200 inputs, each accuracy is uncertain by about ±6.5 points. We ran CVE three times, the last one three hours after the first two. The number of predictions that changed was at the edge of what 1,024-shot sampling alone predicts: 19 against 13.3 expected over the three CVE runs (an exact test gives p = 0.055), and 4 against 3.1 for sentiment (p = 0.37). Repeated runs agreed on 96% of predictions. The compiled circuit is small: depth 37, six two-qubit gates.

**Bias: small but real, and it drifts.** The device pushed every output slightly toward "negative" and "low/medium", by about 0.004 to 0.005, with confidence intervals that exclude zero. Its size changed between sessions: per CVE run it was 0.006 and 0.005, then 0.002 three hours later, even though IBM reported the same calibration for those qubits. That is too small to move accuracy at this sample size, but it tips inputs that sit near the 0.5 line, which is why an earlier 40-input run happened to lose 3 CVE answers.

**Match the noise model to the device.** Qiskit's simulated copy of the same machine (`FakeMarrakesh`) reproduced both the accuracy and the bias. A simulated copy of an older 5-qubit device (`FakeManilaV2`) overstated the bias about fivefold and changed significantly more predictions than chance allows.

## Project 2: quantum-native data

If quantum models have an edge, theory says it is on data that is quantum to begin with. The second project, Entangle, classifies quantum states directly, comparing a quantum model with classical methods that only see measurement results.

**Entanglement (2 to 4 qubits).** A quantum model that receives two copies of each state at once (a "2-copy" model) told entangled from unentangled states perfectly in exact simulation, and 0.99 to 1.00 with 256 copies, over five seeds. The same circuit with one copy stayed at chance, about 0.50. That is expected for this model: with one copy, its output probability is a linear function of the state, and this entanglement label is not; it does not mean every single-copy method fails. Classical models given the raw state vectors also struggled: 0.72, 0.57 and 0.52 at 2, 3 and 4 qubits. But classical models given 256 random-measurement snapshots ("classical shadows") reached 0.95, 0.98 and 0.99, within 0.04 to 0.01 of the quantum model. So this task does not separate the two.

**Phases of matter.** Classifying ground states of the Ising spin chain (4 to 8 qubits) gave no quantum edge: every model, quantum or classical, scored 0.96 to 1.00. A toy lattice gauge theory gave the same picture. The task turned out to be easy: a logistic regression on a single number, such as the average magnetisation, scores 0.99 or better. Every model's mistakes sit near the phase transition, about a fifth of the test states. The tutorial version of the quantum convolutional network (QCNN) also output a constant 0.5 on these symmetric states, so we replaced its building blocks.

**Pure or mixed: a gap that doubles per qubit.** Here theory predicts that single-copy strategies need exponentially many copies as the system grows, while a 2-copy test needs a fixed number. In our simulated test, the learned 2-copy model reached 90% accuracy with 16 to 64 copies per training seed at every size, while the classical-shadow method we tested needed 128 copies at 2 qubits and up to 4,096 at 6:

![Copies needed for 90% accuracy: classical shadows double with each qubit, the 2-copy quantum model stays flat at about 32](copies_for_90pct.png)

One caveat: this confirms a known theoretical separation (multi-copy quantum learning) at small scale rather than discovering a new one. The 2-copy model also needed care to train. With separate weights for each copy pair, one of three training runs failed at 5 qubits. We then measured why: at random starting points the gradients shrink about 4× per added qubit, the "barren plateau" effect. Sharing one block of weights across copy pairs slowed that to 1.7× per qubit, and training worked.

**Pure or mixed on the real device.** We ran the 2-qubit version on `ibm_marrakesh` twice, on 60 test states with 1,024 copies each. Pure and mixed states were prepared with circuits of the same depth, so the device could not tell them apart by circuit length. With all 1,024 copies, every model scored 0.99 to 1.00. With fewer copies the gap showed, but smaller than in simulation:

| Copies of each state needed for 90% | Noise-free simulation | ibm_marrakesh |
| --- | --- | --- |
| 2-copy quantum model | 32 | 64 |
| Classical shadows | 128 | 128 |

![Accuracy against copies on ibm_marrakesh (solid) and its simulated noise model (dashed): the 2-copy model stays ahead of classical shadows, but less so on the real device](hw_purity.png)

The 2-copy circuit is about three times deeper than a shadow circuit (19 two-qubit gates after compiling, against 7), so it picks up more noise. Here Qiskit's simulated copy of the device understated that noise by about 2.5×, unlike for the shallow text classifier. Entangle's entanglement and phase classifiers also ran on the device (40 states, two runs). After a small recalibration on labelled device states they stayed at 0.93 to 0.99, but with so few states no ranking between models is statistically meaningful.

## What we learned

In our tests, the quantum models showed an edge in only one setting: quantum data that can be loaded two copies at a time. Everywhere else, a well-built classical model matched them.

| Setting we tested | Quantum edge? | Why |
| --- | --- | --- |
| Everyday data (text, medical, synthetic) | No | A classical encoder does the heavy lifting; the circuit only classifies 4 numbers |
| Quantum data, one copy at a time | No | This model's output is linear in the state; classical shadows do as well |
| Phases of matter, lattice gauge toy | No | Every model scores 0.96 to 1.00, so the task may be too easy to separate models |
| Quantum data, two copies at once (simulated; 2 qubits on hardware) | Yes, for this purity test | 16 to 64 copies vs 128 to 4,096 for the classical-shadow method; on hardware 64 vs 128 |

Practical lessons for anyone trying this:

- **Choose the encoding before adding qubits.** In our ablation the data encoding moved accuracy by 21 points; going from 2 to 6 qubits moved it by about 1.
- **Test small circuits on real hardware, and look past accuracy.** For these shallow circuits the device matched the noise-free accuracy, but it still carried a small, measurable bias in its outputs.
- **Use a noise model of the same device, and still check it.** A simulated copy of `ibm_marrakesh` predicted the shallow text circuit's behaviour; a model of an older device did not. For the deeper 2-copy circuit, even the same-device model understated the noise.
- **Expect tooling friction.** Both projects hit the same bug: `qiskit-ibm-runtime` 0.44.1 claims Qiskit 1.x support but breaks real-device compiling on it. One pinned the package, the other changed a compiler setting. We reported it as [Qiskit/qiskit-ibm-runtime#3563](https://github.com/Qiskit/qiskit-ibm-runtime/issues/3563).
- **Run it on a free plan.** All hardware runs fit within IBM's free Open Plan, a rolling 10 minutes per 28 days.

## Limitations and what's next

These are small experiments, and they should be read that way:

- **Small scale.** At most 8 qubits, simulated exactly, so nothing here is beyond classical computers.
- **Small hardware samples.** On the device, project 1 used 200 test inputs per task, with three CVE runs and one sentiment run on one day. Entangle's hardware runs used 40 to 60 states and two runs each, and the purity test ran on hardware only at 2 qubits: larger versions need deeper circuits than the device can run cleanly. Enough to measure accuracy and bias, not to rank models within a task.
- **A known result.** The purity gap matches the multi-copy separation proven by Huang et al. in ["Quantum advantage in learning from experiments"](https://arxiv.org/abs/2112.00778). We illustrate it at small scale against one classical method; we do not claim a new or general separation.
- **Approximate labels.** Predicting CVE severity from the description alone approximates CVSS, which also scores attack vector, privileges and impact.

Next steps:

- Run the purity test on hardware at 3 or more qubits, which will need error mitigation or a less noisy device.
- Push the hardware study past where noise starts to matter: more qubits, deeper circuits, and a plot of accuracy loss against two-qubit gate count.
- Test whether classical models built to mimic quantum circuits ("dequantized" models) can match the quantum ones on the text tasks.

Code, data pipelines and every result file live in two repositories: [H3XY/AGI](https://github.com/H3XY/AGI) (project 1) and [H3XY/Entangle](https://github.com/H3XY/Entangle) (project 2). Each reproduces its numbers with one command per experiment.
