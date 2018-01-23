---
layout: default
---

# YASET - Yet Another SEquence Tagger

## What is YASET

`yaset` is a sequence tagger written in [Python](https://www.python.org/). 
This tool can be used for various NLP-related sequence tagging tasks 
(e.g. [Named Entity Recognition](https://en.wikipedia.org/wiki/Named-entity_recognition) 
or [Part-of-Speech tagging](https://en.wikipedia.org/wiki/Part-of-speech_tagging)). 
It implements state-of-the-art deep learning algorithms for sequence tagging from 
the NLP community.

## Algorithms

Currently, one algorithm is implemented in `YASET` but others will follow:

* BiLSTM-Char-CRF ([Lample et al., 2016](http://dx.doi.org/10.18653/v1/N16-1030))

## Installation

1. You need a working **Python 3.3+** environment

2. Download the last version of the tool (current version: 0.3.0)
```bash
wget https://github.com/jtourille/yaset/archive/0.3.0.tar.gz
```

2. Decompressed the archive
```bash
tar xzf 0.3.0.tar.gz
```

3. Move into the newly created directory
```bash
cd yaset-0.3.0
```

4. Install the tool into your python environment
```
pip install .
```

## Documentation

The documentation is available at this location: [http://yaset.readthedocs.io](http://yaset.readthedocs.io)

## Contributors

* Principal contributors: [Julien Tourille](https://jtourille.github.io/), [Olivier Ferret](http://oferret.free.fr/), [Aurélie Névéol](https://perso.limsi.fr/neveol/), [Xavier Tannier](http://xavier.tannier.free.fr/index.php)
* Other contributor: Pierre Magistry

## Acknowledgements

This work was supported by [Labex Digicosme](https://digicosme.lri.fr), operated by the Foundation for Scientific Cooperation (FSC) Paris-Saclay, under grant CÔT and by the French National Agency for Research under grant [CABeRneT](https://cabernet.limsi.fr/) ANR-13-JS02-0009-01.