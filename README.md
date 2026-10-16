# PitchCheck: AI Cricket Match Decider

a simple machine learning project built with python and scikit-learn. it uses a decision tree classifier to predict whether it is safe and enjoyable to play outdoor cricket based on weather factors like rain, temperature, and wind.

# features

- trained using scikit-learn's decision tree classifier
- simple rule-based split logic mimicking human decision-making
- instant prediction for custom weather conditions

# dataset inputs

the model evaluates three simple parameters:
- rain: 0 for dry weather, 1 for active rain
- temperature: current temperature in celsius
- wind: 0 for calm conditions, 1 for strong wind

the target output is binary:
- 1: clear to play outside
- 0: stay indoors

# quickstart

1. clone the repository:
   git clone https://github.com/your-username/pitchcheck.git
   cd pitchcheck

2. install dependencies:
   pip install scikit-learn

3. run the script:
   python main.py
