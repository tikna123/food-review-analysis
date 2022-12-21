# Food Review Analysis
# Problem Definition
A dataset that comprises product reviews aggregated from the Food review app has been provided. Use this dataset to conduct an analysis (with appropriate data visualisation), and generate insights. Generate features from unstructured text data, and/or use external data sources to augment your analysis.

# Method
I have used external dictionary and food BERT pretrained model to extract food
entities(features) from the reviews. I have also also done sentiment analysis on the reviews to understand the polarity(pos or neg) of the review. I have also extracted hashtags from the reviews. Added 3 columns in the existing data: foodEntities, sentiment_score and hashtags. The Notebook is self explanatory(can go through the notebook if need more details)
