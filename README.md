# 🏠 Marketing House

A collection of AI/ML/DL notebooks and demo applications for enterprise marketing use cases.

![Marketing House](https://your-logo-url-here.png)

## 📋 Overview

Marketing House provides ready-to-use AI and machine learning solutions tailored for marketing professionals and data scientists. This repository contains notebooks, demonstration applications, and resources for implementing advanced analytical techniques in marketing contexts.

## 🏷️ Artifact Labels

- 🧪 - Artifacts particularly suitable for exploratory data analysis, evaluating causal effects, and feasibility studies
- 🚀 - Conceptual prototypes using advanced methods (not necessarily suitable for productization)
- 📚 - Educational notebooks demonstrating basic algorithms

## 🎯 Use Cases

Our collection includes the following categories of solutions:

### 🛒 Promotions, Offers, and Advertisements
- **Customer Propensity Scoring** Using Deep Learning (LSTM with Attention)
- **Customer-level Uplift Modeling** Based On Observational Data Using Causal Inference 🧪
- **Customer Lifetime Value (LTV) Estimation** Using Markov Chains and Bayesian Buy-Till-You-Die (BTYD) Models
- **Dynamic Content Personalization** Using Contextual Bandits (LinUCB)
- **Next Best Action Model** Using Reinforcement Learning (Fitted Q Iteration)

### 📊 Marketing, Customer, and Content Analytics
- **Sentiment Analysis** Using Basic Transformers
- **Virtual Focus Groups** Using LLMs
- **RFM Analysis** of Customer Purchases 🧪
- **Customer Behavior Patterns** Using LSTM/Transformers
- **Customer/Item Embeddings** Using Word2vec and Doc2vec techniques
- **Media Mix Modeling** with Bayesian Models and Adstock Models for Attribution
- **Multitouch Channel Attribution** Using Deep Learning

### 🔍 Search Solutions
- **Retrieval-augmented Generation (RAG)** Using LLMs
- **Visual Search** by Artistic Style, Product Type, and Using Language-Image Models
- **Relational Data Querying** Using LLMs

### 👍 Recommendations
- **Collaborative Filtering** approaches including Neural and Hybrid Recommenders
- **Behavior Sequence Transformer** for improved recommendations
- **Graph Recommender** Using Node2Vec

### 📈 Demand Forecasting
- **Traditional Methods** using ETS, ARIMA, and Generalized Linear Models
- **Deep Learning Methods** like DeepAR and NeuralProphet
- **Bayesian Demand Models** for dynamic learning

### 💰 Pricing and Assortment
- **Strategic Price Optimization** using Reinforcement Learning (DQN) that learns Hi-Lo pricing policies 🚀
- **Market Response Functions** for understanding price elasticity 📚
- **Dynamic Pricing** using Thompson Sampling and with Limited Price Experimentation

### ⛓️ Supply Chain
- **Inventory Optimization** for single-echelon and multi-echelon systems
- **Supply Chain Simulator** for Reinforcement Learning Based Optimization 🚀
- **Supply Chain Control Tower** Using LLMs 🚀

## ✨ Features

- Comprehensive notebooks with step-by-step implementation
- Interactive demo applications
- Enterprise-ready code samples
- Detailed documentation for each use case
- Performance metrics and evaluation frameworks

## 🛠️ Technologies

Marketing House leverages the following technologies:

### Deep Learning
- TensorFlow
- PyTorch

### Reinforcement Learning
- RLlib

### Causal Inference
- DoWhy
- EconML

### Probabilistic/Bayesian Inference
- PyMC

### Generative AI
- LangChain

### Traditional Machine Learning
- statsmodels
- scikit-learn
- LightGBM

### Data Processing & Visualization
- NumPy
- pandas
- Matplotlib
- seaborn

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- Conda for environment management
- Poetry for dependency management

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/marketing-house.git
   cd marketing-house
   ```

2. Create a conda environment:
   ```bash
   conda create -n marketing-house python=3.11
   conda activate marketing-house
   ```

3. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

## 📋 Questionnaire

Our structured questionnaires help understand specific business needs when implementing a solution:

* [Business & Technical Requirements Questionnaire](https://your-questionnaire-url-here.com/business)
* [Solution Architecture Questionnaire](https://your-questionnaire-url-here.com/architecture)
* [Implementation Roadmap Questionnaire](https://your-questionnaire-url-here.com/roadmap)

## 🧩 Usage

Each use case is contained in its own directory with dedicated README files and instructions. Navigate to the specific use case directory to learn more about implementation details and how to run the demos.

For example:

```bash
cd price-optimization
jupyter notebook price_optimization_demo.ipynb
```

## 📁 Project Structure

```
marketing-house/
├── README.md
├── requirements.txt
├── price-optimization/
│   ├── README.md
│   ├── notebooks/
│   ├── data/
│   └── src/
├── customer-segmentation/
│   ├── README.md
│   ├── notebooks/
│   ├── data/
│   └── src/
└── ...
```

## 👥 Contributing

We welcome contributions from team members! Please follow these steps:

1. Check the issue tracker for available tasks or create a new issue to discuss your ideas
2. Fork the repository (for external contributors)
3. Create a new branch (`git checkout -b feature/your-feature-name`)
4. Make your changes
5. Commit your changes (`git commit -m 'Add some feature'`)
6. Push to the branch (`git push origin feature/your-feature-name`)
7. Open a Pull Request

## 📜 License

This project is proprietary and confidential. Unauthorized copying, distribution, or use is strictly prohibited.

## 📞 Contact

For questions or feedback, please contact [your-email@company.com](mailto:your-email@company.com).
