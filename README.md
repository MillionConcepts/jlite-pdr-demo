# pdr-demo

This is a deployment repository for a GitHub Pages site containing a 
JupyterLite version of the [`pdr`](https://github.com/millionConcepts/pdr) 
example Notebook.

The deployed Notebook can be found at https://millionconcepts.github.io/jlite-pdr-demo.

This repository is based on the official JupyterLite Pages deployment template: 
https://github.com/jupyterlite/demo

If you would like to build and run this site locally, create a conda environment
using the `pdr-demo-build.yml` environment file, then, from the repository root
directory, run `jupyter lite build --contents content` followed by `jupyter lite serve`.
