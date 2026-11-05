# Wilson–Cowan equations: from a single region to the whole-brain connectome

**Antonio B. Marín-Carballo** ([GitHub](https://github.com/MarinCarballo)) and **ZhuoZhuo Liu**
University of Granada, 2025

📄 [Paper](paper/paper.pdf) · 🎞️ [Slides](https://github.com/liuzhuozhuo/wilson-cowan/releases/download/v1.0/slides.pptx) · 🎬 [Animations](https://github.com/liuzhuozhuo/wilson-cowan/releases/tag/v1.0)

## Abstract

The Wilson–Cowan model describes the dynamics of interacting excitatory and inhibitory neuron populations. In this study, we explore the fundamental behavior of this model, beginning with a simplified single-region system. Through linear stability analysis and bifurcation theory, we identify distinct dynamical regimes (quiescent, oscillatory, and bistable) and classify their transitions via Hopf, Pitchfork, Saddle-Node, and Takens–Bogdanov bifurcations.

Building on this, we expand the model to a network of interconnected brain regions using structural data encoded in an adjacency matrix. By computing the Adjacency Matrix eigenvalues, we uncover universal patterns in healthy brains. By solving the eigenvalue problem for the corresponding connectome Laplacian, we obtain the harmonic modes of brain organization. We use these to analyze whole-brain dynamics, quantifying synchronization across regions using the Kuramoto order parameter.

Additionally, we consider stochastic extensions of the Wilson–Cowan equations via a master equation approach and derive their corresponding Fokker–Planck and Langevin formulations.

## The model (Sec. II, Fig. 1)

$$
\tau_E \frac{dE}{dt} = -E + S(w_{EE}E - w_{EI}I + P_E), \qquad
\tau_I \frac{dI}{dt} = -I + S(w_{IE}E - w_{II}I + P_I),
$$

with $S(x) = \tanh(x)$, so that $E, I \in [-1, 1]$.

| Code | Result |
|---|---|
| [`01_model/model_diagram.py`](01_model/model_diagram.py) | Fig. 1: E–I circuit illustration (Manim) |
| [`01_model/sigmoid_function.py`](01_model/sigmoid_function.py) | Logistic vs. tanh activation (Manim) |

## Results

### A. Single region: dynamical regimes and bifurcations (Sec. II.A, Fig. 2)

Taking $\tau_{E,I}=1$, $P_{E,I}=0$ and fixing $(w_{II}, w_{EI}) = (1, 10)$, the $(w_{EE}, w_{IE})$ plane splits into **quiescent**, **oscillatory** and **bistable** regimes, separated by Hopf, Pitchfork, Saddle-Node and Takens–Bogdanov bifurcations.

![Fig. 2](02_single_region/figures/fig2.png)
*Fig. 2: Left: phase diagram in the $(w_{EE}, w_{IE})$ plane. Right: phase portraits for (A) quiescent, (B) oscillatory, (C, D) bistable.*

| Code | Result |
|---|---|
| [`02_single_region/phase_diagram.ipynb`](02_single_region/phase_diagram.ipynb) | Fig. 2 (left): phase diagram in $(w_{EE}, w_{IE})$ → [`figures/phase_diagram.pdf`](02_single_region/figures/phase_diagram.pdf) |
| [`02_single_region/phase_portraits.ipynb`](02_single_region/phase_portraits.ipynb) | Fig. 2 (right): phase portraits per regime → `figures/{quiescent,oscillatory,bistable}_*.pdf`, animations: [quiescent](https://github.com/liuzhuozhuo/wilson-cowan/releases/download/v1.0/single-region_quiescent.mp4), [oscillatory](https://github.com/liuzhuozhuo/wilson-cowan/releases/download/v1.0/single-region_oscillatory.mp4), [bistable](https://github.com/liuzhuozhuo/wilson-cowan/releases/download/v1.0/single-region_bistable.mp4) |

Saddle-node illustrations: [`figures/saddle-node_bifurcation.png`](02_single_region/figures/saddle-node_bifurcation.png), [`figures/saddle-node_limit_cycle.png`](02_single_region/figures/saddle-node_limit_cycle.png).

### B. Brain structure: adjacency matrix and connectome harmonics (Sec. II.B, Fig. 3)

Structural connectomes of 88 subjects (Schaefer-200 + Tian-16 parcellation, 216 nodes) are used to study the adjacency spectrum and degree distribution across individuals, and the Laplacian eigenmodes $L = D - A$ (connectome harmonics).

![Fig. 3](03_brain_structure/figures/fig3.png)
*Fig. 3: (A) connectome nodes, (B) adjacency matrix, (C) Laplacian harmonic modes, (D) Laplacian eigenvalue and (E) degree distributions across 88 subjects.*

| Code | Result |
|---|---|
| [`03_brain_structure/connectome.ipynb`](03_brain_structure/connectome.ipynb) | Fig. 3A: connectome rendered on the brain → `figures/connectome_view_*.png`, interactive [`output/hcp_MEG_connectome.html`](03_brain_structure/output/hcp_MEG_connectome.html)<br>Fig. 3B: adjacency matrix → [`figures/Adjacency.pdf`](03_brain_structure/figures/Adjacency.pdf) |
| [`03_brain_structure/laplacian.ipynb`](03_brain_structure/laplacian.ipynb) | Fig. 3C: Laplacian harmonic modes → `figures/mode{1,2,3}{,_side}.pdf`<br>Universality across subjects → [`figures/eigenvalues_univ.pdf`](03_brain_structure/figures/eigenvalues_univ.pdf), [`figures/degrees_univ.pdf`](03_brain_structure/figures/degrees_univ.pdf) |

### C. Brain dynamics: Kuramoto order parameter (Sec. II.C, Fig. 4)

Coupling one Wilson–Cowan unit per node through the connectome, synchronization is measured with the Kuramoto order parameter $r$. The resulting phase diagram resembles, but does not equal, the single-region one — *more is different*.

![Fig. 4](04_brain_dynamics/figures/fig4.png)
*Fig. 4: Left: mean Kuramoto order parameter $r$. Right: node trajectories in the $(E, I)$ plane for (A) quiescent, (B) oscillatory, (C, D) bistable.*

| Code | Result |
|---|---|
| [`04_brain_dynamics/kuramoto.ipynb`](04_brain_dynamics/kuramoto.ipynb) | Fig. 4 (left): mean $r$ over $(w_{EE}, w_{IE})$ → [`figures/kuramoto.pdf`](04_brain_dynamics/figures/kuramoto.pdf), data in [`results/`](04_brain_dynamics/results) |
| [`04_brain_dynamics/three_regimes.ipynb`](04_brain_dynamics/three_regimes.ipynb) | Fig. 4 (right): node trajectories in the $(E, I)$ plane per regime → `figures/{quiescent,oscillatory,bistable}_wEE_*.pdf`, animations: see below |

**Animations** (whole-brain, one trajectory per node):

| Regime | E–I phase plane | 3D brain + phase plane |
|---|---|---|
| Quiescent ($w_{EE}=2$) | [mp4](https://github.com/liuzhuozhuo/wilson-cowan/releases/download/v1.0/brain_quiescent_phase-plane.mp4) | [mp4](https://github.com/liuzhuozhuo/wilson-cowan/releases/download/v1.0/brain_quiescent_wEE2_3d-phase.mp4) |
| Oscillatory ($w_{EE}=15$) | [mp4](https://github.com/liuzhuozhuo/wilson-cowan/releases/download/v1.0/brain_oscillatory_phase-plane.mp4) | [mp4](https://github.com/liuzhuozhuo/wilson-cowan/releases/download/v1.0/brain_oscillatory_wEE15_3d-phase.mp4) |
| Bistable ($w_{EE}=15$) | [mp4](https://github.com/liuzhuozhuo/wilson-cowan/releases/download/v1.0/brain_bistable_phase-plane.mp4) | [mp4](https://github.com/liuzhuozhuo/wilson-cowan/releases/download/v1.0/brain_bistable_wEE15_3d-phase.mp4) |
| $w_{EE}=27,\ w_{IE}=2$ | [mp4](https://github.com/liuzhuozhuo/wilson-cowan/releases/download/v1.0/brain_wEE27_wIE2_phase-plane.mp4) | [mp4](https://github.com/liuzhuozhuo/wilson-cowan/releases/download/v1.0/brain_wEE27_wIE2_3d-rotating.mp4) |

Whole-brain activity in 3D: [`brain_3d.mp4`](https://github.com/liuzhuozhuo/wilson-cowan/releases/download/v1.0/brain_3d.mp4)

The network simulation cells at the end of `03_brain_structure/connectome.ipynb` also write the bistable trajectory figures into `04_brain_dynamics/figures/`.

### Appendices

Appendix A (analytical bifurcations) and Appendix B (stochastic brain dynamics: master equation → Fokker–Planck / Langevin) are analytical and are contained in the [paper](paper/paper.pdf).

## Repository layout

```
paper/                 paper.pdf
data/                  HCP structural connectomes (88 subjects) + parcellation coordinates
01_model/              Fig. 1  – model illustrations (Manim)
02_single_region/      Sec. II.A, Fig. 2 – phase diagram, phase portraits, bifurcations
03_brain_structure/    Sec. II.B, Fig. 3 – adjacency matrix, spectra, Laplacian harmonics
04_brain_dynamics/     Sec. II.C, Fig. 4 – whole-brain simulation, Kuramoto order parameter
```

Each section folder contains its notebooks plus `figures/` (and `videos/`, `results/` where relevant). Run notebooks from their own folder; data is read from `../data/`.

Animations (`*.mp4`) and slides are not tracked in git. They are attached to the [v1.0 release](https://github.com/liuzhuozhuo/wilson-cowan/releases/tag/v1.0). Re-running a notebook writes its videos into the local `videos/` folder, which git ignores.

**Dependencies:** `numpy`, `scipy`, `pandas`, `matplotlib`, `numba`, `joblib`, `tqdm`, `nilearn`, `manim` (for `01_model/`), and `ffmpeg` for animations.

## Use of AI Tools

This project uses [ChatGPT](https://openai.com/chatgpt) (GPT-4o and GPT o4-mini-high) to assist in the following aspects:
- Function generation in the code
- Debugging and optimization

All AI-generated content was reviewed and verified before inclusion.
