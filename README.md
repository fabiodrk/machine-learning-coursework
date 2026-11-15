# Machine learning coursework

Selected study notebooks from my machine-learning class activities. This repository shows practice with Python, scikit-learn, model comparison, and evaluation. It is coursework adapted from teaching scaffolding, including activities designed for pair work, rather than a collection of independent research projects.

## Explore the notebooks

| Notebook | Focus | Publication scope |
| --- | --- | --- |
| [01 · Regression and overfitting](notebooks/01-regression-and-overfitting.ipynb) | Linear regression, KNN, polynomial complexity, train/test MSE | Completed coding sections; fictional-country teaching data |
| [02 · Housing workflow](notebooks/02-housing-workflow.ipynb) | Inspection, preprocessing, baseline, CV, random-forest tuning | Completed coding sections; California housing fetched separately |
| [03 · Classification baselines](notebooks/03-classification-baselines.ipynb) | Stratification, scaling, logistic regression, KNN, random forest | Completed subset; unfinished later exercises omitted |
| [04 · Dimensionality reduction](notebooks/04-dimensionality-reduction.ipynb) | PCA, LDA, mutual information, noise features | Coding workflow; training CV selects the final representation |
| [05 · Decision trees](notebooks/05-decision-trees.ipynb) | Depth, boundaries, splitting criteria, probabilities, grid search | Working code; unfinished depth-summary table omitted |
| [06 · Ensembles](notebooks/06-ensemble-learning.ipynb) | Bagging, forests, extra trees, boosting, feature importance | Coding workflow; test-based model selection discussed as a limitation |

## Run locally

Use Python 3.11 in a fresh virtual environment:

```sh
python -m venv .venv
```

Activate it with `.venv\Scripts\activate` on Windows or `source .venv/bin/activate` on macOS/Linux, then:

```sh
python -m pip install -r requirements.txt
jupyter lab
```

Open a notebook and choose **Restart Kernel and Run All Cells**. No API key or cloud service is needed. Notebook 02 may download a dataset on its first run. The other notebooks use embedded teaching data, generated data, or datasets packaged with scikit-learn. Dataset descriptions and source references are in [ATTRIBUTION.md](ATTRIBUTION.md).

For a headless execution check of the five notebooks that need no dataset download:

```sh
python scripts/check_notebooks.py
```

To include the housing notebook, using a cached copy or allowing scikit-learn to download it:

```sh
python scripts/check_notebooks.py --include-downloads
```

The check runs the actual notebook code in order and prints tables and metrics. It closes plots without rendering a browser UI. It verifies execution, not scientific validity or visual layout. Notebooks are committed without saved outputs; rerunning them produces current results.

GitHub checks run the five offline notebooks and then the housing notebook in a separate step. That housing step requires the external dataset download to be available. To run only that notebook locally, use `python scripts/check_notebooks.py --include-downloads --notebook 02`.

## Concepts explored

- Training error can fall while unseen-data performance worsens.
- Scaling and feature transformations belong inside a cross-validation pipeline.
- Accuracy alone does not describe all classification errors.
- Variance retained by PCA and predictive usefulness answer different questions.
- Comparing many models on the same test set makes that set part of model selection.
- Feature importance is a property of a fitted model, not proof of causation.

## Interpretation

These are small educational experiments. The tree and ensemble activities reuse test observations for comparisons; their displayed scores are exploratory, not independent final estimates. The classification activities use a public research dataset for ML practice and have no clinical validation or diagnostic use. The dimensionality-reduction publication selects the final representation from training CV rather than keeping a hard-coded choice.

The SVM worksheet, teaching demos, supplied solution notebook, group assignment, course handouts, and restricted local data are omitted. See [ATTRIBUTION.md](ATTRIBUTION.md) for provenance and editorial changes.

