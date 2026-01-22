Generate forecasts for the VN1 forecasting competition using Nixtla, specfically TimeGPT-1 and TimeGPT-1-long-horizon, and also the median ensemble of these two models.

The competiton has 3 Phases, you have to use Phase 0 data and Phase 1 data to forecast Phase 2.
Data is Weekly (W-MON). Convert the data to Nixtla's format and then, given this is retail data, remove the leading zeros for each series.

You can find the description of the competition and the evaluation metric in Link. Make sure to use that exact evaluation metric in this link:https://www.datasource.ai/en/home/data-science-competitions-for-startups/vn1-forecasting-accuracy-challenge-phase-1/description

Extract the scores of the top 5 solutions from this link and compare them with our 3 models: https://www.datasource.ai/en/data-science-articles/announcing-the-winners-of-the-vn1-forecasting-datathon-advancing-supply-chain-efficiency-and-reducing-forecasting-errors

Data to download to the Nixtla Server (only use this sources):

Phase 0: https://www.datasource.ai/attachments/eyJpZCI6Ijk4NDYxNjE2NmZmZjM0MGRmNmE4MTczOGMyMzI2ZWI2LmNzdiIsInN0b3JhZ2UiOiJzdG9yZSIsIm1ldGFkYXRhIjp7ImZpbGVuYW1lIjoiUGhhc2UgMCAtIFNhbGVzLmNzdiIsInNpemUiOjEwODA0NjU0LCJtaW1lX3R5cGUiOiJ0ZXh0L2NzdiJ9fQ

Phase 1: https://www.datasource.ai/attachments/eyJpZCI6ImM2OGQxNGNmNTJkZDQ1MTUyZTg0M2FkMDAyMjVlN2NlLmNzdiIsInN0b3JhZ2UiOiJzdG9yZSIsIm1ldGFkYXRhIjp7ImZpbGVuYW1lIjoiUGhhc2UgMSAtIFNhbGVzLmNzdiIsInNpemUiOjEwMTgzOTYsIm1pbWVfdHlwZSI6InRleHQvY3N2In19

Phase 2: https://www.datasource.ai/attachments/eyJpZCI6IjhlNmJmNmU3ZTlhNWQ4NTcyNGVhNTI4YjAwNTk3OWE1LmNzdiIsInN0b3JhZ2UiOiJzdG9yZSIsIm1ldGFkYXRhIjp7ImZpbGVuYW1lIjoiUGhhc2UgMiAtIFNhbGVzLmNzdiIsInNpemUiOjEwMTI0MzcsIm1pbWVfdHlwZSI6InRleHQvY3N2In19