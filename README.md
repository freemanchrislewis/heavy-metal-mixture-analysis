<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>Heavy Metal Mixture Analysis</h1>
<p>A statistical analysis of heavy metal mixtures and their association with disease outcomes. This project uses logistic regression and other techniques to explore the relationships between heavy metal exposure and disease outcomes.</p>

<hr>

<h2>Analysis Techniques</h2>
<p>The following methods are used in this project:</p>
<ol>
    <li><strong>Logistic Regression</strong>: For binary disease outcomes.</li>
    <li><strong>Weighted Quantile Sum (WQS) Regression</strong>: For assessing mixture effects.</li>
    <li><strong>Bayesian Kernel Machine Regression (BKMR)</strong>: For exploring nonlinear associations and interactions.</li>
</ol>

<hr>

<h2>Repository Structure</h2>
<h3>Folders and Files</h3>
<ul>
    <li><strong><code>data/</code></strong>: Place all datasets here. The primary dataset used is <code>FL_HeavyMetalMaster_111824_MissingRemoved.csv</code>.</li>
    <li><strong><code>scripts/</code></strong>: Contains Python scripts for logistic regression models:
        <ul>
            <li><code>model1_script.py</code>: Full logistic regression model including all metals.</li>
            <li><code>model2_script.py</code>: Excludes Arsenic from the model.</li>
            <li><code>model3_script.py</code>: Excludes Nickel from the model.</li>
            <li><code>model4_script.py</code>: Excludes Mercury from the model.</li>
        </ul>
    </li>
</ul>

<hr>

<h2>How to Run the Scripts</h2>

<h3>1. Clone this Repository</h3>
<p>You can clone this repository to your local machine using either <strong>SSH</strong> or <strong>HTTPS with a Personal Access Token (PAT)</strong>. GitHub no longer supports password authentication for HTTPS URLs, so ensure you are using one of the methods below.</p>

<h4>Option 1: Clone Using SSH</h4>
<ol>
    <li>Copy the SSH URL:
        <pre><code>git@github.com:freemanchrislewis/heavy-metal-analysis.git</code></pre>
    </li>
    <li>Clone the repository:
        <pre><code>git clone git@github.com:freemanchrislewis/heavy-metal-analysis.git
cd heavy-metal-analysis</code></pre>
    </li>
</ol>

<h4>Option 2: Clone Using HTTPS with a Personal Access Token (PAT)</h4>
<ol>
    <li>Generate a Personal Access Token (PAT) from GitHub:
        <ul>
            <li>Go to <strong>Settings &gt; Developer Settings &gt; Personal Access Tokens</strong>.</li>
            <li>Generate a new token with the <code>repo</code> scope.</li>
        </ul>
    </li>
    <li>Clone the repository using the HTTPS URL:
        <pre><code>git clone https://&lt;YOUR_USERNAME&gt;@github.com/freemanchrislewis/heavy-metal-analysis.git
cd heavy-metal-analysis</code></pre>
    </li>
    <li>When prompted for a password, use your Personal Access Token instead.</li>
</ol>

<h3>2. Set up the Environment</h3>
<ol>
    <li>Ensure you have Python 3.8 or later installed on your system.</li>
    <li>(Optional) Create a virtual environment to isolate dependencies:
        <pre><code>python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate</code></pre>
    </li>
    <li>Install the required Python packages:
        <pre><code>pip install pandas numpy matplotlib seaborn statsmodels scikit-learn</code></pre>
    </li>
</ol>

<h3>3. Run the Scripts</h3>

<h4>Option 1: Using the Command Line</h4>
<ol>
    <li>Navigate to the <code>scripts</code> folder:
        <pre><code>cd scripts</code></pre>
    </li>
    <li>Run any script to generate results:
        <pre><code>python model1_script.py</code></pre>
    </li>
    <li>Repeat for other scripts as needed:
        <pre><code>python model2_script.py
python model3_script.py
python model4_script.py</code></pre>
    </li>
</ol>

<h4>Option 2: Using Jupyter Notebooks</h4>
<ol>
    <li>Start Jupyter Lab or Notebook:
        <pre><code>jupyter lab</code></pre>
    </li>
    <li>Navigate to the <code>scripts</code> folder in Jupyter.</li>
    <li>Open and execute any script cell by cell to see intermediate results interactively.</li>
</ol>

<hr>

<h2>Outputs and Results</h2>
<p>The scripts generate the following outputs:</p>
<ul>
    <li><strong>Logistic Regression Summary</strong>: Printed directly in the terminal or Jupyter Notebook.</li>
    <li><strong>ROC-AUC Scores</strong>: A measure of the model's performance, printed in the terminal.</li>
    <li><strong>Confusion Matrices</strong>: Displayed in the terminal or optionally saved to the <code>outputs</code> folder.</li>
    <li><strong>Optional Visualizations</strong>: ROC curves or other diagnostic plots, which may be displayed or saved.</li>
</ul>

<hr>

<h2>Contact Information</h2>
<p>For any questions or feedback regarding this project, please feel free to reach out:</p>
<ul>
    <li><strong>Freeman Lewis</strong></li>
    <li>Email: <a href="mailto:Flewi017@fiu.edu">Flewi017@fiu.edu</a></li>
    <li>GitHub: <a href="https://github.com/freemanchrislewis">freemanchrislewis</a></li>
</ul>

<hr>

</body>
</html>
