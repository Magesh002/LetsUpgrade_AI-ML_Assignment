import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

Pat = [5, 4, 4, 3, 9, 4]
Jack = [4, 8, 7, 5, 1, 5]
Alex = [9, 9, 8, 10, 4, 10]

allScores = Pat + Jack + Alex
participantNames = (['Pat'] * len(Pat)) + (['Jack'] * len(Jack)) + (['Alex'] * len(Alex))

data = pd.DataFrame({'participants': participantNames, 'scores': allScores})
print("The generated data:\n", data)

participantMean = data.groupby('participants').mean()
print("\nThe calculated participantMean is:\n", participantMean)

lm = ols('scores ~ participants', data=data).fit()
table = sm.stats.anova_lm(lm)
print("\nThe anova calculation is:\n", table)