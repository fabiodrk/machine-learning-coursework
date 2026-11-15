# Attribution and publication scope

The source material is the user's local machine-learning coursework under `C:\MCS\Machine Learning`, weeks 1–6, with filenames beginning `ML_CSAI500` or `MCAI500`, plus `Module_4_Dimensionality_Reduction_Activity.ipynb`.

The class supplied instructional structure, starter code, examples, and prompts. Some worksheets explicitly asked students to work in pairs. This repository does not claim that every retained line was independently authored by Fabio or that paired contributions can be separated. It presents the completed local coding work as an adapted learning record. The instructor and any activity partners are not named because their identities and individual contributions were not established from these files.

Full worksheet narratives, teaching demos, supplied solutions, group assignments, original notebook outputs, and course documents are not republished. The selected code is reorganized into newly introduced study extracts using common Python/scikit-learn APIs. This is an attribution record, not a grant of rights to third-party teaching material or datasets; no blanket license is applied to them.

## Dataset references

- Week 1: the local worksheet's small embedded teaching table uses fictional country names. It should not be interpreted as observed national statistics. The worksheet identifies inspiration from the machine-learning-landscape example; its supplied solution is not included.
- Week 2: California housing is obtained through scikit-learn's `fetch_california_housing`. No cached data is bundled. Refer to the dataset's `DESCR` and the [scikit-learn dataset description](https://scikit-learn.org/stable/datasets/real_world.html#california-housing-dataset) for the original source and usage context.
- Weeks 3 and 6: scikit-learn's `load_breast_cancer` research dataset. The data is loaded through the library; original source details are available in `DESCR` and the [dataset description](https://scikit-learn.org/stable/datasets/toy_dataset.html#breast-cancer-wisconsin-diagnostic-dataset).
- Week 4: scikit-learn's `load_wine` dataset. Source details are in `DESCR` and the [dataset description](https://scikit-learn.org/stable/datasets/toy_dataset.html#wine-recognition-dataset).
- Week 5: synthetic samples from `make_moons`, generated with a fixed seed.

## Editorial changes made for publication

- Extract completed code cells and replace worksheet prompts with brief new context.
- Remove saved outputs, execution counts, personal metadata, and assignment identifiers.
- Keep partial activities explicitly partial. Do not implement unanswered sections and present them as class work.
- Remove a duplicate assignment in the classification target recoding.
- Use one worker for model searches to make local execution less resource-intensive.
- Select the dimensionality-reduction representation from its existing training-CV comparison table rather than a hard-coded model name.
- Add reproducible setup, a headless execution checker, and GitHub execution checks.
- Add discussion of repeated test-set use and medical-data interpretation limits. This commentary was added during portfolio preparation and is not represented as the original class submission.

Original class folders remain unchanged.
