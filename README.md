![](static/card.png)

# Tupy: A Lightweight Energy Optimization Package for PyTorch (and TinyGrad Soon!)

Tupy is a streamlined package aimed at optimizing energy consumption for PyTorch-based AI models and, eventually, TinyGrad. By tracking and minimizing resource usage during training and inference, Tupy empowers developers and researchers to reduce the carbon footprint of their AI projects without compromising model performance. This tool is ideal for anyone looking to incorporate sustainable practices into their machine learning workflows, especially in resource-constrained environments.

> Tupy comes from *Tupã*, which means "Thunder" in [Tupi](https://en.wikipedia.org/wiki/Tupi_language), the largest indigenous language in Brazil.

### Features
- Real-time energy monitoring
- Real-time optimization of energy consumption
- Support for PyTorch

### Directory Structure

```
tupy/
├── src/
│   ├── __init__.py
│   ├── monitor.py
│   ├── optimizer.py
│   └── callbacks.py
├── tests/
│   ├── __init__.py
│   ├── test_monitor.py
│   ├── test_optimizer.py
│   └── test_callbacks.py
├── docs/
│   └── index.md
├── setup.py
└── README.md
``` 

### Installation
```python
pip install tupy
```