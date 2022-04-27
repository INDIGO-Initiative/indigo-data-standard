# indigo-data-standard

See https://indigo-data-standard.readthedocs.io


## Developers & Working with versions in GitHub / ReadTheDocs

New work should be done on a separate branch. Merge to `main` branch when ready. 
Update the changelog in `docs/versions_changelog.rst` as you work. 
(Have an "Unreleased" section at the top.)

When you want to release a new version, 
* Update `docs/versions_changelog.rst` with the new version number and release date. Merge these changes to `main`.
* Create a tag at the last commit on `main`. The tag name should be `MAJOR.MINOR.PATCH`.

The changes should also be placed on the correct branch, `MAJOR.MINOR` (no `PATCH`).

If the branch already exists:
* Move the changes to the correct branch.

If the branch does not already exist:
* Create the branch from the last commit on `main`.
* Go to GitHub settings and protected branches and set up protection for this new branch. The options should be the same as on the `main` branch.
* Go to ReadTheDocs and enable public builds for this new branch.

Finally,
* Verify that `https://indigo-data-standard.readthedocs.io/en/MAJOR.MINOR/` updates as expected 
* Verify that https://indigo-data-standard.readthedocs.io/en/stable/ updates as expected



