# Heavy Metal Analysis

A statistical analysis of heavy metal mixtures and their association with disease outcomes. This project uses logistic regression and other techniques to explore the relationships between heavy metal exposure and disease outcomes.

---

## Analysis Techniques
The following methods are used in this project:
1. **Logistic Regression**: For binary disease outcomes.
2. **Weighted Quantile Sum (WQS) Regression**: For assessing mixture effects.
3. **Bayesian Kernel Machine Regression (BKMR)**: For exploring nonlinear associations and interactions.

---

## Project Structure

### **Folders and Files**
- **`data/`**: Place all datasets here. The primary dataset used is `FL_HeavyMetalMaster_111824_MissingRemoved.csv`.
- **`scripts/`**: Contains Python scripts for logistic regression models:
  - `model1_script.py`: Full logistic regression model including all metals.
  - `model2_script.py`: Excludes Arsenic from the model.
  - `model3_script.py`: Excludes Nickel from the model.
  - `model4_script.py`: Excludes Mercury from the model. 

---

## How to Run the Scripts
1. Clone this repository:
   ```bash
   git clone https://github.com/freemanchrislewis/heavy-metal-analysis.git
   cd heavy-metal-analysis
